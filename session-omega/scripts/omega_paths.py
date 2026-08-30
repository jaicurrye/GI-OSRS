"""
omega_paths.py — locate the D&D data root, campaigns, and the installed dnd
skill's code, then run targeted extraction over a long campaign.

Session Omega never reads a 100-session log end to end. It pulls the handful of
things that carry signal:

    calibration   ### DM Calibration blocks written by /dm:dnd end
    arc           arc revisions, beat completions, Arc History
    mortality     deaths, death saves, downed characters, TPK near-misses
    npcs          NPC attitude/disposition shifts
    party         roster changes, plus character-file mtimes
    sessions      session headers, for pacing and length outliers

The file list matters more than the patterns. /dm:dnd save keeps only the two
most recent session entries in session-log.md and appends everything older to
session-log-archive.md, so a search that skips the archive finds ~2% of a long
campaign. NPC detail lives in npcs-full.md, not npcs.md.

For ad-hoc keyword lookups during a stage, prefer the dnd skill's own
campaign_search.py — it does AND-keyword search over the same files. This
module exists for the fixed regex targets above.

Usage:
    python3 omega_paths.py roots
    python3 omega_paths.py campaigns
    python3 omega_paths.py extract <campaign> [--what calibration,arc,...]
                                              [--context N] [--max-per-file N]

Environment:
    DND_CAMPAIGN_ROOT   data root (default ~/.claude/dnd), the same var the dnd
                        skill's paths.py honours.
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

DEFAULT_ROOT = pathlib.Path("~/.claude/dnd").expanduser()

SKILL_CANDIDATES = [
    "~/.claude/skills/dnd",
    "~/.claude/plugins/*/skills/dnd",
    "~/.claude/plugins/repos/*/*/skills/dnd",
    "~/.claude/skills/synced/*/skills/dnd",
]

# Directory copies made by the graph-init and ruleset-migration flows. Not
# campaigns, and listing them shows the user phantom duplicates.
BACKUP_RE = re.compile(r"\.backup[-.]|\.bak$")


def data_root() -> pathlib.Path:
    raw = os.environ.get("DND_CAMPAIGN_ROOT", "").strip()
    return pathlib.Path(raw).expanduser() if raw else DEFAULT_ROOT


def campaigns_dir() -> pathlib.Path:
    return data_root() / "campaigns"


def campaign_dir(name: str) -> pathlib.Path:
    """Locate a campaign, falling back to the legacy root like upstream does.

    paths.find_campaign checks ~/.claude/dnd even when DND_CAMPAIGN_ROOT is set
    elsewhere, so a campaign that has not yet been copied into a relocated root
    still loads. Without the same fallback, /dm:dnd load works and every omega
    command reports "no such campaign".
    """
    primary = campaigns_dir() / name
    if primary.is_dir():
        return primary
    legacy = DEFAULT_ROOT / "campaigns" / name
    if legacy.is_dir():
        return legacy
    return primary  # non-existent; callers report against the configured root


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
    out = []
    seen = set()
    for d in (campaigns_dir(), DEFAULT_ROOT / "campaigns"):
        if not d.is_dir():
            continue
        for c in sorted(p for p in d.iterdir() if p.is_dir()):
            if BACKUP_RE.search(c.name) or c.name in seen:
                continue
            seen.add(c.name)
            state = c / "state.md"
            sessions = None
            if state.exists():
                m = re.search(r"\*\*Session count:\*\*\s*(\d+)",
                              state.read_text(encoding="utf-8", errors="replace"))
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
# Word boundaries are load-bearing. Without them "ally" matches finally,
# actually, really; "dies?" matches studies, bodies, ladies. On a long log that
# fills the result cap with adverbs and starves every later file.

PATTERNS = {
    "calibration": r"###\s*DM Calibration|what worked this session|would you adjust",
    "arc": r"revision_log|Arc History|arc_number|/dm:dnd arc|status:\s*(complete|skipped)",
    "mortality": (r"death sav|\bdie(s|d)?\b|\bkilled\b|\bTPK\b|drops? to 0|"
                  r"\bunconscious\b|stabiliz|resurrect|revivif"),
    "npcs": (r"\battitude\b|\bdisposition\b|\bbetray(s|ed|al)?\b|turns? on the party|"
             r"\bally\b|\ballies\b|\bhostile\b|\bfriendly\b"),
    "party": (r"joins the party|leaves the party|new character|\bretired\b|"
              r"took over|now controls|/dm:dnd character"),
    "sessions": r"^#{1,3}\s*Session\s+\d+|^\*\*Session\s+\d+",
}

# Order matters only for readability; each file gets its own cap, so an early
# file can no longer starve a later one.
SEARCH_FILES = [
    "state.md",
    "session-log.md",
    "session-log-archive.md",   # holds all but the 2 most recent sessions
    "npcs.md",
    "npcs-full.md",             # NPC detail lives here, not in npcs.md
    "world.md",
    "world-nodes.md",
    "arc.md",
]


def extract(name, what, context=2, max_per_file=120):
    cdir = campaign_dir(name)
    if not cdir.is_dir():
        sys.exit(f"no such campaign: {cdir}")

    results = {}
    for key in what:
        pat = PATTERNS.get(key)
        if not pat:
            sys.exit(f"unknown extraction target: {key} (have: {', '.join(PATTERNS)})")
        rx = re.compile(pat, re.IGNORECASE | re.MULTILINE)

        hits, capped, searched, missing = [], [], [], []
        for fname in SEARCH_FILES:
            f = cdir / fname
            if not f.exists():
                missing.append(fname)
                continue
            searched.append(fname)
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            n_before = len(hits)
            for i, line in enumerate(lines):
                if rx.search(line):
                    if len(hits) - n_before >= max_per_file:
                        capped.append(fname)
                        break
                    lo, hi = max(0, i - context), min(len(lines), i + context + 1)
                    hits.append({"file": fname, "line": i + 1,
                                 "text": "\n".join(lines[lo:hi]).strip()})

        results[key] = {
            "count": len(hits),
            "files_searched": searched,
            "files_absent": missing,
            "files_capped": sorted(set(capped)),  # non-empty = results incomplete HERE
            "hits": hits,
        }
    return results


def character_timeline(name):
    """Roster changes by file mtime — when characters entered the campaign.

    Regex over the logs rarely captures a control handover; file mtimes date it
    directly. Copied files can carry a copy time, so treat this as a lead to
    confirm in the log, not proof.
    """
    cdir = campaign_dir(name) / "characters"
    if not cdir.is_dir():
        return {"characters_dir": str(cdir), "present": False, "characters": []}
    out = []
    for p in sorted(cdir.glob("*.md")):
        st = p.stat()
        out.append({
            "name": p.stem,
            "modified": __import__("datetime").datetime.fromtimestamp(st.st_mtime)
                        .isoformat(timespec="seconds"),
            "est_tokens": round(st.st_size / 4),
        })
    return {"characters_dir": str(cdir), "present": True,
            "characters": sorted(out, key=lambda c: c["modified"])}


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
    e.add_argument("--max-per-file", type=int, default=120)
    a = ap.parse_args()

    if a.cmd == "roots":
        skill = dnd_skill_root()
        print(json.dumps({
            "data_root": str(data_root()),
            "campaigns_dir": str(campaigns_dir()),
            "campaigns_dir_exists": campaigns_dir().is_dir(),
            "dnd_skill_root": str(skill) if skill else None,
            "templates_dir": str(skill / "templates") if skill else None,
            "campaign_search": str(skill / "scripts" / "campaign_search.py") if skill else None,
        }, indent=2))
    elif a.cmd == "campaigns":
        print(json.dumps(list_campaigns(), indent=2))
    else:
        what = [w.strip() for w in a.what.split(",") if w.strip()]
        out = extract(a.campaign, what, a.context, a.max_per_file)
        if "party" in what:
            out["party"]["character_timeline"] = character_timeline(a.campaign)
        print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
