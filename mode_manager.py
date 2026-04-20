import json
import subprocess
from command_ir import CommandIR


MODES_FILE = "modes.json"

# processes that must never be force-killed inside a mode close
PROTECTED_PROCESSES = {"explorer", "taskmgr", "svchost", "winlogon", "csrss", "lsass"}


# ─── JSON Persistence ────────────────────────────────────────────────────────

def load_modes() -> dict:
    try:
        with open(MODES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_modes(modes: dict):
    with open(MODES_FILE, "w") as f:
        json.dump(modes, f, indent=4)


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _launch_item(item: str):
    """
    Launch a single item from a mode list.
    Works for both executable names and URLs — 'start' handles both.
    """
    subprocess.Popen(["start", "", item], shell=True)


def _close_item(item: str):
    """
    Close a single item from a mode list.
    URLs are skipped (no process to kill).
    Protected processes are skipped with a warning.
    """
    if item.startswith("http"):
        print(f"Skipping URL (cannot close by process): {item}")
        return

    item_lower = item.lower().replace(".exe", "")

    if item_lower in PROTECTED_PROCESSES:
        print(f"Skipping protected process: {item}")
        return

    subprocess.run(
        ["taskkill", "/f", "/im", f"{item}.exe"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )


# ─── Mode Operations ─────────────────────────────────────────────────────────

def open_mode(command_ir: CommandIR):
    modes     = load_modes()
    mode_name = command_ir.target

    if mode_name not in modes:
        print(f"Mode '{mode_name}' not found.")
        return

    for item in modes[mode_name]:
        try:
            _launch_item(item)
        except Exception as e:
            print(f"Could not open '{item}': {e}")


def close_mode(command_ir: CommandIR):
    modes     = load_modes()
    mode_name = command_ir.target

    if mode_name not in modes:
        print(f"Mode '{mode_name}' not found.")
        return

    for item in modes[mode_name]:
        _close_item(item)


def create_mode(command_ir: CommandIR):
    mode_name = command_ir.target
    app_list  = command_ir.parameters.get("app_list", [])

    if not mode_name:
        print("No mode name provided.")
        return

    modes = load_modes()
    modes[mode_name] = app_list
    save_modes(modes)
    print(f"Mode '{mode_name}' created with: {app_list}")


def update_mode(command_ir: CommandIR):
    """
    Adds new items to an existing mode without replacing the whole list.
    Items already present are skipped (no duplicates).
    """
    mode_name = command_ir.target
    new_items = command_ir.parameters.get("app_list", [])

    if not mode_name:
        print("No mode name provided.")
        return

    modes = load_modes()

    if mode_name not in modes:
        print(f"Mode '{mode_name}' does not exist. Use 'create mode' first.")
        return

    existing = modes[mode_name]
    added    = [item for item in new_items if item not in existing]
    existing.extend(added)

    modes[mode_name] = existing
    save_modes(modes)

    if added:
        print(f"Mode '{mode_name}' updated. Added: {added}")
    else:
        print(f"No new items added to '{mode_name}' (all already present).")


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
