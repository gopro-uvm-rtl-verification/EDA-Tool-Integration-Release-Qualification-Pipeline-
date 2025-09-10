from .patterns import STA_VIOL_RE, WNS_RE, TNS_RE

def parse_sta_log(text: str):
    mviol = STA_VIOL_RE.search(text)
    mwns  = WNS_RE.search(text)
    mtns  = TNS_RE.search(text)
    return {
        "violations": int(mviol.group(1)) if mviol else 9999,
        "wns_ns": float(mwns.group(1)) if mwns else -999.0,
        "tns_ns": float(mtns.group(1)) if mtns else 9999.0,
    }
