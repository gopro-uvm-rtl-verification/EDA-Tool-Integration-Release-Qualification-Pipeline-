import re

STA_VIOL_RE = re.compile(r"VIOLATIONS:\s*(\d+)", re.I)
WNS_RE      = re.compile(r"WNS:\s*([-+]?\d+\.\d+)", re.I)
TNS_RE      = re.compile(r"TNS:\s*([-+]?\d+\.\d+)", re.I)

DRC_ERR_RE    = re.compile(r"DRC\s+ERRORS:\s*(\d+)", re.I)
LVS_STATUS_RE = re.compile(r"LVS\s+STATUS:\s*(\w+)", re.I)
LVS_SHORTS_RE = re.compile(r"SHORTS:\s*(\d+)", re.I)
LVS_OPENS_RE  = re.compile(r"OPENS:\s*(\d+)", re.I)

IR_MAX_RE   = re.compile(r"MAX_IR_DROP_MV:\s*(\d+\.?\d*)", re.I)
EM_VIO_RE   = re.compile(r"EM_VIOLATIONS:\s*(\d+)", re.I)
