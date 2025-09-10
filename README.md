# EDA Tool Integration & Release — Qualification Pipeline

Production-style reference for qualifying & releasing multi-vendor EDA tools:
- Adapters unify CLI/RC/logs
- Qualification matrix (modes/corners/design classes)
- JSON Schemas validate results
- Jenkins distributed regressions (shard/retry)
- Auto-diff results, promotion criteria, release notes & rollback points

## Quick start
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/dry_run.py --matrix matrix/qual_matrix.yaml --out out_local
