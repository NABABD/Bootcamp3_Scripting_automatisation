#!/usr/bin/python3

import os, subprocess, psutil, socket, platform, json, logging, datetime
from pathlib import Path

REPORT_DIR = "reports"
LOG_FILE_NAME = "sentinel_init.log"
if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

LOG_PATH = Path(REPORT_DIR) / LOG_FILE_NAME
logging.basicConfig(
    filename=LOG_PATH,
    #filename="./sentinel_init.log",
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

    print("Process Number : ", len(psutil.pids()))


    logging.info("End audit")

    json_path = Path(REPORT_DIR) / "sentinel_report.json"
    md_path = Path(REPORT_DIR) / "sentinel_report.md"
    report_data = {
        "hostname": hostname,
        "os_name": os_name,
        "os_version": os_version,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
        "timestamp": datetime.datetime.now().isoformat()
    }

    with open(json_path, "w") as report_file:
        json.dump(report_data, report_file, indent=4)   

    markdown_content = f"""# Rapport Sentinel de Surveillance
    ## Informations Système
    - **Nom d'hôte** : {hostname}   
    - **Système d'exploitation** : {os_name}
    - **Version du système d'exploitation** : {os_version}
    ## Utilisation des Ressources
    - **Utilisation du CPU** : {cpu_usage} %
    - **Utilisation de la RAM** : {ram_usage} % 
    - **Utilisation du Disque** : {disk_usage} %
    ## Horodatage   
    - **Généré le** : {datetime.datetime.now().isoformat()}
    """

    with open(md_path, "w") as md_file:
        md_file.write(markdown_content)
    

    
if __name__=="__main__":
    main()