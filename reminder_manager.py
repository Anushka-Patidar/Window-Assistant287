import json
import time
from datetime import datetime

from command_ir import CommandIR
from input_processor import input_processor
from command_parser import command_parser
from validator import validator

FILE = "reminders.json"


# ─── LOAD / SAVE ───

def load():
    try:
        return json.load(open(FILE))
    except:
        return []


def save(data):
    json.dump(data, open(FILE, "w"), indent=4)


# ─── CREATE REMINDER ───

def create_reminder(ir: CommandIR):
    text = ir.target.lower()

    if "at" not in text:
        print("❌ Please specify time using 'at HH:MM'")
        return

    parts = text.split("at")

    command_text = parts[0].replace("me to", "").strip()
    time_text = parts[1].strip()

    reminders = load()

    reminders.append({
        "command": command_text,
        "time": time_text,
        "done": False
    })

    save(reminders)

    print(f"✅ Reminder set → {command_text} at {time_text}")


# ─── RUN LOOP ───

def run_reminders():
    print("Reminder system running...")

    from executor import execution

    while True:
        reminders = load()
        now = datetime.now().strftime("%H:%M")

        for r in reminders:
            if r["time"] == now and not r["done"]:
                print(f"⏰ Executing: {r['command']}")

                tokens = input_processor(r["command"])
                ir = validator(command_parser(tokens))

                if not ir.errors:
                    execution(ir)

                r["done"] = True

        save(reminders)
        time.sleep(60)