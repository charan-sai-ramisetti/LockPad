provider "aws" {
  region = "ap-south-1"  # Change if needed
}

# ---------------------------
# S3 Bucket for Terraform State
# ---------------------------
resource "aws_s3_bucket" "tf_state" {
  bucket = "lockpad-terraform-state-bucket"

  tags = {
    Name        = "lockpad-tf-state"
    Environment = "dev"
  }
}

# Enable versioning
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.tf_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Enable encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.tf_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Block public access
resource "aws_s3_bucket_public_access_block" "block_public" {
  bucket = aws_s3_bucket.tf_state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# ---------------------------
# DynamoDB Table for Locking
# ---------------------------
resource "aws_dynamodb_table" "tf_lock" {
  name         = "lockpad-terraform-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name        = "lockpad-tf-lock"
    Environment = "dev"
  }
}