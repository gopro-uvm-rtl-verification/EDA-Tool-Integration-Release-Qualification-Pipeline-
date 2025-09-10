import os, argparse, shutil
from orchestrator.run_matrix import run_all
from reports.release_notes_gen import gen_release_notes

def main(matrix, out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out, exist_ok=True)
    s = run_all(matrix, out)
    gen_release_notes(out, os.path.join(out, "RELEASE_NOTES.md"), "LOCAL-TEST")
    print("Run complete:", s['run_id'])
    print("Artifacts in:", out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    main(a.matrix, a.out)
