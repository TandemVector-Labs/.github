#!/usr/bin/env python3
"""Read-only cooperative PR evidence gate; never grants merge authority."""
import argparse
import json
import re
import subprocess
import sys
import unittest
from urllib.parse import quote

SHA = re.compile(r"^[0-9a-f]{40}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
LOGIN = re.compile(r"^[A-Za-z0-9-]+$")


def assess(pr, branch, runs, reviews, head, base, checks, reviewer, final_pr, final_branch):
    issues = []
    def need(condition, reason):
        if not condition:
            issues.append(reason)
    def snapshot(p):
        return (p["head"]["sha"], p["base"]["sha"], p["base"]["ref"],
                p["state"], p["draft"], p.get("mergeable"))
    need(snapshot(pr) == snapshot(final_pr), "PR_CHANGED_DURING_READ")
    need(branch == final_branch == base, "BASE_CHANGED_OR_UNEXPECTED")
    need(pr["head"]["sha"] == head and pr["base"]["sha"] == base, "PR_SHA_MISMATCH")
    need(pr["state"] == "open" and not pr["draft"], "NOT_OPEN_NON_DRAFT")
    need(pr.get("mergeable") is True, "MERGEABILITY_NOT_CONFIRMED")
    need(bool(checks), "NO_EXPLICIT_CHECK_POLICY")
    for app, name in checks:
        matching = [r for r in runs if r.get("name") == name and (r.get("app") or {}).get("id") == app]
        need(len(matching) == 1 and matching[0].get("head_sha") == head
             and matching[0].get("status") == "completed"
             and matching[0].get("conclusion") == "success", "CHECK_NOT_EXACT_SUCCESS:" + str(app) + ":" + name)
    decisive = {}
    for r in sorted(reviews, key=lambda x: (x.get("submitted_at") or "", x["id"])):
        user = r.get("user") or {}
        login = user.get("login", "").lower()
        if login and r.get("state") in {"APPROVED", "CHANGES_REQUESTED", "DISMISSED"}:
            decisive[login] = r
    rr = decisive.get(reviewer.lower(), {})
    need(reviewer.lower() != pr["user"]["login"].lower(), "SELF_REVIEW")
    need(rr.get("state") == "APPROVED" and rr.get("commit_id") == head
         and (rr.get("user") or {}).get("type") == "User"
         and rr.get("author_association") in {"OWNER", "MEMBER", "COLLABORATOR"},
         "NO_EXACT_ELIGIBLE_REVIEW_RECORD")
    need(not any(r["state"] == "CHANGES_REQUESTED" for r in decisive.values()), "CHANGES_REQUESTED_REMAINS")
    return {"result": "BLOCKED" if issues else "METADATA_PASS_HUMAN_CONFIRMATION_REQUIRED",
            "issues": issues, "required_checks": len(checks),
            "server_enforcement": False, "merge_authorized": False}


def api(endpoint, pages=False):
    cmd = ["gh", "api", "--method", "GET"]
    if pages:
        cmd += ["--paginate", "--slurp"]
    cmd.append(endpoint)
    return json.loads(subprocess.check_output(cmd, text=True, timeout=60))


def inspect(args):
    root = "repos/" + args.repo
    pr_path = root + "/pulls/" + str(args.pr)
    p = api(pr_path)
    branch_path = root + "/branches/" + quote(p["base"]["ref"], safe="")
    b = api(branch_path)["commit"]["sha"]
    run_pages = api(root + "/commits/" + args.head + "/check-runs?filter=latest&per_page=100", True)
    runs = [r for page in run_pages for r in page["check_runs"]]
    reviews = [r for page in api(pr_path + "/reviews?per_page=100", True) for r in page]
    # These are observations, not an atomic server-side admission transaction.
    p2 = api(pr_path)
    b2 = api(branch_path)["commit"]["sha"]
    return assess(p, b, runs, reviews, args.head, args.base, args.check, args.reviewer, p2, b2)


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.h, self.b = "a"*40, "b"*40
        self.p = {"head":{"sha":self.h}, "base":{"sha":self.b,"ref":"main"},
                  "state":"open","draft":False,"mergeable":True,"user":{"login":"author"}}
        self.r = [{"id":1,"user":{"login":"peer","type":"User"},"state":"APPROVED",
                   "commit_id":self.h,"author_association":"OWNER","submitted_at":"2026-11-25"}]
        self.c = [{"name":"test","app":{"id":1},"head_sha":self.h,"status":"completed","conclusion":"success"}]
    def gate(self, **overrides):
        args = dict(pr=self.p,branch=self.b,runs=self.c,reviews=self.r,head=self.h,base=self.b,
                    checks=[(1,"test")],reviewer="peer",final_pr=self.p,final_branch=self.b)
        args.update(overrides)
        return assess(**args)
    def test_good_metadata_never_authorizes(self):
        r=self.gate(); self.assertEqual(r["result"],"METADATA_PASS_HUMAN_CONFIRMATION_REQUIRED")
        self.assertFalse(r["merge_authorized"]);self.assertFalse(r["server_enforcement"])
    def test_missing_checks(self): self.assertIn("NO_EXPLICIT_CHECK_POLICY",self.gate(checks=[])["issues"])
    def test_missing_run(self): self.assertEqual(self.gate(runs=[])["result"],"BLOCKED")
    def test_wrong_app(self): self.assertEqual(self.gate(checks=[(2,"test")])["result"],"BLOCKED")
    def test_duplicate(self): self.assertEqual(self.gate(runs=self.c*2)["result"],"BLOCKED")
    def test_skip(self): self.c[0]["conclusion"]="skipped"; self.assertEqual(self.gate()["result"],"BLOCKED")
    def test_stale_run(self): self.c[0]["head_sha"]=self.b; self.assertEqual(self.gate()["result"],"BLOCKED")
    def test_stale_review(self): self.r[0]["commit_id"]=self.b; self.assertEqual(self.gate()["result"],"BLOCKED")
    def test_self_review(self): self.assertIn("SELF_REVIEW",self.gate(reviewer="author")["issues"])
    def test_dismissal(self): self.r.append(dict(self.r[0],id=2,state="DISMISSED")); self.assertEqual(self.gate()["result"],"BLOCKED")
    def test_changes_requested(self):
        self.r.append(dict(self.r[0],id=2,state="CHANGES_REQUESTED",user={"login":"other","type":"User"}))
        self.assertIn("CHANGES_REQUESTED_REMAINS",self.gate()["issues"])
    def test_comment_not_approval(self): self.r[0]["state"]="COMMENTED"; self.assertEqual(self.gate()["result"],"BLOCKED")
    def test_draft(self): self.p["draft"]=True; self.assertIn("NOT_OPEN_NON_DRAFT",self.gate()["issues"])
    def test_race(self): self.assertIn("BASE_CHANGED_OR_UNEXPECTED",self.gate(final_branch=self.h)["issues"])
    def test_head_race(self):
        self.assertIn("PR_CHANGED_DURING_READ",self.gate(final_pr=dict(self.p,head={"sha":self.b}))["issues"])
    def test_unknown_mergeability(self): self.p["mergeable"]=None; self.assertEqual(self.gate()["result"],"BLOCKED")
    def test_review_bot(self): self.r[0]["user"]["type"]="Bot"; self.assertEqual(self.gate()["result"],"BLOCKED")


def check_arg(value):
    app, sep, name = value.partition(":")
    if not sep or not app.isdigit() or int(app) < 1 or not name.strip():
        raise argparse.ArgumentTypeError("expected APP_ID:CHECK_NAME")
    return int(app), name


def main():
    if sys.argv[1:] == ["--self-test"]:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests)
        return 0 if unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful() else 1
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo")
    parser.add_argument("pr",type=int)
    parser.add_argument("--head",required=True)
    parser.add_argument("--base",required=True)
    parser.add_argument("--reviewer",required=True)
    parser.add_argument("--check",type=check_arg,action="append",required=True)
    a=parser.parse_args()
    if not REPO.fullmatch(a.repo) or a.pr<1 or not SHA.fullmatch(a.head) or not SHA.fullmatch(a.base) or not LOGIN.fullmatch(a.reviewer) or len(set(a.check))!=len(a.check):
        parser.error("invalid or duplicate scope input")
    try:
        r=inspect(a)
    except (KeyError,ValueError,TypeError,subprocess.SubprocessError,OSError):
        r={"result":"BLOCKED","issues":["API_OR_SCHEMA_ERROR"],"server_enforcement":False,"merge_authorized":False}
    print(json.dumps(r,sort_keys=True))
    return 0 if r["result"]=="METADATA_PASS_HUMAN_CONFIRMATION_REQUIRED" else 2


if __name__ == "__main__":
    sys.exit(main())

