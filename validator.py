from command_ir import CommandIR
import shutil

LEVEL_ACTIONS = {
    "increase_brightness", "decrease_brightness", "set_brightness",
    "increase_volume", "decrease_volume", "set_volume",
    "increase_zoom", "decrease_zoom", "set_zoom"
}

APPLICATION_ACTIONS = {
    "open_application",
    "close_application"
}

def validator(command_ir: CommandIR) -> CommandIR:

    # validating 'level' parameter
    if command_ir.action in LEVEL_ACTIONS:
        level = command_ir.parameters.get("level")

        if level is None: 
            # setting default level, if not
            command_ir.parameters["level"] = 50
            command_ir.warnings.append("No level provided. Defaulted to 50.")
        else:
            # capping down level beyond 100
            if level > 100:
                command_ir.parameters["level"] = 100
                command_ir.warnings.append("Level provided greater than 100. Capped down to 100.")
            # if level less than 0, setting it to minimum == 0
            if level < 0:
                command_ir.parameters["level"] = 0
                command_ir.warnings.append("Level provided less than 0. Set to 0.")

    # checking application validness
    if command_ir.action in APPLICATION_ACTIONS and command_ir.target is not None:
        if shutil.which(command_ir.target) is None:
            command_ir.errors.append("Target not found on the system!")

    return command_ir