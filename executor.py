from command_ir import CommandIR

# importing action function files
import shutdown_restart_lock 
import open_application
import close_application
import set_brightness
import set_volume
import check_internet
import check_disk


# maps action -> action's functions
dispatch = {
    "shutdown":             shutdown_restart_lock.shutdown,
    "restart":              shutdown_restart_lock.restart,
    "lock_screen":          shutdown_restart_lock.lock_screen,

    "increase_brightness":  set_brightness.increase_brightness,
    "decrease_brightness":  set_brightness.decrease_brightness,
    "set_brightness":       set_brightness.set_brightness,

    "increase_volume":      set_volume.increase_volume,
    "decrease_volume":      set_volume.decrease_volume,
    "set_volume":           set_volume.set_volume,
    "mute":                 set_volume.mute,

    "open_application":     open_application.open_application,
    "close_application":    close_application.close_application,

    "check_internet":       check_internet.check_internet,
    "check_disk":     check_disk.check_disk,
    # "reminder":             reminder,
    # "create_video_call":    create_video_call,
    # "group_open":           group_open,
}

def execution(command_ir: CommandIR):
    func = dispatch[command_ir.action]
    func(command_ir)