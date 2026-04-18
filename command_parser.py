from command_ir import CommandIR    # class object to be returned

# verb resolution map: technical-defined word from many synonyms
#  verb -> tokens list structure
VERB_SYNONYMS = {
    "increase": ["increase", "raise", "boost", "brighten", "higher", "more", "enhance", "intensify", "amplify", "elevate", "heighten", "crank", "bump", "louder", "enlarge", "magnify", "expand", "grow"],
    "decrease": ["decrease", "lower", "reduce", "dim", "less", "soften", "minimize", "darken", "drop", "shrink", "tone", "weaken", "fade", "cut", "quieter"],
    "set":      ["set", "put", "make", "change", "adjust", "fix", "assign", "configure", "define", "update", "apply", "move", "go", "shift", "push"],
    "mute":     ["mute", "silence", "quiet", "hush", "suppress", "deafen", "drown", "block", "zero"],
    "open":     ["open", "launch", "start", "run", "execute", "load", "boot", "fire", "begin", "initiate", "activate", "bring", "pull", "access", "enter"],
    "close":    ["close", "quit", "exit", "kill", "stop", "terminate", "shut", "end", "finish", "destroy", "remove", "collapse", "dismiss", "leave", "abandon"],
    "check":    ["check", "test", "measure", "diagnose", "verify", "inspect", "monitor", "analyze", "scan", "ping", "evaluate"],
}

# generating flattened lookup dictionary from VERB_SYNONYMS (faster access)
# token -> verb
flattened_verb_dict = {} # verb resolution table
for key, synonyms_list in VERB_SYNONYMS.items():
    for synonym in synonyms_list:
        flattened_verb_dict[synonym] = key


# target resolution table: technological word for target from many synonyms
# target -> synonyms list
TARGET_SYNONYMS = {
    "brightness": ["brightness", "bright", "screen", "display", "backlight", "luminance", "glow"],
    "volume":     ["volume", "sound", "audio", "noise", "speaker", "music"],
    "internet":   ["internet", "wifi", "network", "connection", "connectivity", "speed", "bandwidth", "web", "signal", "net"],
    "disk":       ["disk", "storage", "drive", "space", "memory", "hard drive", "harddrive", "ssd", "hdd", "c drive"],
}

# flattened dict: synonym -> target
flattened_target_dict = {}
for key, synonyms_list in TARGET_SYNONYMS.items():
    for synonym in synonyms_list:
        flattened_target_dict[synonym] = key

# verbs requiring no target. already complete
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

    "mute":      "mute",
    "silence":   "mute",
    "quiet":     "mute",
    "hush":      "mute",
    "suppress":  "mute",
    "deafen":    "mute",
    "drown":     "mute",
    "block":     "mute",
    "zero":      "mute",
}

# special action dict 
SPECIAL_ACTIONS = {
    "open": "open_application",
    "close": "close_application"
}

##########################################################################################



def command_parser(tokens: list) -> CommandIR:
    command_ir = CommandIR()    # resulting intermediate representation

    # flags for finding various parameters in the input command given
    action_found = False        # technical action word (verb + target) found!
    target_found = False        # target to be acted on found!
    verb_found = False          # verb part of the action found

    verb, target = None, None       # currently, none
    
    for i, token in enumerate(tokens):

        # for verb requiring no target
        if token in STANDALONE_ACTIONS:
            command_ir.action = STANDALONE_ACTIONS[token]
            # everything found!
            action_found = True
            verb_found = True
            target_found = True
            break   # no loop needed through rest of the token list



        # for verbs requiring a target
        else:

            # finding the verb
            if token in flattened_verb_dict:
                verb = flattened_verb_dict[token]
                verb_found = True

                # special action: a command needing a different action creation then 'verb + target'
                # hence won't go through target-based creation
                # case inside verb finding because synonyms may exist for these too
                if verb in SPECIAL_ACTIONS:
                    command_ir.action = SPECIAL_ACTIONS[verb]   # action found based on verb
                    action_found = True

                    # finding target for special action
                    if (i+1) < len(tokens):     # for no out-of-bound condition
                        # all the words after the special command are target
                        # hence: target could be multi-words based
                        target = " ".join(tokens[i+1:])
                        target_found = True
                    
                    # no target defined for special action
                    else:
                        command_ir.errors.append("No target application provided!")
                        return command_ir   # no checking needed further ahead as partial command provided

        # checking for token
        if token in flattened_target_dict and not target_found:
            # not target_found: to stop over-writing special command's target
            target = flattened_target_dict[token]
            target_found = True

        # breaking if both word and command found 
        if verb_found and target_found:
            break
    
    # error checking
    if not verb_found:
        command_ir.errors.append("No action found!")
        return command_ir
    
    if not target_found:
        command_ir.errors.append("No target found!")
        return command_ir

    # action & target creation (for non-standalone & non-special actions)
    if not action_found:
        command_ir.action = verb + "_" + target
    if target_found:
        command_ir.target = target
    
    # finding parameters, if any
    for i, token in enumerate(tokens):
        if isinstance(token, int): # only for integers
            command_ir.parameters["level"] = token

            # checking for 'minus' in words for numeric values found!
            if i > 0 and tokens[i-1] == "minus":
                command_ir.parameters["level"] = 0 - token

    return command_ir