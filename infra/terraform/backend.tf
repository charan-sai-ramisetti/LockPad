terraform {
  backend "s3" {
    bucket         = "lockpad-terraform-state"
    key            = "lockpad/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    dynamodb_table = "lockpad-terraform-locks"
  }
}
