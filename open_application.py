import psutil
import subprocess
import time
from command_ir import CommandIR


def open_application(ir: CommandIR):
    target      = ir.target
    fallback_url = ir.parameters.get("fallback_url")
    force_web   = ir.parameters.get("force_web", False)

    # ── Case 1: User explicitly asked for browser/web ────────────────────────
    if force_web:
        if fallback_url:
            subprocess.Popen(["start", "", fallback_url], shell=True)
        else:
            subprocess.Popen(["start", "", target], shell=True)
        return

    # ── Case 2: Target is already a resolved URL ─────────────────────────────
    if target.startswith("http"):
        subprocess.Popen(["start", "", target], shell=True)
        return

    # ── Case 3: App launch with no URL fallback ──────────────────────────────
    if fallback_url is None:
        subprocess.Popen(
            ["start", "", target],
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return

    # ── Case 4: App launch with URL fallback ─────────────────────────────────
    subprocess.Popen(["start", "", target], shell=True)

    # wait, then check whether the process actually appeared
    time.sleep(2)

    installed_application_ran = False
    target_lower = target.lower().replace(".exe", "")

    for process in psutil.process_iter(['name']):
        process_name = process.info['name'].lower().replace(".exe", "")
        if target_lower in process_name or process_name in target_lower:
            installed_application_ran = True
            break

    if not installed_application_ran:
        print(f"App '{target}' not found running. Opening in browser...")
        subprocess.Popen(["start", "", fallback_url], shell=True)
