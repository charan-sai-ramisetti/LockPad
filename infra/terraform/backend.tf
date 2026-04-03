terraform {
  backend "s3" {
    bucket         = "lockpad-terraform-state-bucket"
    key            = "global/s3/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "lockpad-terraform-lock"
    encrypt        = true
  }
}