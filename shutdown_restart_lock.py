import subprocess
import ctypes
from command_ir import CommandIR

# shutdown
def shutdown(ir):
    subprocess.run(["shutdown", "/s", "/t", "0"])   

# restart
def restart(ir):
    subprocess.run(["shutdown", "/r", "/t", "0"])   

# lock screen
def lock_screen(ir):
    ctypes.windll.user32.LockWorkStation()           