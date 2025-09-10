from parsers.drc_log_parser import parse_drc_log
from adapters.common.rc_policy import RcPolicy

def run_drc(design, ruledeck, tool='calibre'):
    RcPolicy()
    text = "DRC ERRORS: 0\n"  # 真实场景换成 Calibre/Pegasus 日志
    metrics = parse_drc_log(text)
    return {"tool": tool, "design": design, "ruledeck": ruledeck, **metrics, "metadata": {}}
