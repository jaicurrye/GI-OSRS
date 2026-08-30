"""
omega_health.py — measure what a long campaign did to the machinery.

The `tooling` stage asks whether the plugin served the table well. Most of that
question is answerable with numbers, and the numbers matter because the dnd
skill is explicitly token-budgeted.

/dm:dnd load reads state.md, world.md IN FULL, npcs.md index rows, and ALL of
characters/*.md. Those are a tax paid at the start of every session for the life
of the campaign. session-log.md, session-log-archive.md, npcs-full.md,
world-nodes.md and arc.md are read on demand and can be large for free.

Getting that split wrong sends the optimization at the wrong file: a party of
four level-20 sheets is frequently the second-largest recurring cost after
state.md, and a world.md left full of template placeholders is read in full
every session to say nothing.

Reports:
  files      size and line count per campaign file
  sections   per-section size within state.md — the load-path breakdown
  features   which optional systems left artifacts behind (graph, pins, arc,
             dials, display, characters)
  all        everything, plus flags for the known bloat patterns

Usage:
    python3 omega_health.py all <campaign>
    python3 omega_health.py sections <campaign>
"""

import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from omega_paths import campaign_dir, data_root  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Read in full at every /dm:dnd load. Size here is a per-session tax.
LOAD_PATH = {"state.md", "world.md"}
# Read at load, but index rows only — size is a partial cost.
PARTIAL = {"npcs.md"}
# Read only on demand. Size here is cheap.
COLD = {"session-log.md", "session-log-archive.md", "npcs-full.md",
        "world-nodes.md", "world-seeds.md", "arc.md", "session-tail.md"}


def classify(rel):
    """Load-path class for a campaign-relative path."""
    if rel in LOAD_PATH:
        return "full"
    if rel in PARTIAL:
        return "index-only"
    if rel.startswith("characters/"):
        return "full"          # every character file is read at load
    if rel in COLD or rel.startswith("source/"):
        return "on-demand"
    return "unknown"

# ~4 bytes per token is the standard rough estimate for English prose. Good
# enough to tell 2k from 20k, which is the only distinction that matters here.
BYTES_PER_TOKEN = 4

# Section-size thresholds in estimated tokens. These are judgement calls, not
# limits from the skill itself: a load-path section past ~1500 tokens is worth
# looking at, past ~3000 it is displacing the session.
SECTION_WARN = 1500
SECTION_HIGH = 3000


def est_tokens(n_bytes):
    return round(n_bytes / BYTES_PER_TOKEN)


def files_report(cdir):
    out = []
    for p in sorted(cdir.rglob("*")):
        if not p.is_file() or p.suffix not in (".md", ".json"):
            continue
        if "omega" in p.relative_to(cdir).parts:
            continue
        rel = str(p.relative_to(cdir))
        b = p.stat().st_size
        out.append({
            "file": rel,
            "bytes": b,
            "est_tokens": est_tokens(b),
            "lines": len(p.read_text(encoding="utf-8", errors="replace").splitlines()),
            "load_class": classify(rel),
        })
    return sorted(out, key=lambda r: -r["bytes"])


def load_path_total(files):
    """The number this stage exists to report: cost of starting one session."""
    full = sum(f["est_tokens"] for f in files if f["load_class"] == "full")
    idx = sum(f["est_tokens"] for f in files if f["load_class"] == "index-only")
    return {
        "full_read_est_tokens": full,
        "index_only_est_tokens_upper_bound": idx,
        "per_session_est_tokens": full,
        "breakdown": [{"file": f["file"], "est_tokens": f["est_tokens"]}
                      for f in files if f["load_class"] == "full"],
    }


def sections_report(cdir):
    """Per-section size within state.md — where the per-session tax actually goes."""
    state = cdir / "state.md"
    if not state.exists():
        return {"error": f"no state.md at {state}"}
    text = state.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    marks = [(i, ln[3:].strip()) for i, ln in enumerate(lines) if ln.startswith("## ")]
    sections = []
    for idx, (start, title) in enumerate(marks):
        end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        body = "\n".join(lines[start:end])
        tok = est_tokens(len(body.encode("utf-8")))
        sections.append({
            "section": title,
            "lines": end - start,
            "est_tokens": tok,
            "flag": "high" if tok >= SECTION_HIGH else "warn" if tok >= SECTION_WARN else None,
        })

    total = est_tokens(len(text.encode("utf-8")))
    present = {m[1] for m in marks}
    return {
        "state_md_est_tokens": total,
        "sections": sorted(sections, key=lambda s: -s["est_tokens"]),
        "dm_style_notes_present": "DM Style Notes" in present,
        "missing_expected": [s for s in ("DM Style Notes", "Live State Flags",
                                         "Session Flags", "Campaign Arc",
                                         "Pinned Facts", "Continuity Archive")
                             if s not in present],
    }


def features_report(cdir):
    """Infer which optional systems were actually used, from artifacts left behind."""
    state = cdir / "state.md"
    text = state.read_text(encoding="utf-8", errors="replace") if state.exists() else ""

    def section(name):
        m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text,
                      re.MULTILINE | re.DOTALL)
        return m.group(1).strip() if m else ""

    def used(body):
        # A section holding only its own help text or a "(none)" marker was
        # never used, however many bytes it occupies. The template mixes bold
        # labels with trailing italic hints and a colon —
        # "**Faction stances** *(only list ...)*:" — so stripping only whole
        # italic lines leaves that behind and reads it as content.
        out = []
        for ln in body.splitlines():
            t = ln.strip()
            if not t:
                continue
            t = re.sub(r"\*+\(?[^*]*?\)?\*+", "", t)      # bold/italic runs
            t = re.sub(r"\(none[^)]*\)", "", t)             # (none established)
            t = t.strip(" :*-—")
            if t:
                out.append(t)
        return bool(out)

    graph = cdir / "graph.json"
    graph_info = {"present": graph.exists()}
    if graph.exists():
        try:
            g = json.loads(graph.read_text(encoding="utf-8"))
            graph_info["nodes"] = len(g.get("nodes", []))
            graph_info["edges"] = len(g.get("edges", []))
        except Exception as e:
            graph_info["error"] = f"unreadable: {e}"

    # Strip the template's own italic help text before reading flags — it names
    # every flag it documents, so matching against it reports defaults as set.
    flags = re.sub(r"^\s*\*[^*].*\*\s*$", "", section("Session Flags"),
                   flags=re.MULTILINE)

    def flag(name):
        # Tolerates "- difficulty: hard", "difficulty: hard" and
        # "- **difficulty:** hard".
        m = re.search(rf"^\s*[-*]?\s*\**{name}\**:\**\s*(\w+)", flags, re.MULTILINE)
        return m.group(1) if m else None

    # Only these three are dials in the upstream sense — deliberate tuning of
    # DM defaults. The rest are session flags with their own defaults
    # (autosave is ON unless disabled; autorun and tutor_mode are
    # session-scoped), so reporting them as "never set" would be wrong.
    DIALS = ("difficulty", "spotlight", "pacing")
    OTHER_FLAGS = ("roll_mode", "autosave", "autorun", "tutor_mode")
    dials = {d: flag(d) for d in DIALS}
    other = {d: flag(d) for d in OTHER_FLAGS}

    arc_type = None
    m = re.search(r"^\s*type:\s*(\w+)", section("Campaign Arc"), re.MULTILINE)
    if m:
        arc_type = m.group(1)

    chars = sorted(p.stem for p in (cdir / "characters").glob("*.md")) \
        if (cdir / "characters").is_dir() else []

    return {
        "relationship_graph": graph_info,
        "pinned_facts_used": used(section("Pinned Facts")),
        "faction_moves_used": used(section("Faction Moves")),
        "live_state_flags_used": used(section("Live State Flags")),
        "continuity_archive_used": used(section("Continuity Archive")),
        "arc_type": arc_type,
        "arc_revisions": len(re.findall(r"^\s*-\s*(?:date|revised):", section("Campaign Arc"),
                                        re.MULTILINE)),
        "dials_set": {k: v for k, v in dials.items() if v},
        "dials_unset": [k for k, v in dials.items() if not v],
        "session_flags_set": {k: v for k, v in other.items() if v},
        "characters": chars,
        # Display usage is NOT detectable from disk: the runtime dir is created
        # by paths.py on every /dm:dnd load whether or not the companion ran.
        # Ask the player instead of inferring.
        "display_usage": "not detectable — ask the player",
    }


def findings(files, sections, features, cdir):
    """The known bloat and misconfiguration patterns, checked explicitly."""
    out = []
    by = {f["file"]: f for f in files}
    lp = load_path_total(files)

    if lp["per_session_est_tokens"] > 12000:
        out.append(f"Every session starts by reading ~{lp['per_session_est_tokens']} tokens "
                   "of campaign files. That is the recurring cost of this campaign, "
                   "paid before a word of play.")
    for f in files:
        # Character files are covered by the aggregate below; listing each one
        # separately just repeats the same finding once per party member.
        if (f["load_class"] == "full" and f["est_tokens"] > 4000
                and not f["file"].startswith("characters/")):
            out.append(f"{f['file']} is ~{f['est_tokens']} tokens and is read IN FULL at "
                       "every load.")
    chars = [f for f in files if f["file"].startswith("characters/")]
    ctot = sum(f["est_tokens"] for f in chars)
    if len(chars) >= 3 and ctot > 4000:
        out.append(f"{len(chars)} character files totalling ~{ctot} tokens are read in "
                   "full at every load — a party-size cost that grows with level.")

    if isinstance(sections, dict) and sections.get("sections"):
        for sec in sections["sections"]:
            if sec["flag"] == "high":
                out.append(f"state.md → ## {sec['section']} is ~{sec['est_tokens']} tokens. "
                           "Archive or compress it.")
    if isinstance(sections, dict) and not sections.get("dm_style_notes_present"):
        out.append("No '## DM Style Notes' section in state.md — the per-campaign "
                   "calibration mechanism was never used, so nothing the table "
                   "learned was carried between sessions automatically.")

    if not features["relationship_graph"]["present"]:
        out.append("No graph.json — the relationship graph was never initialized. "
                   "On a long campaign this is the main defence against continuity "
                   "loss under context compaction.")
    if not features["pinned_facts_used"]:
        out.append("No pinned facts. /dm:dnd pin is the cheapest continuity tool "
                   "in the skill and it went unused — and it is the direct fix for "
                   "the DM dropping a detail the player had flagged as mattering.")
    if not features["faction_moves_used"]:
        out.append("Faction Moves empty — the 'world moves without the player' "
                   "mechanism (Standard 11) left no trace.")
    if not features["live_state_flags_used"]:
        out.append("Live State Flags never maintained — the compaction-survival "
                   "mechanism was not used. Cross-check against reported "
                   "continuity failures.")
    if features["dials_unset"]:
        out.append("Dials never set: " + ", ".join(features["dials_unset"]) +
                   ". The DM ran on defaults for the whole campaign — not wrong, "
                   "but never a deliberate choice.")

    # session-log.md is SUPPOSED to be small: /dm:dnd save keeps only the two
    # most recent entries and appends the rest to the archive. Compare the pair.
    log = (by.get("session-log.md", {}).get("est_tokens", 0)
           + by.get("session-log-archive.md", {}).get("est_tokens", 0))
    state = by.get("state.md", {}).get("est_tokens", 0)
    if log and state > log:
        out.append("state.md is larger than the session log and archive combined — "
                   "history is accumulating in the load path instead of being "
                   "archived out of it.")
    if "session-log-archive.md" not in by and (
            by.get("session-log.md", {}).get("est_tokens", 0) > 6000):
        out.append("No session-log-archive.md, and session-log.md is large — "
                   "the archival step of /dm:dnd save may never have run.")

    world = by.get("world.md")
    if world and world["est_tokens"] < 300:
        out.append("world.md is nearly empty but is read IN FULL at every load. "
                   "If it holds template placeholders, every session begins by "
                   "reading them.")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", choices=["files", "sections", "features", "all"])
    ap.add_argument("campaign")
    a = ap.parse_args()

    cdir = campaign_dir(a.campaign)
    if not cdir.is_dir():
        sys.exit(f"no such campaign: {cdir}")

    if a.report == "files":
        out = files_report(cdir)
    elif a.report == "sections":
        out = sections_report(cdir)
    elif a.report == "features":
        out = features_report(cdir)
    else:
        f, s, ft = files_report(cdir), sections_report(cdir), features_report(cdir)
        out = {"files": f, "load_path": load_path_total(f), "state_sections": s,
               "features": ft, "findings": findings(f, s, ft, cdir)}
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
