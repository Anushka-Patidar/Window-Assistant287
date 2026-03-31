# action synonyms map (action -> token) 
ACTION_SYNONYMS = {
    "increase_brightness": ["increase", "raise", "boost", "brighten", "up", "higher", "more", "enhance", "intensify", "amplify", "maximize", "elevate", "heighten", "crank", "bump"],
    "decrease_brightness": ["decrease", "lower", "reduce", "dim", "down", "less", "soften", "minimize", "darken", "drop", "shrink", "tone", "weaken", "fade", "cut"],
    "set_brightness":      ["set", "put", "make", "change", "adjust", "fix", "assign", "configure", "define", "update", "apply", "move", "go", "shift", "push"],

    "increase_volume":     ["increase", "raise", "boost", "louder", "up", "higher", "more", "amplify", "maximize", "elevate", "crank", "bump", "turn", "enhance", "intensify"],
    "decrease_volume":     ["decrease", "lower", "reduce", "quieter", "down", "less", "soften", "minimize", "drop", "shrink", "tone", "weaken", "fade", "cut", "mute"],
    "set_volume":          ["set", "put", "make", "change", "adjust", "fix", "assign", "configure", "define", "update", "apply", "move", "go", "shift", "push"],
    "mute_volume":         ["mute", "silence", "quiet", "hush", "kill", "suppress", "deafen", "stop", "disable", "shut", "drown", "block", "cut", "off", "zero"],

    "open_application":    ["open", "launch", "start", "run", "execute", "load", "boot", "fire", "begin", "initiate", "activate", "bring", "pull", "access", "enter"],
    "close_application":   ["close", "quit", "exit", "kill", "stop", "terminate", "shut", "end", "finish", "destroy", "remove", "collapse", "dismiss", "leave", "abandon"],

    "increase_zoom":       ["zoom", "increase", "raise", "boost", "enlarge", "up", "higher", "more", "magnify", "maximize", "scale", "expand", "grow", "amplify", "in"],
    "decrease_zoom":       ["unzoom", "decrease", "lower", "reduce", "shrink", "down", "less", "minimize", "scale", "contract", "compress", "out", "drop", "fade", "back"],

    "lock_screen":         ["lock", "secure", "protect", "sleep", "block", "guard", "freeze", "seal", "hide", "suspend", "idle", "pause", "screen", "engage", "arm"],
    "shutdown":            ["shutdown", "off", "poweroff", "halt", "stop", "kill", "terminate", "end", "close", "finish", "cut", "down", "power", "switch", "turn"],
    "restart":             ["restart", "reboot", "reset", "reload", "refresh", "cycle", "renew", "reinitialize", "restore", "bounce", "redo", "start", "boot", "flip", "turn"],
}

# generating flattened lookup dictionary from ACTION_SYNONYMS
# token -> action
flattened_dict = {} # verb resolution table
for key, synonyms_list in ACTION_SYNONYMS.items():
    for synonym in synonyms_list:
        flattened_dict[synonym] = key

# target positional/lookup dictionary
ACTION_TARGET_MODE = {
    "increase_brightness": "lookup",
    "decrease_brightness": "lookup",
    "set_brightness":      "lookup",
    "increase_volume":     "lookup",
    "decrease_volume":     "lookup",
    "set_volume":          "lookup",
    "mute_volume":         "lookup",
    "open_application":    "positional",
    "close_application":   "positional",
    "increase_zoom":       "lookup",
    "decrease_zoom":       "lookup",
    "lock_screen":         "none",
    "shutdown":            "none",
    "restart":             "none",
}

def command_parser(tokens: list):
    for i, token in enumerate(tokens):
        if token in flattened_dict:
            action = flattened_dict[token]
            break
    
    KNOWN_TARGETS = ["brightness", "volume", "zoom"]
    if ACTION_TARGET_MODE[action] == "lookup":
        for token in tokens:
            if token in KNOWN_TARGETS:
                target = token
    elif ACTION_TARGET_MODE[action] == "positional":
        target = tokens[i+1]
