import psutil
import subprocess
import time
from command_ir import CommandIR

def open_application(ir: CommandIR):
    # target: either an application OR a url
    if ir.parameters["fallback_url"] is None:
        subprocess.Popen(["start", ir.target], shell=True)      # directly execute whatever is

        # NOTE: Start DOESN'T report whether such an application/website exists or not!
        
    else:       # target: could be both application and a url
        # first, run the application
        subprocess.Popen(["start", ir.target], shell=True)

        # next: check if it actually ran by
        # checking whether such a process was created or not
        time.sleep(2)       # wait for 2 seconds

        installed_application_ran = False   # flag
        for process in psutil.process_iter(['name']):
            if ir.target == process.info['name'].lower():
                installed_application_ran = True
        
        # check for fallback_url execution
        if not installed_application_ran:       # i.e.: no installed application ran
            subprocess.Popen(["start", ir.parameters["fallback_url"]], shell=True)