import json
import subprocess
from command_ir import CommandIR

MODES_FILE = "modes.json"

PROTECTED_PROCESSES = {"explorer", "taskmgr", "svchost", "winlogon", "csrss", "lsass"}


# ─── JSON Read/Write ────────────────────────────────────────────────────────────

def load_modes():
    try:
        with open(MODES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_modes(modes):
    with open(MODES_FILE, "w") as f:
        json.dump(modes, f, indent=4)


# ─── Executor Functions ─────────────────────────────────────────────────────────

def open_mode(command_ir: CommandIR):
    modes = load_modes()
    mode_name = command_ir.target

    if mode_name not in modes:
        print(f"Mode '{mode_name}' not found.")
        return

    app_list = modes[mode_name]
    for app in app_list:
        try:
            subprocess.Popen(["start", app], shell=True)
        except FileNotFoundError:
            print(f"Could not open: {app}")


def close_mode(command_ir: CommandIR):
    modes = load_modes()
    mode_name = command_ir.target

    if mode_name not in modes:
        print(f"Mode '{mode_name}' not found.")
        return

    app_list = modes[mode_name]
    for app in app_list:
        if app in PROTECTED_PROCESSES:
            print(f"Skipping protected process: {app}\nMay kill necessary processes.")
            continue
        subprocess.run(["taskkill", "/f", "/im", f"{app}.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def create_mode(command_ir: CommandIR):
    mode_name = command_ir.target
    app_list = command_ir.parameters.get("app_list", [])

    if not mode_name:
        print("No mode name provided.")
        return

    modes = load_modes()
    modes[mode_name] = app_list
    save_modes(modes)


def delete_mode(command_ir: CommandIR):
    mode_name = command_ir.target

    if not mode_name:
        print("No mode name provided.")
        return

    modes = load_modes()
    if mode_name not in modes:
        print(f"Mode '{mode_name}' does not exist.")
        return

    del modes[mode_name]
    save_modes(modes)
    print(f"Mode '{mode_name}' deleted.")