import screen_brightness_control as sbc
from command_ir import CommandIR

def set_brightness(ir:CommandIR):
    sbc.set_brightness(ir.parameters["level"])

def increase_brightness(ir:CommandIR):
    if ir.parameters.get("level") is not None:
        set_brightness(ir)
    else:
        current_brightness_level = sbc.get_brightness()[0]      # indexing because it returns a list (in case: multiple monitors)
        sbc.set_brightness(current_brightness_level + 10)

def decrease_brightness(ir:CommandIR):
    if ir.parameters.get("level") is not None:
        set_brightness(ir)
    else:
        current_brightness_level = sbc.get_brightness()[0]      # indexing because it returns a list (in case: multiple monitors)
        sbc.set_brightness(current_brightness_level - 10)