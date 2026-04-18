import psutil
from command_ir import CommandIR

def close_application(ir: CommandIR):
    target = ir.target
    
    # process found and close
    found_and_closed = False

    for process in psutil.process_iter(['name']):
        if target in process.info['name'].lower():
            process.terminate()
            found_and_closed = True
    
    if not found_and_closed:
        print("Warning: No such process was running, to be closed.")