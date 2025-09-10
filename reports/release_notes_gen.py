import json, os, datetime

def gen_release_notes(out_dir, notes_path, version_tag):
    summary = json.load(open(os.path.join(out_dir, "summary.json")))
    lines = []
    lines.append(f"# Release Notes — {version_tag}")
    lines.append("")
    lines.append(f"- Timestamp (UTC): {datetime.datetime.utcnow().isoformat()}Z")
    lines.append(f"- Run ID: {summary['run_id']}")
    lines.append("")
    lines.append("## Artifacts")
    for a in summary['artifacts']:
        lines.append(f"- {a}")
    open(notes_path, "w").write("\n".join(lines))
    return notes_path
