resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.acme_vpc.id
  tags = {
    Name = "IGW"
  }
}
