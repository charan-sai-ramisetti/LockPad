variable "aws_region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "ami_id" {
  description = "Ubuntu 22.04 AMI ID"
  default     = "ami-02b8269d5e85954ef"
}
