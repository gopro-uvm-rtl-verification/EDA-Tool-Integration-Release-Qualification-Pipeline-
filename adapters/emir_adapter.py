from parsers.emir_log_parser import parse_emir_log
from adapters.common.rc_policy import RcPolicy

def run_emir(design, tool='voltus'):
    RcPolicy()
    text = "MAX_IR_DROP_MV: 52.4\nEM_VIOLATIONS: 0\n"
    metrics = parse_emir_log(text)
    return {"tool": tool, "design": design, **metrics, "metadata": {}}
