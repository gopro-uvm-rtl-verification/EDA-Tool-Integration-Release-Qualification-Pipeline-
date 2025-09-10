import json, os
from tabulate import tabulate

def diff_two_runs(dir_old, dir_new):
    def load_sum(d): return json.load(open(os.path.join(d, "summary.json")))
    s_old = load_sum(dir_old); s_new = load_sum(dir_new)
    rows = []
    for art in sorted(set(s_old['artifacts']) | set(s_new['artifacts'])):
        oldp, newp = os.path.join(dir_old, art), os.path.join(dir_new, art)
        old = json.load(open(oldp)) if os.path.exists(oldp) else {}
        new = json.load(open(newp)) if os.path.exists(newp) else {}
        rows.append([art,
                     old.get('violations') or old.get('errors') or old.get('status') or old.get('max_ir_drop_mv'),
                     new.get('violations') or new.get('errors') or new.get('status') or new.get('max_ir_drop_mv')])
    print(tabulate(rows, headers=["artifact", "old", "new"], tablefmt="github"))
