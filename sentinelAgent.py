#!/usr/bin/python3

import os, subprocess, psutil, socket, platform, json, logging, datetime


logging.basicConfig(
    filename="./sentinel_init.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
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

    try:
        logging.info("Get memory informations")
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent
    except:
        logging.warning("Error in getting memory informations")

    print("IP Address : ", socket.gethostbyname(socket.gethostname()))
    print("Network interfaces : ", psutil.net_if_addrs().keys())
    # print("Open ports : ", subprocess.getoutput("ss -tulnp"))

    print("Process Number : ", )

if __name__=="__main__":
    main()