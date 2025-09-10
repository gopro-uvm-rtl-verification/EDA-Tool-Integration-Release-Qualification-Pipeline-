from dataclasses import dataclass

@dataclass
class RcPolicy:
    ok: set = None
    retryable: set = None

    def __post_init__(self):
        if self.ok is None:
            self.ok = {0}
        if self.retryable is None:
            # 示例：137=OOM/kill；2=license not available
            self.retryable = {2, 137}

    def classify(self, rc: int) -> str:
        if rc in self.ok:
            return "ok"
        if rc in self.retryable:
            return "retry"
        return "fail"
