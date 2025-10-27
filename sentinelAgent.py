#!/usr/bin/python3

import os, subprocess, psutil, socket, platform, json, logging, datetime


logging.basicConfig(
    filename="./sentinel_init.log",
    level=logging.INFO
)

def main():
    logging.info("Start audit")

    try:
        logging.info("Get system informations")
        hostname = socket.gethostname()
        os_name = platform.system()
        os_version = platform.version()
    except:
        logging.warning("Error in getting system infomations")

    print("CPU usage : ", psutil.cpu_percent(), "%")
    print("RAM usage : ", psutil.virtual_memory().percent, "%")
    print("Disk usage : ", psutil.disk_usage("/").percent, "%")

    print("IP Address : ", socket.gethostbyname(socket.gethostname()))
    print("Network interfaces : ", psutil.net_if_addrs().keys())
    # print("Open ports : ", subprocess.getoutput("ss -tulnp"))

    print("Process Number : ", )

if __name__=="__main__":
    main()