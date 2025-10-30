output "IPAddr_node_1" {
  value = element(virtualbox_vm.node.*.network_adapter.0.ipv4_address, 1)
}

output "IPAddr_node_2" {
  value = element(virtualbox_vm.node.*.network_adapter.0.ipv4_address, 2)
}

output "IPAddr_monitor" {
  value = element(virtualbox_vm.monitor.*.network_adapter.0.ipv4_address, 2)
}