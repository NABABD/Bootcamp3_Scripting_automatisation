# Declare VirtualBox provider
terraform {
  required_providers {
    virtualbox = {
      source  = "terra-farm/virtualbox"
      version = "0.2.2-alpha.1"
    }
  }
}

# Declare App nodes VMs
resource "virtualbox_vm" "node" {
  count  = 2
  name   = format("node-%02d", count.index + 1)
  image  = var.image_name
  cpus   = var.cpu
  memory = var.ram

  network_adapter {
    type           = "hostonly"
    host_interface = var.interface_name
  }

  network_adapter {
    type = "nat"
  }
}

# Declare Monitoring node VM
resource "virtualbox_vm" "monitor" {
  name   = "monitor"
  image  = var.image_name
  cpus   = var.cpu
  memory = var.ram

  network_adapter {
    type           = "hostonly"
    host_interface = var.interface_name
  }

  network_adapter {
    type = "nat"
  }
}

resource "null_resource" "generate_inventory" {
  depends_on = [virtualbox_vm.node, virtualbox_vm.monitor]

  provisioner "local-exec" {
    command = "/usr/bin/python3 /home/admin/nova-sentinel-infra/ansible/files/generate_hosts.py '${join(",", virtualbox_vm.node.*.network_adapter.0.ipv4_address)}' '${element(virtualbox_vm.monitor.*.network_adapter.0.ipv4_address, 1)}'"
  }
}

resource "null_resource" "ansible_playbook" {
  depends_on = [null_resource.generate_inventory]

  provisioner "local-exec" {
    command = "ansible-playbook -i /home/admin/nova-sentinel-infra/ansible/inventory/hosts.ini /home/admin/nova-sentinel-infra/ansible/playbooks/nodes.yaml /home/admin/nova-sentinel-infra/ansible/playbooks/appservers.yaml"
  }
}
