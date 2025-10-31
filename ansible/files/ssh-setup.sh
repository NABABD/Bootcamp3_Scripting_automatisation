#!/bin/bash

: '
This script performs a clean installation and basic setup of the SSH service on a Debian system.
Usage:
1. Save this script in a file (e.g., ssh_setup.sh).
2. Make it executable (chmod +x ssh_setup.sh).
3. Run the script with ./ssh_setup.sh.
Note: Use this script with caution and review/edit the configuration settings based on your requirements.
'

# Clean uninstallation of SSH
sudo apt-get purge openssh-server
sudo rm -rf /etc/ssh/

# Update package lists
sudo apt-get update

# Install SSH service
sudo apt-get install openssh-server

# Start the SSH service
sudo service ssh start
# Or, for systems with systemd:
# sudo systemctl start ssh

# Basic SSH configuration
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup   # Backup the original configuration file
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config      # Set the listening port to 22
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config   # Disable root login
sudo sed -i 's/PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config   # Enable password authentication

# Restart the SSH service to apply changes
sudo service ssh restart
# Or, for systems with systemd:
# sudo systemctl restart ssh

echo "SSH clean install and basic setup completed."