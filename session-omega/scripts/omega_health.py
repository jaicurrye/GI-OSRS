"""
omega_health.py — measure what a long campaign did to the machinery.

The `tooling` stage asks whether the plugin served the table well. Most of that
question is answerable with numbers, and the numbers matter because the dnd
skill's design is explicitly token-budgeted: `state.md` is read at every
`/dm:dnd load`, so its size is a tax paid at the start of every session for the
life of the campaign. `session-log.md` is not on the load path — it can be large
without costing anything. Confusing the two leads to optimizing the wrong file.

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

# Files read at every /dm:dnd load. Size here is a per-session tax.
LOAD_PATH = {"state.md"}
# Read only on demand. Size here is cheap.
COLD = {"session-log.md", "world.md", "npcs.md", "arc.md"}

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
            "lines": len(p.read_text(errors="replace").splitlines()),
            "load_path": rel in LOAD_PATH,
        })
    return sorted(out, key=lambda r: -r["bytes"])


def sections_report(cdir):
    """Per-section size within state.md — where the per-session tax actually goes."""
    state = cdir / "state.md"
    if not state.exists():
        return {"error": f"no state.md at {state}"}
    text = state.read_text(errors="replace")
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
    text = state.read_text(errors="replace") if state.exists() else ""

    def section(name):
        m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text,
                      re.MULTILINE | re.DOTALL)
        return m.group(1).strip() if m else ""

    def used(body):
        # A section holding only its own italic help text or a "(none)" marker
        # was never used, however many bytes it occupies.
        stripped = re.sub(r"^\*.*\*$", "", body, flags=re.MULTILINE).strip()
        stripped = re.sub(r"\(none[^)]*\)", "", stripped).strip()
        return bool(stripped)

    graph = cdir / "graph.json"
    graph_info = {"present": graph.exists()}
    if graph.exists():
        try:
            g = json.loads(graph.read_text())
            graph_info["nodes"] = len(g.get("nodes", []))
            graph_info["edges"] = len(g.get("edges", []))
        except Exception as e:
            graph_info["error"] = f"unreadable: {e}"

    # Strip the template's own italic help text before reading dials — it names
    # every flag it documents, so matching against it reports defaults as set.
    flags = re.sub(r"^\*.*\*$", "", section("Session Flags"), flags=re.MULTILINE)
    dials = {}
    for d in ("difficulty", "spotlight", "pacing", "roll_mode",
              "autosave", "autorun", "tutor_mode"):
        m = re.search(rf"^\s*[-*]?\s*{d}:\s*(\w+)", flags, re.MULTILINE)
        dials[d] = m.group(1) if m else None

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
        "characters": chars,
        "display_runtime_present": (data_root() / ".runtime").is_dir(),
    }


def findings(files, sections, features, cdir):
    """The known bloat and misconfiguration patterns, checked explicitly."""
    out = []
    state = next((f for f in files if f["file"] == "state.md"), None)
    if state and state["est_tokens"] > 8000:
        out.append(f"state.md is ~{state['est_tokens']} tokens and is read at EVERY load — "
                   "this is the single largest recurring cost in the campaign.")
    if isinstance(sections, dict) and sections.get("sections"):
        for s in sections["sections"]:
            if s["flag"] == "high":
                out.append(f"state.md → ## {s['section']} is ~{s['est_tokens']} tokens. "
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
                   "in the skill and it went unused.")
    if not features["faction_moves_used"]:
        out.append("Faction Moves empty — the 'world moves without the player' "
                   "mechanism (Standard 11) left no trace.")
    if features["dials_unset"]:
        out.append("Dials never set: " + ", ".join(features["dials_unset"]) +
                   ". The DM ran on defaults for the whole campaign.")
    log = next((f for f in files if f["file"] == "session-log.md"), None)
    if log and state and log["est_tokens"] < state["est_tokens"]:
        out.append("session-log.md is smaller than state.md — history is probably "
                   "accumulating in the load path instead of being archived out of it.")
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
        out = {"files": f, "state_sections": s, "features": ft,
               "findings": findings(f, s, ft, cdir)}
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
