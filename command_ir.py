from dataclasses import dataclass, field
from typing import Optional

@dataclass
class CommandIR:
    action: Optional[str] = None
    target: Optional[str] = None
    parameters: dict = field(default_factory=dict)
    warnings: list = field(default_factory=list)
    errors: list = field(default_factory=list)