import sys

def generate_hosts_file(node_ips, monitor_ip):
    hosts_file = "/home/admin/nova-sentinel-infra/ansible/inventory/hosts.ini"
    
    with open(hosts_file, 'w') as f:
        f.write("[applications]\n")
        for ip in node_ips:
            f.write(f"{ip}\n")
        
        f.write("\n[monitoring]\n")
        f.write(f"{monitor_ip}\n")
        
        f.write("\n[all:vars]\n")
        f.write('ansible_user="ubuntu"\n')
        f.write('ansible_port=2222\n')
        f.write('ansible_ssh_private_key_file="~/.ssh/id_ed25519"\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_hosts.py '<node_ips>' '<monitor_ip>'")
        sys.exit(1)
    
    node_ips = sys.argv[1].split(',')
    monitor_ip = sys.argv[2]
    
    generate_hosts_file(node_ips, monitor_ip)
