from .patterns import LVS_STATUS_RE, LVS_SHORTS_RE, LVS_OPENS_RE

def parse_lvs_log(text: str):
    status = (LVS_STATUS_RE.search(text).group(1).lower()
              if LVS_STATUS_RE.search(text) else "error")
    shorts = int(LVS_SHORTS_RE.search(text).group(1)) if LVS_SHORTS_RE.search(text) else 0
    opens  = int(LVS_OPENS_RE.search(text).group(1)) if LVS_OPENS_RE.search(text) else 0
    return {"status": status, "shorts": shorts, "opens": opens}
