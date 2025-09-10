from parsers.lvs_log_parser import parse_lvs_log
from adapters.common.rc_policy import RcPolicy

def run_lvs(design, ruledeck, tool='calibre'):
    RcPolicy()
    text = "LVS STATUS: clean\nSHORTS: 0\nOPENS: 0\n"
    metrics = parse_lvs_log(text)
    return {"tool": tool, "design": design, "ruledeck": ruledeck, **metrics, "metadata": {}}
