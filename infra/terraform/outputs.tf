output "ec2_public_ip" {
  value = aws_instance.lockpad_ec2.public_ip
}

output "frontend_bucket_name" {
  value = aws_s3_bucket.frontend.bucket
}

output "frontend_bucket_website_endpoint" {
  value = aws_s3_bucket_website_configuration.frontend_site.website_endpoint
}

output "lockpad_elastic_ip" {
  value = aws_eip.lockpad_eip.public_ip
}


