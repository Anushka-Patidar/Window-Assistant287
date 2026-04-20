from command_ir import CommandIR


# ─── Verb Resolution ─────────────────────────────────────────────────────────
# Maps canonical (software-name) verb → list of synonyms the user might say.
# Flattened below for O(1) lookup during parsing.

VERB_SYNONYMS = {
    "increase": ["increase", "raise", "boost", "brighten", "higher", "more", "enhance",
                 "intensify", "amplify", "elevate", "heighten", "crank", "bump", "louder",
                 "enlarge", "magnify", "expand", "grow"],
    "decrease": ["decrease", "lower", "reduce", "dim", "less", "soften", "minimize",
                 "darken", "drop", "shrink", "tone", "weaken", "fade", "cut", "quieter"],
    "set":      ["set", "put", "make", "change", "adjust", "fix", "assign", "configure",
                 "define", "update", "apply", "move", "go", "shift", "push"],
    "mute":     ["mute", "silence", "quiet", "hush", "suppress", "deafen", "drown",
                 "block", "zero"],
    "open":     ["open", "launch", "start", "run", "execute", "load", "boot", "fire",
                 "begin", "initiate", "activate", "bring", "pull", "access", "enter"],
    "close":    ["close", "quit", "exit", "kill", "stop", "terminate", "shut", "end",
                 "finish", "destroy", "remove", "collapse", "dismiss", "leave", "abandon"],
    "check":    ["check", "test", "measure", "diagnose", "verify", "inspect", "monitor",
                 "analyze", "scan", "ping", "evaluate"],
    "create":   ["create", "make", "add", "new", "save", "build", "setup", "define",
                 "register", "store"],
    "delete":   ["delete", "remove", "destroy", "erase", "clear", "wipe", "drop",
                 "unregister"],
    "remind":   ["remind", "schedule", "alert"]
}

# flattened: synonym → canonical verb  (built once at import time)
flattened_verb_dict = {
    synonym: verb
    for verb, synonyms in VERB_SYNONYMS.items()
    for synonym in synonyms
}


# ─── Target Resolution ───────────────────────────────────────────────────────
# Maps canonical target → list of synonyms the user might say.
# Flattened below for O(1) lookup during parsing.

TARGET_SYNONYMS = {
    "brightness": ["brightness", "bright", "screen", "display", "backlight",
                   "luminance", "glow"],
    "volume":     ["volume", "sound", "audio", "noise", "speaker", "music"],
    "internet":   ["internet", "wifi", "network", "connection", "connectivity",
                   "speed", "bandwidth", "web", "signal", "net"],
    "disk":       ["disk", "storage", "drive", "space", "memory",
                   "hard drive", "harddrive", "ssd", "hdd", "c drive"],
}

# flattened: synonym → canonical target  (built once at import time)
flattened_target_dict = {
    synonym: target
    for target, synonyms in TARGET_SYNONYMS.items()
    for synonym in synonyms
}


# ─── Standalone Actions ───────────────────────────────────────────────────────
# Single-token commands that need no target — the token alone IS the full action.

STANDALONE_ACTIONS = {
    # shutdown
    "shutdown":       "shutdown",
    "off":            "shutdown",
    "poweroff":       "shutdown",
    "halt":           "shutdown",
    "power":          "shutdown",

    # restart
    "restart":        "restart",
    "reboot":         "restart",
    "reset":          "restart",
    "reload":         "restart",
    "refresh":        "restart",
    "cycle":          "restart",
    "renew":          "restart",
    "reinitialize":   "restart",
    "restore":        "restart",
    "bounce":         "restart",
    "redo":           "restart",
    "flip":           "restart",

    # lock screen
    "lock":           "lock_screen",
    "secure":         "lock_screen",
    "protect":        "lock_screen",
    "sleep":          "lock_screen",
    "guard":          "lock_screen",
    "freeze":         "lock_screen",
    "seal":           "lock_screen",
    "hide":           "lock_screen",
    "suspend":        "lock_screen",
    "idle":           "lock_screen",
    "pause":          "lock_screen",
    "engage":         "lock_screen",
    "arm":            "lock_screen",

    # mute
    "mute":           "mute",
    "silence":        "mute",
    "quiet":          "mute",
    "hush":           "mute",
    "suppress":       "mute",
    "deafen":         "mute",
    "drown":          "mute",
    "block":          "mute",
    "zero":           "mute",
}


# ─── Special Actions ──────────────────────────────────────────────────────────
# Verbs whose action name is NOT constructed as verb + "_" + target.
# These get a direct action string and need their own target-extraction logic.

SPECIAL_ACTIONS = {
    "open":   "open_application",
    "close":  "close_application",
    "create": "create_mode",
    "delete": "delete_mode",
    "update": "update_mode",
    "remind": "create_reminder"
}

# tokens that signal the user wants force-web opening (used in parameter pass)
FORCE_WEB_PHRASES = {
    "browser", "web", "online", "internet", "site", "website", "webpage"
}

# preposition words to strip when cleaning target for force_web
STRIP_PREPOSITIONS = {"in", "on", "via", "through", "using", "with"}


# ─── App Aliases (for mode creation) ─────────────────────────────────────────
# Maps user-friendly name → executable name.
# Used by extract_app_list when building app lists for modes.
# To add a new app: add one entry here.

APP_ALIASES = {
    # ── Browsers ────────────────────────────────────────────────────────────────
    "chrome":                   "chrome",
    "google chrome":            "chrome",
    "firefox":                  "firefox",
    "mozilla firefox":          "firefox",
    "edge":                     "msedge",
    "microsoft edge":           "msedge",
    "opera":                    "opera",
    "brave":                    "brave",
    "brave browser":            "brave",
    "vivaldi":                  "vivaldi",
    "tor":                      "tor browser",
    "tor browser":              "tor browser",

    # ── Code Editors & IDEs ─────────────────────────────────────────────────────
    "vs code":                  "code",
    "vscode":                   "code",
    "visual studio code":       "code",
    "visual studio":            "devenv",
    "pycharm":                  "pycharm",
    "intellij":                 "idea",
    "intellij idea":            "idea",
    "webstorm":                 "webstorm",
    "android studio":           "studio64",
    "sublime":                  "sublime_text",
    "sublime text":             "sublime_text",
    "atom":                     "atom",
    "notepad":                  "notepad",
    "notepad++":                "notepad++",
    "vim":                      "vim",
    "neovim":                   "nvim",

    # ── Terminals & Shells ──────────────────────────────────────────────────────
    "terminal":                 "wt",
    "windows terminal":         "wt",
    "cmd":                      "cmd",
    "command prompt":           "cmd",
    "powershell":               "powershell",
    "git bash":                 "git-bash",
    "wsl":                      "wsl",

    # ── Communication ───────────────────────────────────────────────────────────
    "discord":                  "discord",
    "slack":                    "slack",
    "teams":                    "teams",
    "microsoft teams":          "teams",
    "zoom":                     "zoom",
    "skype":                    "skype",
    "telegram":                 "telegram",
    "whatsapp":                 "whatsapp",
    "signal":                   "signal",

    # ── Productivity & Office ───────────────────────────────────────────────────
    "notion":                   "notion",
    "obsidian":                 "obsidian",
    "word":                     "winword",
    "microsoft word":           "winword",
    "excel":                    "excel",
    "microsoft excel":          "excel",
    "powerpoint":               "powerpnt",
    "microsoft powerpoint":     "powerpnt",
    "onenote":                  "onenote",
    "outlook":                  "outlook",
    "microsoft outlook":        "outlook",
    "todoist":                  "todoist",
    "trello":                   "trello",
    "evernote":                 "evernote",
    "libreoffice":              "soffice",
    "libre office":             "soffice",

    # ── Media & Entertainment ───────────────────────────────────────────────────
    "spotify":                  "spotify",
    "vlc":                      "vlc",
    "vlc player":               "vlc",
    "media player":             "wmplayer",
    "windows media player":     "wmplayer",
    "netflix":                  "netflix",
    "youtube music":            "youtubemusic",
    "itunes":                   "itunes",
    "plex":                     "plex",
    "kodi":                     "kodi",
    "foobar":                   "foobar2000",
    "foobar2000":               "foobar2000",
    "audacity":                 "audacity",

    # ── Image & Video Editing ───────────────────────────────────────────────────
    "photoshop":                "photoshop",
    "adobe photoshop":          "photoshop",
    "illustrator":              "illustrator",
    "adobe illustrator":        "illustrator",
    "premiere":                 "premiere",
    "adobe premiere":           "premiere",
    "after effects":            "afterfx",
    "adobe after effects":      "afterfx",
    "lightroom":                "lightroom",
    "adobe lightroom":          "lightroom",
    "gimp":                     "gimp",
    "figma":                    "figma",
    "davinci resolve":          "resolve",
    "davinci":                  "resolve",
    "capcut":                   "capcut",
    "canva":                    "canva",
    "blender":                  "blender",
    "inkscape":                 "inkscape",

    # ── File Management & Utilities ─────────────────────────────────────────────
    "explorer":                 "explorer",
    "file explorer":            "explorer",
    "7zip":                     "7zfm",
    "7-zip":                    "7zfm",
    "winrar":                   "winrar",
    "everything":               "everything",
    "total commander":          "totalcmd",
    "onedrive":                 "onedrive",
    "dropbox":                  "dropbox",
    "google drive":             "googledrivesync",

    # ── System Tools ────────────────────────────────────────────────────────────
    "task manager":             "taskmgr",
    "control panel":            "control",
    "settings":                 "ms-settings:",
    "windows settings":         "ms-settings:",
    "registry editor":          "regedit",
    "regedit":                  "regedit",
    "device manager":           "devmgmt.msc",
    "disk management":          "diskmgmt.msc",
    "event viewer":             "eventvwr.msc",
    "calculator":               "calc",
    "calc":                     "calc",
    "snipping tool":            "snippingtool",
    "snip":                     "snippingtool",
    "paint":                    "mspaint",
    "mspaint":                  "mspaint",
    "clock":                    "clock",
    "sticky notes":             "stikynot",

    # ── Development & Database Tools ────────────────────────────────────────────
    "postman":                  "postman",
    "insomnia":                 "insomnia",
    "docker":                   "docker desktop",
    "docker desktop":           "docker desktop",
    "dbeaver":                  "dbeaver",
    "mysql workbench":          "mysqlworkbench",
    "mongodb compass":          "mongodbcompass",
    "pgadmin":                  "pgadmin4",
    "filezilla":                "filezilla",
    "putty":                    "putty",

    # ── Gaming ──────────────────────────────────────────────────────────────────
    "steam":                    "steam",
    "epic games":               "epicgameslauncher",
    "epic":                     "epicgameslauncher",
    "xbox":                     "xboxapp",
    "xbox app":                 "xboxapp",
    "gog":                      "gogalaxy",
    "gog galaxy":               "gogalaxy",
    "origin":                   "origin",
    "ea app":                   "eadesktop",
    "battle.net":               "battle.net",
    "battlenet":                "battle.net",
    "ubisoft connect":          "ubisoftconnect",
    "uplay":                    "ubisoftconnect",

    # ── Security ────────────────────────────────────────────────────────────────
    "bitwarden":                "bitwarden",
    "lastpass":                 "lastpass",
    "malwarebytes":             "malwarebytes",
    "windows defender":         "windowsdefender:",
    "defender":                 "windowsdefender:",

    # ── Notes & Writing ─────────────────────────────────────────────────────────
    "typora":                   "typora",
    "bear":                     "bear",
    "craft":                    "craft",
    "logseq":                   "logseq",
    "roam":                     "roamresearch",
}

# filler words to skip over when scanning app lists in mode commands
SKIP_WORDS = {"with", "and", "also", "plus", "along"}


# ─── Helper: App List Extraction ─────────────────────────────────────────────

def extract_app_list(tokens: list, start_index: int) -> list:
    """
    Scans tokens from start_index onward and builds a list of resolved
    app executables / URLs for use in mode commands.

    Resolution priority per phrase:
      1. APP_ALIASES   → installed app executable name
      2. URL_TARGETS   → website URL
      3. raw token     → best-effort pass-through
    """
    from validator import URL_TARGETS   # imported here to avoid circular import

    apps = []
    i = start_index

    while i < len(tokens):

        if tokens[i] in SKIP_WORDS:
            i += 1
            continue

        matched = False
        for window in [3, 2, 1]:               # try longest match first
            if i + window <= len(tokens):
                phrase = " ".join(str(t) for t in tokens[i:i + window])

                if phrase in APP_ALIASES:
                    apps.append(APP_ALIASES[phrase])
                    i += window
                    matched = True
                    break

                if phrase in URL_TARGETS:
                    apps.append(URL_TARGETS[phrase])
                    i += window
                    matched = True
                    break

        if not matched:
            apps.append(tokens[i])             # unknown — pass through as-is
            i += 1

    return apps


# ─── Main Parser ─────────────────────────────────────────────────────────────

def command_parser(tokens: list) -> CommandIR:
    command_ir = CommandIR()

    # flags to check validity
    action_found = False
    target_found = False
    verb_found   = False
    verb, target = None, None

    for i, token in enumerate(tokens):

        # ── Standalone actions: single token = complete action, no target needed ──
        if token in STANDALONE_ACTIONS:
            command_ir.action = STANDALONE_ACTIONS[token]
            action_found = True
            verb_found   = True
            target_found = True
            break

        # ── All other verbs ───────────────────────────────────────────────────────
        else:

            if token in flattened_verb_dict:
                verb = flattened_verb_dict[token]
                verb_found = True

                if verb in SPECIAL_ACTIONS:

                    # open/close: check ahead for "mode" to decide open_mode vs open_application
                    if verb in ["open", "close"]:
                        if i + 1 < len(tokens):
                            for j in range(i + 1, len(tokens)):
                                if tokens[j] == "mode":
                                    command_ir.action = "open_mode" if verb == "open" else "close_mode"
                                    action_found = True
                                    break

                    # all other special verbs (create, delete, update, and open/close
                    # if "mode" was NOT found above)
                    if not action_found:
                        command_ir.action = SPECIAL_ACTIONS[verb]
                        action_found = True

                    # ── Target extraction for special actions ─────────────────────
                    if (i + 1) < len(tokens):

                        # create_mode: target = everything up to and including "mode"
                        if command_ir.action == "create_mode":
                            k = i + 1
                            target = ""
                            while k < len(tokens):
                                target = target + " " + tokens[k]
                                if tokens[k] == "mode":
                                    break
                                k += 1
                            if target:
                                target = target.strip()
                                target_found = True

                        # open_application: strip force-web signal words from target
                        elif command_ir.action == "open_application":
                            remaining = tokens[i + 1:]
                            force_web = any(t in FORCE_WEB_PHRASES for t in remaining)
                            if force_web:
                                command_ir.parameters["force_web"] = True
                                remaining = [
                                    t for t in remaining
                                    if t not in FORCE_WEB_PHRASES
                                    and t not in STRIP_PREPOSITIONS
                                ]
                            target = " ".join(str(t) for t in remaining)
                            target_found = True

                        # all other special actions: target = everything after the verb
                        else:
                            target = " ".join(str(t) for t in tokens[i + 1:])
                            target_found = True

                    else:
                        command_ir.errors.append("No target application provided!")
                        return command_ir

        # ── Target token lookup (non-special verbs) ───────────────────────────────
        if token in flattened_target_dict and not target_found:
            target = flattened_target_dict[token]
            target_found = True

        if verb_found and target_found:
            break

    # ── Error checks ─────────────────────────────────────────────────────────────
    if not verb_found:
        command_ir.errors.append("No action found!")
        return command_ir

    if not target_found:
        command_ir.errors.append("No target found!")
        return command_ir

    # ── Build action and target on the IR ────────────────────────────────────────
    if not action_found:
        command_ir.action = verb + "_" + target
    if target_found:
        command_ir.target = target

    # ── Parameter extraction ──────────────────────────────────────────────────────
    for i, token in enumerate(tokens):

        # numeric level parameter
        if isinstance(token, int):
            command_ir.parameters["level"] = token
            if i > 0 and tokens[i - 1] == "minus":
                command_ir.parameters["level"] = 0 - token

        # app list for mode creation
        if command_ir.action == "create_mode" and i - 1 >= 0 and tokens[i - 1] == "mode":
            command_ir.parameters["app_list"] = extract_app_list(tokens, i + 1)

    return command_ir