import psutil
import subprocess
from command_ir import CommandIR


# ─── Process Name Aliases ─────────────────────────────────────────────────────
# Maps launch/executable name → actual running process name, for cases where
# the two differ. Most apps don't need an entry here (process name == exe name).
# None means "this is a URI scheme — no process can be killed".

PROCESS_NAME_ALIASES = {
    # ── Windows built-ins ────────────────────────────────────────────────────────
    "calc":             "calculatorapp",    # UWP Calculator in Win10/11
    "stikynot":         "stikynot",
    "ms-settings:":     None,               # URI scheme — cannot kill by process
    "windowsdefender:": None,               # URI scheme — cannot kill by process
    "devmgmt.msc":      "mmc",              # all .msc snap-ins run as mmc.exe
    "diskmgmt.msc":     "mmc",
    "eventvwr.msc":     "mmc",

    # ── Windows Terminal ─────────────────────────────────────────────────────────
    "wt":               "windowsterminal",

    # ── Adobe ────────────────────────────────────────────────────────────────────
    "premiere":         "adobe premiere pro",   # process name differs from exe

    # ── GOG Galaxy ───────────────────────────────────────────────────────────────
    "gogalaxy":         "galaxyclient",

    # ── Git Bash ─────────────────────────────────────────────────────────────────
    "git-bash":         "bash",

    # ── Tor Browser ──────────────────────────────────────────────────────────────
    "tor browser":      "firefox",              # Tor is built on Firefox
}

# processes that must never be killed — doing so crashes Windows or the session
PROTECTED_PROCESSES = {"winlogon", "csrss", "lsass", "svchost", "wininit", "services"}

# explorer needs a graceful close (no /f) — Windows auto-restarts the shell
GRACEFUL_ONLY = {"explorer"}


# ─── Main Function ────────────────────────────────────────────────────────────

def close_application(ir: CommandIR):
    target = ir.target.lower().replace(".exe", "")

    # ── URI-based targets have no process to kill ─────────────────────────────
    if target in PROCESS_NAME_ALIASES and PROCESS_NAME_ALIASES[target] is None:
        print(f"'{target}' is a system URI and cannot be closed this way.")
        return

    # ── Resolve alias if process name differs from launch name ───────────────
    resolved = PROCESS_NAME_ALIASES.get(target, target)

    # ── Protected: refuse entirely ───────────────────────────────────────────
    if resolved in PROTECTED_PROCESSES:
        print(f"'{target}' is a protected system process. Refusing to close.")
        return

    # ── Explorer: graceful close (Windows restarts the shell automatically) ──
    if resolved in GRACEFUL_ONLY:
        result = subprocess.run(
            ["taskkill", "/im", "explorer.exe"],    # NO /f flag — graceful
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            print("File Explorer closed. Windows will restart the shell automatically.")
        else:
            print("Could not close File Explorer.")
        return

    # ── Normal termination via psutil ─────────────────────────────────────────
    # ── Normal termination via psutil ─────────────────────────────────────────
    found_and_closed = False

    for process in psutil.process_iter(['name']):
        # DEBUG: print(f"process info: {process.info()}")
        process_name = process.info['name'].lower().replace(".exe", "")
        if (resolved in process_name or process_name in resolved) and process_name != "":
            try:
                process.terminate()
                found_and_closed = True
            except psutil.AccessDenied:
                # psutil was denied — fall back to taskkill
                exe_name = process_name + ".exe"
                result = subprocess.run(
                    ["taskkill", "/F", "/IM", exe_name],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                if result.returncode == 0:
                    found_and_closed = True
                    break           # since no remaining processes running to check on!
                else:
                    print(f"Access denied and taskkill also failed for '{exe_name}'.")
            except psutil.NoSuchProcess:
                pass  # process died between iteration and terminate — harmless

    if not found_and_closed:
        print(f"Warning: No running process found matching '{target}'.")
