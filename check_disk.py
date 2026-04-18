import shutil
from command_ir import CommandIR

def check_disk(ir:CommandIR):
    total_space, used_space, free_space = shutil.disk_usage("C:\\")

    # converting to gb
    total_space /= (1024 * 1024 * 1024)
    used_space /= (1024 * 1024 * 1024)
    free_space /= (1024 * 1024 * 1024)

    print("Total Disk Space:", f"{total_space:.2f}", "GB")
    print("Used Disk Space:", f"{used_space:.2f}", "GB")
    print("Free Disk Space:", f"{free_space:.2f}", "GB")