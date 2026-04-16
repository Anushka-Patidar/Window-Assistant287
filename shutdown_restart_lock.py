import subprocess
import ctypes

# shutdown
def shutdown():
    subprocess.run(["shutdown", "/s", "/t", "0"])   

# restart
def restart():
    subprocess.run(["shutdown", "/r", "/t", "0"])   

# lock screen
def lock_screen():
    ctypes.windll.user32.LockWorkStation()           