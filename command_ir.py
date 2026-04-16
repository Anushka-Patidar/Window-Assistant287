from dataclasses import dataclass, field
from typing import Optional

@dataclass      # for no manual __init__ or __eq__ methods!
class CommandIR:
    action: Optional[str] = None        # value = either string or None
    target: Optional[str] = None        # value = either string or None
    parameters: dict = field(default_factory=dict)      # for a new dict for each command
    
    # ignorable but inform the user
    warnings: list = field(default_factory=list)    # new list for each command

    # fatal issues! inform and stop the program
    errors: list = field(default_factory=list)  # new list for each command