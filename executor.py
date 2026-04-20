from command_ir import CommandIR

import shutdown_restart_lock
import open_application
import close_application
import set_brightness
import set_volume
import check_internet
import check_disk
import mode_manager


# ─── Dispatch Table ───────────────────────────────────────────────────────────
# Maps every action string → its handler function.
# To add a new action: add the import above and one entry here.

dispatch = {
    # ── System ──────────────────────────────────────────────────────────────────
    "shutdown":             shutdown_restart_lock.shutdown,
    "restart":              shutdown_restart_lock.restart,
    "lock_screen":          shutdown_restart_lock.lock_screen,

    # ── Brightness ──────────────────────────────────────────────────────────────
    "increase_brightness":  set_brightness.increase_brightness,
    "decrease_brightness":  set_brightness.decrease_brightness,
    "set_brightness":       set_brightness.set_brightness,

    # ── Volume ──────────────────────────────────────────────────────────────────
    "increase_volume":      set_volume.increase_volume,
    "decrease_volume":      set_volume.decrease_volume,
    "set_volume":           set_volume.set_volume,
    "mute":                 set_volume.mute,

    # ── Applications ────────────────────────────────────────────────────────────
    "open_application":     open_application.open_application,
    "close_application":    close_application.close_application,

    # ── Diagnostics ─────────────────────────────────────────────────────────────
    "check_internet":       check_internet.check_internet,
    "check_disk":           check_disk.check_disk,

    # ── Modes ────────────────────────────────────────────────────────────────────
    "open_mode":            mode_manager.open_mode,
    "close_mode":           mode_manager.close_mode,
    "create_mode":          mode_manager.create_mode,
    "update_mode":          mode_manager.update_mode,
    "delete_mode":          mode_manager.delete_mode,
}


# ─── Entry Point ─────────────────────────────────────────────────────────────

def execution(command_ir: CommandIR):
    func = dispatch[command_ir.action]
    func(command_ir)
