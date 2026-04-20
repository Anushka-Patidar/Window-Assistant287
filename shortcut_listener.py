import keyboard

from input_processor import input_processor
from command_parser import command_parser
from validator import validator
from executor import execution


def handle_command(command: str):
    tokens = input_processor(command)
    if not tokens:
        return

    ir = validator(command_parser(tokens))
    if not ir.errors:
        execution(ir)


def run_shortcuts(shortcuts: dict):
    for combo, command in shortcuts.items():
        keyboard.add_hotkey(combo, lambda cmd=command: handle_command(cmd))

    print("Keyboard shortcuts active...")
    keyboard.wait()