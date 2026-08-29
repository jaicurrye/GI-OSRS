"""
omega_paths.py — locate the D&D data root, campaigns, and the installed dnd
skill's code, then run targeted extraction over a long campaign.

Session Omega never reads a 100-session log end to end. It pulls the handful of
things that actually carry signal:

    calibration   ### DM Calibration blocks written by /dm:dnd end
    arc           arc revisions, beat completions, Arc History
    mortality     deaths, death saves, downed characters, TPK near-misses
    npcs          NPC attitude/disposition shifts
    party         character-file creation dates (when the roster changed)
    sessions      session headers, for pacing and length outliers

Usage:
    python3 omega_paths.py roots
    python3 omega_paths.py campaigns
    python3 omega_paths.py extract <campaign> [--what calibration,arc,...]
                                              [--context N] [--max N]

Environment:
    DND_CAMPAIGN_ROOT   data root (default ~/.claude/dnd), same var the dnd
                        skill's own paths.py honours, so a relocated data tree
                        is found without extra configuration.
"""

import argparse
import json
import os
import pathlib
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DEFAULT_ROOT = "~/.claude/dnd"

# Where the dnd skill's code may live. Its templates/ are the source of truth
# for the files `build` writes, so we locate them rather than duplicating.
SKILL_CANDIDATES = [
    "~/.claude/skills/dnd",
    "~/.claude/plugins/*/skills/dnd",
    "~/.claude/plugins/repos/*/*/skills/dnd",
    "~/.claude/skills/synced/*/skills/dnd",
]


def data_root() -> pathlib.Path:
    raw = os.environ.get("DND_CAMPAIGN_ROOT", "").strip()
    return pathlib.Path(raw or DEFAULT_ROOT).expanduser()


def campaigns_dir() -> pathlib.Path:
    return data_root() / "campaigns"


def campaign_dir(name: str) -> pathlib.Path:
    return campaigns_dir() / name


def dnd_skill_root():
    """Best-effort location of the installed dnd skill's code directory."""
    for pattern in SKILL_CANDIDATES:
        base = pathlib.Path(pattern).expanduser()
        if "*" in str(base):
            root = pathlib.Path(str(base).split("*")[0]).expanduser()
            rel = str(base)[len(str(root)):].lstrip("/")
            if not root.exists():
                continue
            matches = sorted(root.glob(rel))
        else:
            matches = [base] if base.exists() else []
        for m in matches:
            if (m / "SKILL.md").exists() and (m / "templates").is_dir():
                return m
    return None


def list_campaigns():
    d = campaigns_dir()
    if not d.is_dir():
        return []
    out = []
    for c in sorted(p for p in d.iterdir() if p.is_dir()):
        state = c / "state.md"
        sessions = None
        if state.exists():
            m = re.search(r"\*\*Session count:\*\*\s*(\d+)", state.read_text(errors="replace"))
            if m:
                sessions = int(m.group(1))
        out.append({
            "name": c.name,
            "path": str(c),
            "sessions": sessions,
            "files": sorted(p.name for p in c.iterdir() if p.is_file()),
            "characters": sorted(p.stem for p in (c / "characters").glob("*.md"))
            if (c / "characters").is_dir() else [],
        })
    return out


# ── extraction ────────────────────────────────────────────────────────────
# Each pattern is deliberately broad on the recall side. Session Omega would
# rather hand the model twelve irrelevant hits than silently miss the session
# where a character died.

PATTERNS = {
    "calibration": r"###\s*DM Calibration|what worked this session|would you adjust",
    "arc": r"revision_log|Arc History|beat .*(complete|skipped)|status:\s*complete|arc_number|/dm:dnd arc",
    "mortality": r"death sav|dies?\b|died\b|killed\b|\bTPK\b|drops? to 0|unconscious|stabiliz|resurrect|revivif",
    "npcs": r"attitude|disposition|betray|turns? on the party|ally|hostile|friendly",
    "party": r"joins the party|leaves the party|new character|retired|took over|now controls",
    "sessions": r"^#{1,3}\s*Session\s+\d+|^\*\*Session\s+\d+",
}

SEARCH_FILES = ["session-log.md", "state.md", "npcs.md", "world.md", "arc.md"]


def extract(name, what, context=2, max_hits=400):
    cdir = campaign_dir(name)
    if not cdir.is_dir():
        sys.exit(f"no such campaign: {cdir}")

    results = {}
    for key in what:
        pat = PATTERNS.get(key)
        if not pat:
            sys.exit(f"unknown extraction target: {key} (have: {', '.join(PATTERNS)})")
        rx = re.compile(pat, re.IGNORECASE | re.MULTILINE)
        hits = []
        for fname in SEARCH_FILES:
            f = cdir / fname
            if not f.exists():
                continue
            lines = f.read_text(errors="replace").splitlines()
            for i, line in enumerate(lines):
                if rx.search(line):
                    lo, hi = max(0, i - context), min(len(lines), i + context + 1)
                    hits.append({
                        "file": fname,
                        "line": i + 1,
                        "text": "\n".join(lines[lo:hi]).strip(),
                    })
                    if len(hits) >= max_hits:
                        break
            if len(hits) >= max_hits:
                break
        results[key] = {"count": len(hits), "truncated": len(hits) >= max_hits, "hits": hits}
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("roots")
    sub.add_parser("campaigns")
    e = sub.add_parser("extract")
    e.add_argument("campaign")
    e.add_argument("--what", default="calibration,arc,mortality,npcs,party,sessions")
    e.add_argument("--context", type=int, default=2)
    e.add_argument("--max", type=int, default=400)
    a = ap.parse_args()

    if a.cmd == "roots":
        skill = dnd_skill_root()
        print(json.dumps({
            "data_root": str(data_root()),
            "campaigns_dir": str(campaigns_dir()),
            "campaigns_dir_exists": campaigns_dir().is_dir(),
            "dnd_skill_root": str(skill) if skill else None,
            "templates_dir": str(skill / "templates") if skill else None,
        }, indent=2))
    elif a.cmd == "campaigns":
        print(json.dumps(list_campaigns(), indent=2))
    else:
        what = [w.strip() for w in a.what.split(",") if w.strip()]
        print(json.dumps(extract(a.campaign, what, a.context, a.max), indent=2))


if __name__ == "__main__":
    main()
