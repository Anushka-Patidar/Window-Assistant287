from command_ir import CommandIR
# importing action function files
import shutdown_restart_lock 


# maps action -> action's functions and the necessary list of parameters
# both available in CommandIR object
dispatch = {
    "shutdown":             (shutdown_restart_lock.shutdown,              []),
    "restart":              (shutdown_restart_lock.restart,               []),
    "lock_screen":          (shutdown_restart_lock.lock_screen,            []),

    # "increase_brightness":  (increase_brightness,   ["level"]),
    # "decrease_brightness":  (decrease_brightness,   ["level"]),
    # "set_brightness":       (set_brightness,        ["level"]),

    # "increase_volume":      (increase_volume,       ["level"]),
    # "decrease_volume":      (decrease_volume,       ["level"]),
    # "set_volume":           (set_volume,            ["level"]),
    # "mute":                 (mute,                  []),

    # "increase_zoom":        (increase_zoom,         []),
    # "decrease_zoom":        (decrease_zoom,         []),
    # "set_zoom":             (set_zoom,              []),

    # "open_application":     (open_application,      ["target", "url"]),
    # "close_application":    (close_application,     ["target"]),

    # "check_internet":       (check_internet,        []),
    # "check_disk_space":     (check_disk_space,      []),
    # "reminder":             (reminder,              ["time", "message"]),
    # "create_video_call":    (create_video_call,     ["platform"]),
    # "group_open":           (group_open,            ["mode"]),
}

def execution(command_ir: CommandIR):
    func, params = dispatch[command_ir.action]
    args = [command_ir.parameters[p] for p in params]
    func(*args)