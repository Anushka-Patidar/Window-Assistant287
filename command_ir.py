from dataclasses import dataclass, field
from typing import Optional


@dataclass      # eliminates need for manual __init__ or __eq__
class CommandIR:
    action:     Optional[str] = None                        # what to do -> will be 'str' or None
    target:     Optional[str] = None                        # what entity to act on
    parameters: dict          = field(default_factory=dict) # extra data needed for execution -> field creates new dict each time

    warnings:   list          = field(default_factory=list) # non-fatal — inform but continue
    errors:     list          = field(default_factory=list) # fatal     — inform and stop
