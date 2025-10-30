terraform {
  required_providers {
    virtualbox = {
      source = "terra-farm/virtualbox"
      version = "0.2.2-alpha.1"
    }
  }
}

resource "virtualbox_vm" "node" {
  count     = 2
  name      = format("node-%02d", count.index + 1)
  image     = "./ubuntu-15.04.tar.xz"
  cpus      = 1
  memory    = "256 mib"

  network_adapter {
    type           = "hostonly"
    host_interface = "vboxnet0"
  }
}

resource "virtualbox_vm" "monitor" {
  name      = "monitor"
  image     = "./ubuntu-15.04.tar.xz"
  cpus      = 1
  memory    = "256 mib"

  network_adapter {
    type           = "hostonly"
    host_interface = "vboxnet0"
  }
}