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
    "create":   ["create", "make", "add", "new", "save", "build", "setup", "define", "register", "store"],
    "delete":   ["delete", "remove", "destroy", "erase", "clear", "wipe", "drop", "unregister"],
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
    "close": "close_application",
    "create": "create_mode",
    "delete": "delete_mode",
}

APP_ALIASES = {
    # browsers
    "chrome":                       "chrome",
    "google chrome":                "chrome",
    "firefox":                      "firefox",
    "mozilla firefox":              "firefox",
    "edge":                         "msedge",
    "microsoft edge":               "msedge",
    "opera":                        "opera",
    "brave":                        "brave",
    "brave browser":                "brave",
    "vivaldi":                      "vivaldi",
    "tor":                          "tor browser",
    "tor browser":                  "tor browser",

    # code editors & IDEs
    "vs code":                      "code",
    "vscode":                       "code",
    "visual studio code":           "code",
    "visual studio":                "devenv",
    "pycharm":                      "pycharm",
    "intellij":                     "idea",
    "intellij idea":                "idea",
    "webstorm":                     "webstorm",
    "android studio":               "studio64",
    "sublime":                      "sublime_text",
    "sublime text":                 "sublime_text",
    "atom":                         "atom",
    "notepad":                      "notepad",
    "notepad++":                    "notepad++",
    "vim":                          "vim",
    "neovim":                       "nvim",

    # terminals & shells
    "terminal":                     "wt",
    "windows terminal":             "wt",
    "cmd":                          "cmd",
    "command prompt":               "cmd",
    "powershell":                   "powershell",
    "git bash":                     "git-bash",
    "wsl":                          "wsl",

    # communication
    "discord":                      "discord",
    "slack":                        "slack",
    "teams":                        "teams",
    "microsoft teams":              "teams",
    "zoom":                         "zoom",
    "skype":                        "skype",
    "telegram":                     "telegram",
    "whatsapp":                     "whatsapp",
    "signal":                       "signal",

    # productivity & office
    "notion":                       "notion",
    "obsidian":                     "obsidian",
    "word":                         "winword",
    "microsoft word":               "winword",
    "excel":                        "excel",
    "microsoft excel":              "excel",
    "powerpoint":                   "powerpnt",
    "microsoft powerpoint":         "powerpnt",
    "onenote":                      "onenote",
    "outlook":                      "outlook",
    "microsoft outlook":            "outlook",
    "todoist":                      "todoist",
    "trello":                       "trello",
    "evernote":                     "evernote",
    "libreoffice":                  "soffice",
    "libre office":                 "soffice",

    # media & entertainment
    "spotify":                      "spotify",
    "vlc":                          "vlc",
    "vlc player":                   "vlc",
    "media player":                 "wmplayer",
    "windows media player":         "wmplayer",
    "netflix":                      "netflix",
    "youtube music":                "youtubemusic",
    "itunes":                       "itunes",
    "plex":                         "plex",
    "kodi":                         "kodi",
    "foobar":                       "foobar2000",
    "foobar2000":                   "foobar2000",
    "audacity":                     "audacity",

    # image & video editing
    "photoshop":                    "photoshop",
    "adobe photoshop":              "photoshop",
    "illustrator":                  "illustrator",
    "adobe illustrator":            "illustrator",
    "premiere":                     "premiere",
    "adobe premiere":               "premiere",
    "after effects":                "afterfx",
    "adobe after effects":          "afterfx",
    "lightroom":                    "lightroom",
    "adobe lightroom":              "lightroom",
    "gimp":                         "gimp",
    "figma":                        "figma",
    "davinci resolve":              "resolve",
    "davinci":                      "resolve",
    "capcut":                       "capcut",
    "canva":                        "canva",
    "blender":                      "blender",
    "inkscape":                     "inkscape",

    # file management & utilities
    "explorer":                     "explorer",
    "file explorer":                "explorer",
    "7zip":                         "7zfm",
    "7-zip":                        "7zfm",
    "winrar":                       "winrar",
    "everything":                   "everything",
    "total commander":              "totalcmd",
    "onedrive":                     "onedrive",
    "dropbox":                      "dropbox",
    "google drive":                 "googledrivesync",

    # system tools
    "task manager":                 "taskmgr",
    "control panel":                "control",
    "settings":                     "ms-settings:",
    "windows settings":             "ms-settings:",
    "registry editor":              "regedit",
    "regedit":                      "regedit",
    "device manager":               "devmgmt.msc",
    "disk management":              "diskmgmt.msc",
    "event viewer":                 "eventvwr.msc",
    "calculator":                   "calc",
    "calc":                         "calc",
    "snipping tool":                "snippingtool",
    "snip":                         "snippingtool",
    "paint":                        "mspaint",
    "mspaint":                      "mspaint",
    "clock":                        "clock",
    "sticky notes":                 "stikynot",

    # development & database tools
    "postman":                      "postman",
    "insomnia":                     "insomnia",
    "docker":                       "docker desktop",
    "docker desktop":               "docker desktop",
    "dbeaver":                      "dbeaver",
    "mysql workbench":              "mysqlworkbench",
    "mongodb compass":              "mongodbcompass",
    "pgadmin":                      "pgadmin4",
    "filezilla":                    "filezilla",
    "putty":                        "putty",

    # gaming
    "steam":                        "steam",
    "epic games":                   "epicgameslauncher",
    "epic":                         "epicgameslauncher",
    "xbox":                         "xboxapp",
    "xbox app":                     "xboxapp",
    "gog":                          "gogalaxy",
    "gog galaxy":                   "gogalaxy",
    "origin":                       "origin",
    "ea app":                       "eadesktop",
    "battle.net":                   "battle.net",
    "battlenet":                    "battle.net",
    "ubisoft connect":              "ubisoftconnect",
    "uplay":                        "ubisoftconnect",

    # security
    "bitwarden":                    "bitwarden",
    "lastpass":                     "lastpass",
    "malwarebytes":                 "malwarebytes",
    "windows defender":             "windowsdefender:",
    "defender":                     "windowsdefender:",

    # notes & writing
    "typora":                       "typora",
    "notion":                       "notion",
    "bear":                         "bear",
    "craft":                        "craft",
    "logseq":                       "logseq",
    "roam":                         "roamresearch",
}

SKIP_WORDS = {"with", "and", "also", "plus", "along"}

def extract_app_list(tokens: list, start_index: int) -> list:
    """
    Given tokens and the index right after 'mode',
    extracts all recognized app names as a list.
    """
    apps = []
    i = start_index

    while i < len(tokens):
        # skip filler words
        if tokens[i] in SKIP_WORDS:
            i += 1
            continue

        # try matching longest sequence first (3-word, 2-word, 1-word)
        matched = False
        for window in [3, 2, 1]:
            if i + window <= len(tokens):
                phrase = " ".join(tokens[i:i+window])
                if phrase in APP_ALIASES:
                    apps.append(APP_ALIASES[phrase])
                    i += window
                    matched = True
                    break

        # unrecognized token — skip it
        if not matched:
            i += 1

    return apps

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

                    # handling open_mode case:
                    if verb in ["open", "close"]:
                        if i+1 < len(tokens):
                            for j in range(i+1, len(tokens)):
                                if tokens[j] == "mode":
                                    if verb == "open":
                                        command_ir.action = "open_mode"
                                    else:
                                        command_ir.action = "close_mode"
                                    action_found = True
                                    break

                    # handling all other cases:
                    if not action_found:
                        command_ir.action = SPECIAL_ACTIONS[verb]   # action found based on verb
                        action_found = True

                    # finding target for special action
                    if (i+1) < len(tokens):     # for no out-of-bound condition

                        # handling create_mode case:
                        if command_ir.action == "create_mode":
                            k = i+1     # index for accessing values
                            target = ""     # tokens to be added later
                            while k < len(tokens):
                                target = target + " " + tokens[k]
                                if tokens[k] == "mode":     # i.e., we got the complete mode name
                                    break
                                k += 1      # increment
                            if not (target == ""):
                                target = target.strip()     # since a leading space is added
                                target_found = True
                
                        else:
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

        # level as a parameter
        if isinstance(token, int): # only for integers
            command_ir.parameters["level"] = token

            # checking for 'minus' in words for numeric values found!
            if i > 0 and tokens[i-1] == "minus":
                command_ir.parameters["level"] = 0 - token

        # application names as a list of parameters
        if command_ir.action == "create_mode" and i - 1 >= 0 and tokens[i-1] == "mode":
            app_list = extract_app_list(tokens, i + 1)
            command_ir.parameters["app_list"] = app_list

    return command_ir