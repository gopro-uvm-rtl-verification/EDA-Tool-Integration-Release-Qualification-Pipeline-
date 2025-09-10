import os, time, shutil

def gc(path, keep_days=14):
    now = time.time()
    for name in os.listdir(path):
        p = os.path.join(path, name)
        if os.path.isdir(p):
            age_days = (now - os.stat(p).st_mtime)/86400.0
            if age_days > keep_days:
                shutil.rmtree(p, ignore_errors=True)
