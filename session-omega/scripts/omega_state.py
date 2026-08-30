"""
omega_state.py — the resumable progress file behind Session Omega.

Every stage writes as it goes, so a closed laptop, a crash, or a context
compaction costs at most the answer in flight. State lives beside the campaign
it reviews:

    <campaigns>/<campaign>/omega/progress.json

Usage:
    python3 omega_state.py init <campaign> [--new-campaign <name>]
    python3 omega_state.py status <campaign>
    python3 omega_state.py set <campaign> <stage> <pending|active|done|skipped>
    python3 omega_state.py record <campaign> <stage> <key> <value>
    python3 omega_state.py record <campaign> <stage> <key> --stdin
    python3 omega_state.py dispute <campaign> <claim> --dm <text> --player <text>
    python3 omega_state.py dump <campaign> [--stage S] [--key K]
    python3 omega_state.py resolve <campaign> <index> <text>

Sealed answers: a key beginning with `sealed_` is hidden from `dump` unless
named with `--key`. `predict` uses this so question 5 (next-campaign appetite)
cannot be read at `evidence` alongside questions 1-4 — it unseals at `spec`,
after the taste profile has been written independently.
"""

import argparse
import datetime
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from omega_paths import campaign_dir  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

STAGES = ["predict", "review", "evidence", "tooling", "chronicle", "contract",
          "spec", "world", "party", "build", "audit"]
STATUSES = ["pending", "active", "done", "skipped"]


def omega_dir(campaign):
    return campaign_dir(campaign) / "omega"


def progress_path(campaign):
    return omega_dir(campaign) / "progress.json"


def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def load(campaign):
    p = progress_path(campaign)
    if not p.exists():
        sys.exit(f"no Session Omega state for '{campaign}'. Run: omega_state.py init {campaign}")
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"progress file is corrupt: {p}\n  {e}\n"
                 "Fix it by hand or move it aside and re-init; do not overwrite "
                 "it blindly, it holds the recorded answers.")


def save(campaign, data):
    d = omega_dir(campaign)
    d.mkdir(parents=True, exist_ok=True)
    data["updated"] = now()
    # Write-then-rename so an interrupted write can never truncate the file.
    tmp = progress_path(campaign).with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(progress_path(campaign))


def cmd_init(a):
    p = progress_path(a.campaign)
    if p.exists():
        print(json.dumps({"already_initialized": True, "path": str(p)}, indent=2))
        return
    if not campaign_dir(a.campaign).is_dir():
        sys.exit(f"no such campaign: {campaign_dir(a.campaign)}")
    save(a.campaign, {
        "campaign": a.campaign,
        "new_campaign": a.new_campaign,
        "created": now(),
        "stages": {s: {"status": "pending", "answers": {}} for s in STAGES},
        "disputed": [],
    })
    print(json.dumps({"initialized": str(p), "stages": STAGES}, indent=2))


def cmd_status(a):
    d = load(a.campaign)
    stages = d["stages"]
    nxt = next((s for s in STAGES if stages[s]["status"] in ("pending", "active")), None)
    print(json.dumps({
        "campaign": d["campaign"],
        "new_campaign": d.get("new_campaign"),
        "updated": d.get("updated"),
        "stages": {k: v["status"] for k, v in d["stages"].items()},
        "answers_recorded": {k: len(v["answers"]) for k, v in d["stages"].items() if v["answers"]},
        "disputed": len(d.get("disputed", [])),
        "disputes_unresolved": sum(1 for x in d.get("disputed", [])
                                   if not x.get("resolution")),
        "next": nxt,
        "reminder": ("mark a stage done with `set <campaign> <stage> done` — "
                     "recording answers alone leaves it active"),
    }, indent=2))


def cmd_set(a):
    if a.stage not in STAGES:
        sys.exit(f"unknown stage '{a.stage}' (have: {', '.join(STAGES)})")
    if a.status not in STATUSES:
        sys.exit(f"unknown status '{a.status}' (have: {', '.join(STATUSES)})")
    d = load(a.campaign)
    d["stages"][a.stage]["status"] = a.status
    d["stages"][a.stage]["status_at"] = now()
    save(a.campaign, d)
    print(f"{a.stage} -> {a.status}")


def cmd_record(a):
    if a.stage not in STAGES:
        sys.exit(f"unknown stage '{a.stage}' (have: {', '.join(STAGES)})")
    value = sys.stdin.read().rstrip("\n") if a.stdin else a.value
    if value is None:
        sys.exit("provide a value or --stdin")
    d = load(a.campaign)
    d["stages"][a.stage]["answers"][a.key] = {"value": value, "at": now()}
    if d["stages"][a.stage]["status"] == "pending":
        d["stages"][a.stage]["status"] = "active"
    save(a.campaign, d)
    print(f"recorded {a.stage}.{a.key} ({len(value)} chars)")


def cmd_dispute(a):
    d = load(a.campaign)
    d.setdefault("disputed", []).append({
        "claim": a.claim, "dm_position": a.dm, "player_position": a.player,
        "at": now(), "resolution": None,
    })
    save(a.campaign, d)
    print(f"disputed #{len(d['disputed'])} recorded")


def cmd_dump(a):
    d = load(a.campaign)
    if a.stage and a.stage not in STAGES:
        sys.exit(f"unknown stage '{a.stage}' (have: {', '.join(STAGES)})")

    if a.key:
        if not a.stage:
            sys.exit("--key requires --stage")
        answers = d["stages"][a.stage]["answers"]
        if a.key not in answers:
            sys.exit(f"no answer '{a.key}' recorded for stage '{a.stage}'")
        print(json.dumps({a.key: answers[a.key]}, indent=2, ensure_ascii=False))
        return

    def redact(stage):
        st = dict(stage)
        sealed = [k for k in st["answers"] if k.startswith("sealed_")]
        st["answers"] = {k: v for k, v in st["answers"].items()
                         if not k.startswith("sealed_")}
        if sealed:
            st["sealed_keys_withheld"] = sealed
        return st

    if a.stage:
        print(json.dumps(redact(d["stages"][a.stage]), indent=2, ensure_ascii=False))
    else:
        out = dict(d)
        out["stages"] = {k: redact(v) for k, v in d["stages"].items()}
        print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_resolve(a):
    d = load(a.campaign)
    disputes = d.get("disputed", [])
    if not 1 <= a.index <= len(disputes):
        sys.exit(f"no dispute #{a.index} (have {len(disputes)})")
    disputes[a.index - 1]["resolution"] = a.text
    disputes[a.index - 1]["resolved_at"] = now()
    save(a.campaign, d)
    print(f"dispute #{a.index} resolved")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("init"); i.add_argument("campaign"); i.add_argument("--new-campaign", default=None); i.set_defaults(fn=cmd_init)
    s = sub.add_parser("status"); s.add_argument("campaign"); s.set_defaults(fn=cmd_status)
    t = sub.add_parser("set"); t.add_argument("campaign"); t.add_argument("stage"); t.add_argument("status"); t.set_defaults(fn=cmd_set)
    r = sub.add_parser("record"); r.add_argument("campaign"); r.add_argument("stage"); r.add_argument("key")
    r.add_argument("value", nargs="?"); r.add_argument("--stdin", action="store_true"); r.set_defaults(fn=cmd_record)
    p = sub.add_parser("dispute"); p.add_argument("campaign"); p.add_argument("claim")
    p.add_argument("--dm", required=True); p.add_argument("--player", required=True); p.set_defaults(fn=cmd_dispute)
    u = sub.add_parser("dump"); u.add_argument("campaign"); u.add_argument("--stage", default=None)
    u.add_argument("--key", default=None); u.set_defaults(fn=cmd_dump)
    v = sub.add_parser("resolve"); v.add_argument("campaign"); v.add_argument("index", type=int)
    v.add_argument("text"); v.set_defaults(fn=cmd_resolve)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
