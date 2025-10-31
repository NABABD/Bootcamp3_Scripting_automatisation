variable "image_name" {
  type    = string
  default = "/home/admin/nova-sentinel-infra/terraform/ubuntu-15.04.tar.xz"
}

variable "interface_name" {
  type    = string
  default = "vboxnet0"
}

variable "ram" {
  type    = string
  default = "512 mib"
}

variable "cpu" {
  type    = number
  default = 1
}
