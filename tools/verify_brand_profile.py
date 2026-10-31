#!/usr/bin/env python3
"""Read-only, dependency-free GitHub organization branding verification.

Checks image integrity, accessible links, project attribution, and path safety.
Safe for untrusted pull_request code: no network, no secrets, no file changes.
Run: python3 tools/verify_brand_profile.py [--self-test]
"""
from __future__ import annotations

import argparse
import html.parser
import hashlib
import json
from pathlib import Path, PureWindowsPath
import re
import struct
import sys
import tempfile
import zlib
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SVG_NS = "{http://www.w3.org/2000/svg}"
EXPECTED_PREVIEWS = (
    "AppearanceStudio-Core.png",
    "ChatGPTRemoteCommander.png",
    "DirectInternetMethod.png",
    "FreeNetHub.png",
    "OpenInternetGateway.png",
    "PersianWordAgent.png",
    "TaskbarMonitorEnhanced.png",
    "remote-commander-browser.png",
)
FEATURED_SCREENSHOTS = {
    "OpenInternetGateway": ("../brand/screenshots/OpenInternetGateway-dashboard.png", (1180, 760)),
    "FreeNetHub": ("../brand/screenshots/FreeNetHub-R37-dashboard.png", (1440, 1020)),
}
FEATURED_HERO = {
    "ChatGPTRemoteCommander": ("../brand/hero/ChatGPTRemoteCommander-hero-20261030.png", (1774, 887), "846c64417f06bd47de9ecbbd3cc689ff45d19d1c"),
    "remote-commander-browser": ("../brand/hero/RemoteCommanderBrowser-hero-20261030.png", (1774, 887), "be93df7c2165ad452d76424548e9441b000ba01a"),
}
CARD_RE = re.compile(r"\[!\[([^\]]+)\]\(([^)]+)\)\]\((https://github\.com/[^)]+)\)")
MD_LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
FENCE = chr(96) * 3


class AuditError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


class HTMLImages(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            self.images.append({k: v or "" for k, v in attrs})


def relative_file(from_doc: Path, path: str, root: Path) -> Path:
    require(path != "", "EMPTY_LOCAL_PATH")
    require(not path.startswith(("/", "\\", "//")), "ABSOLUTE_PATH")
    require(not re.search(r"(?i)%2f|%5c", path), "ENCODED_SEPARATOR")
    from urllib.parse import unquote
    path = unquote(path)
    require(not re.match(r"^[A-Za-z][\w+.-]*:", path), "UNEXPECTED_SCHEME")
    require("\\" not in path and "\x00" not in path, "UNSAFE_PATH_CHARACTER")
    full = (from_doc.parent / path.split("#", 1)[0].split("?", 1)[0]).resolve()
    require(full.is_relative_to(root.resolve()), "LINK_ESCAPES_REPOSITORY")
    require(full.exists(), "MISSING_LOCAL_TARGET:" + path)
    return full


def png_size(data: bytes, max_bytes: int = 1_000_000) -> tuple[int, int]:
    require(len(data) <= max_bytes, "PNG_TOO_LARGE")
    require(data.startswith(b"\x89PNG\r\n\x1a\n"), "PNG_SIGNATURE")
    offset = 8
    dimensions = None
    first = True
    ended = False
    chunks = 0
    while offset < len(data):
        require(offset + 12 <= len(data), "PNG_TRUNCATED_CHUNK")
        size = struct.unpack(">I", data[offset : offset + 4])[0]
        kind = data[offset + 4 : offset + 8]
        require(size <= len(data) - offset - 12, "PNG_INVALID_LENGTH")
        payload = data[offset + 8 : offset + 8 + size]
        expected = struct.unpack(">I", data[offset + 8 + size : offset + 12 + size])[0]
        actual = zlib.crc32(kind + payload) & 0xFFFFFFFF
        require(expected == actual, "PNG_CRC")
        if first:
            require(kind == b"IHDR" and size == 13, "PNG_MISSING_IHDR")
            width, height = struct.unpack(">II", payload[:8])
            require(width > 0 and height > 0, "PNG_BAD_DIMENSIONS")
            dimensions = (width, height)
            first = False
        if kind == b"IEND":
            require(size == 0, "PNG_BAD_IEND")
            ended = True
            require(offset + 12 == len(data), "PNG_TRAILING_DATA")
        offset += 12 + size
        chunks += 1
        require(chunks < 5000, "PNG_CHUNK_LIMIT")
    require(ended and dimensions is not None, "PNG_NO_IEND")
    return dimensions


def svg_check(source: bytes) -> None:
    require(len(source) < 50_000, "SVG_TOO_LARGE")
    lowered = source.lower()
    require(b"<!doctype" not in lowered and b"<!entity" not in lowered, "SVG_DOCTYPE")
    try:
        root = ET.fromstring(source)
    except ET.ParseError as exc:
        raise AuditError("SVG_PARSE_ERROR") from exc
    require(root.tag == SVG_NS + "svg", "SVG_ROOT")
    require(root.find(SVG_NS + "title") is not None, "SVG_TITLE")
    allowed = {
        "svg", "defs", "title", "desc", "g", "linearGradient",
        "radialGradient", "stop", "pattern", "clipPath",
        "rect", "path", "ellipse", "circle", "text",
    }
    for item in root.iter():
        tag = item.tag.rsplit("}", 1)[-1]
        require(tag in allowed, "SVG_DISALLOWED_ELEMENT:" + tag)
        for key, value in item.attrib.items():
            attr = key.rsplit("}", 1)[-1].lower()
            require(not attr.startswith("on"), "SVG_EVENT_ATTRIBUTE")
            require(attr not in ("href", "style"), "SVG_LINK_OR_STYLE")
            require(not re.search(r"(?i)javascript:|data:|https?://", value), "SVG_REMOTE_CONTENT")
            require(not re.search(r"(?i)url\(\s*(?!#)", value), "SVG_EXTERNAL_URL_REFERENCE")


def iter_links(text: str) -> list[str]:
    urls: list[str] = []
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith(("~~~", FENCE)):
            fenced = not fenced
            continue
        if fenced:
            continue
        for m in MD_LINK_RE.finditer(line):
            urls.append(m.group(1).strip().strip("<>"))
    return urls


def audit(root: Path = ROOT) -> dict[str, object]:
    brand = root / "brand"
    profile = root / "profile/README.md"
    require(profile.is_file(), "ORG_PROFILE_MISSING")
    profile_text = profile.read_text(encoding="utf-8")
    require("TandemVector Labs" in profile_text, "BRAND_IDENTITY_MISSING")
    require("TandemVector-Labs" in profile_text, "CURRENT_NAMESPACE_MISSING")
    require("not a claim of registered company status" in profile_text, "BRAND_STATUS_CAVEAT_MISSING")
    for owner in ("GOD13emad", "mohammadmohammadzadeh19960-code"):
        require("https://github.com/" + owner in profile_text, "OWNER_LINK_MISSING:" + owner)

    previews = sorted((brand / "social").glob("*.png"), key=lambda p: p.name)
    require([p.name for p in previews] == sorted(EXPECTED_PREVIEWS), "SOCIAL_PREVIEW_SET")
    pngs = [(brand / "avatar.png", (512, 512))]
    avatar_file = brand / "avatar.png"
    require(avatar_file.is_file(), "PNG_FILE_MISSING")
    avatar = avatar_file.read_bytes()
    approved_avatar_blob = hashlib.sha1(f"blob {len(avatar)}\0".encode("ascii") + avatar).hexdigest()
    require(approved_avatar_blob == "296408af322c2c22d9265749b113946db5f17c6a", "AVATAR_NOT_APPROVED_BLOB")
    pngs.extend((x, (1280, 640)) for x in previews)
    for file, dims in pngs:
        require(file.is_file(), "PNG_FILE_MISSING")
        require(png_size(file.read_bytes()) == dims, "PNG_DIMENSIONS:" + file.name)
    # Verify the already-approved raster banner independently of the display markup.
    banner_payload = (brand / "banner-approved-20261030.webp").read_bytes()
    require(10_000 < len(banner_payload) < 200_000, "BANNER_WEBP_SIZE")
    require(banner_payload[:4] == b"RIFF" and banner_payload[8:12] == b"WEBP", "BANNER_WEBP_SIGNATURE")
    require(int.from_bytes(banner_payload[4:8], "little") + 8 == len(banner_payload),
            "BANNER_WEBP_RIFF_LENGTH")
    require(banner_payload[12:16] in (b"VP8 ", b"VP8L", b"VP8X"), "BANNER_WEBP_PAYLOAD")
    banner_blob = hashlib.sha1(
        f"blob {len(banner_payload)}\0".encode("ascii") + banner_payload
    ).hexdigest()
    require(banner_blob == "0b55a3f7bc49163e16f065e3240a0fe241dbb5ee",
            "BANNER_NOT_APPROVED_BLOB")
    for filename in ("banner.svg", "monogram.svg"):
        file = brand / filename
        require(file.is_file(), "SVG_FILE_MISSING:" + filename)
        svg_check(file.read_bytes())

    parser = HTMLImages()
    parser.feed(profile_text)
    require(len(parser.images) >= 3, "PROFILE_HTML_IMAGES_MISSING")
    sources: list[str] = []
    for img in parser.images:
        src, alt = img.get("src", ""), img.get("alt", "")
        require(alt.strip(), "PROFILE_IMG_ALT_MISSING")
        if src.startswith("https://"):
            require(src.startswith("https://avatars.githubusercontent.com/u/"), "NON_OWNER_EXTERNAL_IMAGE")
        else:
            require(relative_file(profile, src, root).is_file(), "PROFILE_IMAGE_NOT_FILE")
        sources.append(src)
    require(sources.count("../brand/banner-approved-20261030.webp") == 1, "APPROVED_BANNER_NOT_EMBEDDED")
    require(sum(x.startswith("https://avatars.githubusercontent.com/u/") for x in sources) == 2,
            "COOWNER_AVATAR_COUNT")

    featured = CARD_RE.findall(profile_text)
    require(len(featured) == 4, "FEATURED_CARD_COUNT")
    feature_images = set()
    for alt, path, target in featured:
        require(alt.strip(), "FEATURED_IMG_ALT_EMPTY")
        require(target.startswith("https://github.com/TandemVector-Labs/"), "FEATURED_TARGET_NOT_ORG")
        slug = target.removeprefix("https://github.com/TandemVector-Labs/")
        require(slug in {"OpenInternetGateway", "FreeNetHub", "remote-commander-browser", "ChatGPTRemoteCommander"},
                "FEATURED_UNKNOWN_TARGET")
        approved_blob = None
        if slug in FEATURED_HERO:
            expected_path, dimensions, approved_blob = FEATURED_HERO[slug]
        elif slug in FEATURED_SCREENSHOTS:
            expected_path, dimensions = FEATURED_SCREENSHOTS[slug]
        else:
            expected_path, dimensions = f"../brand/social/{slug}.png", (1280, 640)
            require(f"{slug}.png" in EXPECTED_PREVIEWS, "FEATURED_SOCIAL_UNKNOWN")
        require(path == expected_path, "FEATURED_IMG_NOT_CANONICAL")
        img = relative_file(profile, path, root)
        require(img.is_file(), "FEATURED_IMG_NOT_LOCAL")
        payload = img.read_bytes()
        require(png_size(payload, max_bytes=2_100_000 if approved_blob else 1_000_000) == dimensions,
                "FEATURED_IMG_DIMENSIONS")
        if approved_blob:
            actual_blob = hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()
            require(actual_blob == approved_blob, "FEATURED_HERO_BYTES_CHANGED")
        feature_images.add(path)
    require(len(feature_images) == 4, "FEATURED_IMAGE_REPEATED")

    checked, excluded, markdown_count = 0, 0, 0
    for doc in root.rglob("*.md"):
        if ".git" in doc.parts:
            continue
        markdown_count += 1
        for link in iter_links(doc.read_text(encoding="utf-8")):
            if link.startswith(("https://", "http://", "#", "mailto:")):
                excluded += 1
                continue
            if link:
                relative_file(doc, link, root)
                checked += 1
    require(markdown_count > 3, "NO_MARKDOWN_SCOPE")
    return {
        "status": "PASS",
        "markdown_files": markdown_count,
        "relative_markdown_links": checked,
        "external_and_anchor_links_excluded": excluded,
        "preview_pngs": len(previews),
        "avatar_pngs": 1,
        "svg_files": 2,
        "featured_cards": len(featured),
        "owner_avatar_links": 2,
        "only_local_artwork_and_public_owner_avatars": True,
    }


def self_test() -> None:
    def chunk(kind: bytes, payload: bytes) -> bytes:
        crc = zlib.crc32(kind + payload) & 0xFFFFFFFF
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", crc)

    ihdr = struct.pack(">IIBBBBB", 1, 1, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(
        b"IDAT", zlib.compress(b"\x00\x00\x00\x00\xff")
    ) + chunk(b"IEND", b"")
    require(png_size(png) == (1, 1), "TEST_VALID_PNG")
    bad = bytearray(png)
    bad[-6] ^= 1
    try:
        png_size(bytes(bad))
        raise AssertionError("CRC_MUTATION_NOT_REJECTED")
    except AuditError:
        pass

    svg_check(b'<svg xmlns="http://www.w3.org/2000/svg"><title>Test</title></svg>')
    try:
        svg_check(b'<svg xmlns="http://www.w3.org/2000/svg"><title>Test</title><script/></svg>')
        raise AssertionError("SVG_SCRIPT_NOT_REJECTED")
    except AuditError:
        pass

    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        (base / "a").mkdir()
        (base / "a" / "exists.md").write_text("ok", encoding="utf-8")
        require(relative_file(base / "a" / "profile.md", "exists.md", base).is_file(),
                "TEST_RELATIVE_LINK")
        for candidate in ("../../outside", "/etc/passwd", "https://bad.example"):
            try:
                relative_file(base / "a" / "profile.md", candidate, base)
                raise AssertionError("UNSAFE_LINK_NOT_REJECTED")
            except AuditError:
                pass
    mixed_case = [
        PureWindowsPath("remote-commander-browser.png"),
        PureWindowsPath("TaskbarMonitorEnhanced.png"),
    ]
    require([p.name for p in sorted(mixed_case, key=lambda p: p.name)] ==
            sorted(p.name for p in mixed_case), "TEST_PORTABLE_PREVIEW_ORDER")
    print(json.dumps({"selftest": "PASS", "cases": 9}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
        else:
            print(json.dumps(audit(), sort_keys=True))
    except (AuditError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}))
        sys.exit(1)
