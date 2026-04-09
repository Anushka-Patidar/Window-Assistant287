from command_ir import CommandIR    # class object to be returned

# verb resolution map
VERB_SYNONYMS = {
    "increase": ["increase", "raise", "boost", "brighten", "higher", "more", "enhance", "intensify", "amplify", "elevate", "heighten", "crank", "bump", "louder", "enlarge", "magnify", "expand", "grow"],
    "decrease": ["decrease", "lower", "reduce", "dim", "less", "soften", "minimize", "darken", "drop", "shrink", "tone", "weaken", "fade", "cut", "quieter"],
    "set":      ["set", "put", "make", "change", "adjust", "fix", "assign", "configure", "define", "update", "apply", "move", "go", "shift", "push"],
    "mute":     ["mute", "silence", "quiet", "hush", "suppress", "deafen", "drown", "block", "zero"],
    "open":     ["open", "launch", "start", "run", "execute", "load", "boot", "fire", "begin", "initiate", "activate", "bring", "pull", "access", "enter"],
    "close":    ["close", "quit", "exit", "kill", "stop", "terminate", "shut", "end", "finish", "destroy", "remove", "collapse", "dismiss", "leave", "abandon"]
}

# generating flattened lookup dictionary from VERB_SYNONYMS (faster access)
# token -> verb
flattened_verb_dict = {} # verb resolution table
for key, synonyms_list in VERB_SYNONYMS.items():
    for synonym in synonyms_list:
        flattened_verb_dict[synonym] = key

# target resolution table
TARGET_SYNONYMS = {
    "brightness": ["brightness", "bright", "screen", "display", "backlight", "luminance", "glow"],
    "volume":     ["volume", "sound", "audio", "noise", "speaker", "music"],
    "zoom":       ["zoom", "scale", "magnification", "size"],
}

# flattened disk: synonym -> target
flattened_target_dict = {}
for key, synonyms_list in TARGET_SYNONYMS.items():
    for synonym in synonyms_list:
        flattened_target_dict[synonym] = key

# no target required verbs
STANDALONE_ACTIONS = {
    "shutdown":  "shutdown",
    "off":       "shutdown",
    "poweroff":  "shutdown",
    "halt":      "shutdown",
    "power":     "shutdown",
    "restart":   "restart",
    "reboot":    "restart",
    "reset":     "restart",
    "reload":    "restart",
    "refresh":   "restart",
    "cycle":     "restart",
    "renew":     "restart",
    "reinitialize": "restart",
    "restore":   "restart",
    "bounce":    "restart",
    "redo":      "restart",
    "flip":      "restart",
    "lock":      "lock_screen",
    "secure":    "lock_screen",
    "protect":   "lock_screen",
    "sleep":     "lock_screen",
    "guard":     "lock_screen",
    "freeze":    "lock_screen",
    "seal":      "lock_screen",
    "hide":      "lock_screen",
    "suspend":   "lock_screen",
    "idle":      "lock_screen",
    "pause":     "lock_screen",
    "engage":    "lock_screen",
    "arm":       "lock_screen",
}

# special action updation
SPECIAL_ACTIONS = {
    "open": "open_application",
    "close": "close_application"
}


def command_parser(tokens: list) -> CommandIR:
    command_ir = CommandIR()    # resulting intermediate representation

    action_found = False  # flag
    target_found = False
    verb_found = False

    verb, target = None, None

    for i, token in enumerate(tokens): 
        if token in STANDALONE_ACTIONS:
            command_ir.action = STANDALONE_ACTIONS[token]
            action_found = True
            verb_found = True
            target_found = True
            break
        else:
            if token in flattened_verb_dict:
                verb = flattened_verb_dict[token]
                verb_found = True

                # open action command
                if verb == 'open' or verb == 'close':
                    if (i+1) < len(tokens):
                        target = " ".join(tokens[i+1:])
                        target_found = True
                    else:
                        command_ir.action = verb + "_application"
                        command_ir.errors.append("No target application provided!")
                        return command_ir
                    continue

            if token in flattened_target_dict:
                target = flattened_target_dict[token]
                target_found = True
            
            if verb_found and target_found:
                break
    
    # error checking
    if not verb_found:
        command_ir.errors.append("No action found!")
        return command_ir
    
    if not target_found:
        command_ir.errors.append("No target found!")
        return command_ir

    # action & target creation (for non-standalone actions)
    if not action_found:
        if verb in SPECIAL_ACTIONS:
            command_ir.action = SPECIAL_ACTIONS[verb]
        else:
            command_ir.action = verb + "_" + target
        command_ir.target = target
    
    # finding parameters, if any
    for i, token in enumerate(tokens):
        if isinstance(token, int): # only for integers
            command_ir.parameters["level"] = token

            # checking for 'minus' in words
            if i > 0 and tokens[i-1] == "minus":
                command_ir.parameters["level"] = 0 - token

    return command_ir