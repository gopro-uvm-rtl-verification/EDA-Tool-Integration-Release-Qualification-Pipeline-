from .patterns import IR_MAX_RE, EM_VIO_RE

def parse_emir_log(text: str):
    max_ir = float(IR_MAX_RE.search(text).group(1)) if IR_MAX_RE.search(text) else 999.0
    em_v   = int(EM_VIO_RE.search(text).group(1)) if EM_VIO_RE.search(text) else 9999
    return {"max_ir_drop_mv": max_ir, "em_violations": em_v}
