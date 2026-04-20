import speedtest
from command_ir import CommandIR

def check_internet(ir:CommandIR):
    # calling function to check connectivity
    internet = speedtest.Speedtest()
    internet.get_best_server()

    download_speed_in_bits = internet.download()
    upload_speed_in_bits = internet.upload()

    download_speed_in_mbps = download_speed_in_bits // (1024 * 1024)
    upload_speed_in_mbps = upload_speed_in_bits // (1024 * 1024)

    print("Internet Connectivity Check:")
    print("Download Speed:", download_speed_in_mbps, "MBPS")
    print("Upload Speed:", upload_speed_in_mbps, "MBPS")