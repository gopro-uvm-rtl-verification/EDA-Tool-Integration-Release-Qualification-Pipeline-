import tempfile, os
from adapters.common.rc_policy import RcPolicy
from parsers.sta_log_parser import parse_sta_log

def run_sta(design, mode, corner, tool='primetime'):
    rc_policy = RcPolicy()
    with tempfile.TemporaryDirectory() as td:
        log = os.path.join(td, "sta.log")
        sample = "WNS: 0.12\nTNS: 0.00\nVIOLATIONS: 0\n"  # 真实场景这里是工具原生日志
        open(log, "w").write(sample)
        rc = 0
        status = rc_policy.classify(rc)
        if status == "retry":
            raise RuntimeError("retryable RC")
        if status == "fail":
            raise RuntimeError("tool failed")
        metrics = parse_sta_log(open(log).read())
        return {
            "tool": tool, "design": design, "mode": mode, "corner": corner,
            **metrics, "metadata": {"log_path": log}
        }
