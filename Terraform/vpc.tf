resource "aws_vpc" "acme_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "vpc"
  }
}
