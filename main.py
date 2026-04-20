import threading
import json

from input_processor import input_processor
from command_parser import command_parser
from validator import validator
from executor import execution

import shortcut_listener
import voice_listener
import reminder_manager


# ─── LOAD USER SHORTCUTS ───

def load_shortcuts():
    try:
        with open("shortcuts.json", "r") as f:
            return json.load(f)
    except:
        return {}


# ─── COMMAND HANDLER ───

def handle_command(command: str):
    tokens = input_processor(command)
    if not tokens:
        return

    ir = validator(command_parser(tokens))

    if ir.errors:
        print(ir.errors)
        return

    execution(ir)


# ─── START THREADS ───

def start_background_services():

    # Keyboard shortcuts
    shortcuts = load_shortcuts()
    t1 = threading.Thread(target=shortcut_listener.run_shortcuts, args=(shortcuts,), daemon=True)

    # Voice
    t2 = threading.Thread(target=voice_listener.run_voice, daemon=True)

    # Reminders
    t3 = threading.Thread(target=reminder_manager.run_reminders, daemon=True)

    t1.start()
    t2.start()
    t3.start()


# ─── MAIN LOOP ───

def main():
    start_background_services()

    print("Isha Assistant Running...\n")

    while True:
        command = input(">>> ")
        handle_command(command)


if __name__ == "__main__":
    main()