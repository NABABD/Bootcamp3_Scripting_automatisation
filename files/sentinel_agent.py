#!/usr/bin/python3

import os, subprocess, psutil, socket, platform, json, logging, datetime

REPORT_DIR = "/var/log/sentinel/reports/"

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

logging.basicConfig(
    filename=REPORT_DIR+"sentinel_init.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

def identify_open_ports():
    ports_list = []
    Port = 0 #First port.
    while Port <= 65535: #Port 65535 is last port you can access.
        try:
            try:
                Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #Create a socket.
            except:
                logging.error("Error: Can't open socket!")    
                break #If can't open socket, exit the loop.
            Socket.connect(("127.0.0.1", Port)) #Try connect the port. If port is not listening, throws ConnectionRefusedError. 
            Connected = True
        except ConnectionRefusedError:
            Connected = False       
        finally:
            if(Connected and Port != Socket.getsockname()[1]): #If connected,
                ports_list.append(Port) #Append port to list
            Port = Port + 1 #Increase port.
            Socket.close() #Close socket.
    return ports_list

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

    try:
        logging.info("Get network informations")
        ip_address = socket.gethostbyname(socket.gethostname())
        interfaces = list(psutil.net_if_addrs().keys())
        open_ports = identify_open_ports()
    except:
        logging.warning("Error in getting network informations")

    # print("Open ports : ", subprocess.getoutput("ss -tulnp"))

    try:
        logging.info("Get process informations")
        process_number = len(psutil.pids())
    except:
        logging.warning("Error in getting process informations")


    logging.info("End audit")

    
    try:
        logging.info("Generation of the .json report")
        report_data = {
            "system" : {
                "hostname"   : hostname,
                "os_name"    : os_name,
                "os_version" : os_version,
            },
            "memory" : {
                "cpu_usage"  : cpu_usage,
                "ram_usage"  : ram_usage,
                "disk_usage" : disk_usage,
            },
            "network" : {
                "ip_address" : ip_address,
                "interfaces" : interfaces,
                "open_ports" : open_ports,
            },
            "process" : {
                "number" : process_number,
            }
        }

        with open(REPORT_DIR+"sentinel_report.json", "w", encoding='utf-8') as report_file:
            json.dump(report_data, report_file, indent=4)
        logging.info("File successfully generated")
    except:
        logging.warning("Error in creating the .json report")

    try:
        logging.info("Generation of the .md report")
        markdown_content = f"""# Rapport Sentinel de Surveillance
        ## Informations Système
        - **Nom d'hôte** : {hostname}   
        - **Système d'exploitation** : {os_name}
        - **Version du système d'exploitation** : {os_version}
        ## Utilisation des Ressources
        - **Utilisation du CPU** : {cpu_usage} %
        - **Utilisation de la RAM** : {ram_usage} % 
        - **Utilisation du Disque** : {disk_usage} %
        ## Informations Réseau
        - **Adresse IP** : {ip_address}
        - **Interfaces réseaux** : {interfaces}
        - **Ports ouverts** : {open_ports}
        ## Informations des Processus
        - **Nombre de processus** : {process_number}
        ## Horodatage   
        - **Généré le** : {datetime.datetime.now().isoformat()}
        """
        
        with open(REPORT_DIR+"sentinel_report.md", "w", encoding='utf-8') as md_file:
            md_file.write(markdown_content)
        logging.info("File successfully generated")
    except:
        logging.warning("Error in creating the .md report")

    
if __name__=="__main__":
    main()