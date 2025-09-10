import json, yaml, os, uuid, datetime, pathlib
from adapters.sta_adapter import run_sta
from adapters.drc_adapter import run_drc
from adapters.lvs_adapter import run_lvs
from adapters.emir_adapter import run_emir
from jsonschema import validate
from orchestrator.promotion import can_promote

SCHEMA_DIR = pathlib.Path(__file__).resolve().parents[1] / "schemas"

def load_schema(name):
    return json.load(open(SCHEMA_DIR / name))

def run_all(matrix_path, out_dir):
    cfg = yaml.safe_load(open(matrix_path))
    os.makedirs(out_dir, exist_ok=True)
    artifacts = []
    for d in cfg['designs']:
        for mode in cfg['modes']:
            for corner in cfg['corners']:
                # STA
                sta = run_sta(d['name'], mode, corner['name'], tool=cfg['tools']['sta'])
                validate(sta, load_schema("sta_result.schema.json"))
                sta_file = f"{d['name']}_{mode}_{corner['name']}_sta.json".replace('/', '_')
                json.dump(sta, open(os.path.join(out_dir, sta_file), "w"), indent=2)
                # DRC/LVS
                drc = run_drc(d['name'], cfg['ruledecks']['drc'], tool=cfg['tools']['drc'])
                validate(drc, load_schema("drc_result.schema.json"))
                drc_file = f"{d['name']}_drc.json"
                json.dump(drc, open(os.path.join(out_dir, drc_file), "w"), indent=2)

                lvs = run_lvs(d['name'], cfg['ruledecks']['lvs'], tool=cfg['tools']['lvs'])
                validate(lvs, load_schema("lvs_result.schema.json"))
                lvs_file = f"{d['name']}_lvs.json"
                json.dump(lvs, open(os.path.join(out_dir, lvs_file), "w"), indent=2)

                emir = run_emir(d['name'], tool=cfg['tools']['emir'])
                validate(emir, load_schema("emir_result.schema.json"))
                emir_file = f"{d['name']}_emir.json"
                json.dump(emir, open(os.path.join(out_dir, emir_file), "w"), indent=2)

                artifacts += [sta_file, drc_file, lvs_file, emir_file]

    summary = {
        "run_id": str(uuid.uuid4()),
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "artifacts": sorted(set(artifacts)),
    }
    json.dump(summary, open(os.path.join(out_dir, "summary.json"), "w"), indent=2)
    return summary
