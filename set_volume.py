from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from command_ir import CommandIR

# ── Audio Setup ───────────────────────────────────────────

devices = AudioUtilities.GetSpeakers()
interface = devices.EndpointVolume
volume = cast(interface, POINTER(IAudioEndpointVolume))


# ── Core Utility ──────────────────────────────────────────

def _apply_volume_change(target_level: float):
    # clamp between 0–100
    target_level = max(0, min(target_level, 100))

    # set volume
    volume.SetMasterVolumeLevelScalar(target_level / 100, None)

    # 🔥 sync mute state with volume (fix for keyboard mute light)
    if target_level == 0:
        volume.SetMute(1, None)
    else:
        volume.SetMute(0, None)


# ── Volume Actions ────────────────────────────────────────

def set_volume(ir: CommandIR):
    level = ir.parameters.get("level")
    if level is None:
        return

    _apply_volume_change(level)


def increase_volume(ir: CommandIR):
    level = ir.parameters.get("level")

    if level is not None:
        # absolute set
        _apply_volume_change(level)
        return

    # relative +10
    current = volume.GetMasterVolumeLevelScalar() * 100
    _apply_volume_change(current + 10)


def decrease_volume(ir: CommandIR):
    level = ir.parameters.get("level")

    if level is not None:
        # absolute set
        _apply_volume_change(level)
        return

    # relative -10
    current = volume.GetMasterVolumeLevelScalar() * 100
    _apply_volume_change(current - 10)


def mute(ir: CommandIR):
    volume.SetMute(1, None)


def unmute(ir: CommandIR):
    volume.SetMute(0, None)


def toggle_mute(ir: CommandIR):
    current = volume.GetMute()
    volume.SetMute(0 if current else 1, None)