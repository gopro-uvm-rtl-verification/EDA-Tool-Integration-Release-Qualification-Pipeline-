from .patterns import DRC_ERR_RE

def parse_drc_log(text: str):
    m = DRC_ERR_RE.search(text)
    return {"errors": int(m.group(1)) if m else 9999, "waived": 0}
