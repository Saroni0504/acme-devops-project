resource "aws_subnet" "public_subnet" {
  count                   = 2
  vpc_id                  = aws_vpc.acme_vpc.id
  cidr_block              = "10.0.${count.index + 1}.0/24"
  availability_zone       = element(["us-east-1a", "us-east-1b"], count.index)
  map_public_ip_on_launch = true
  tags = {
    Name = "public-subnet-${count.index + 1}"
  }
}

resource "aws_subnet" "private_subnet" {
  count             = 2
  vpc_id            = aws_vpc.acme_vpc.id
  cidr_block        = "10.0.${count.index + 3}.0/24"
  availability_zone = element(["us-east-1a", "us-east-1b"], count.index)
  tags = {
    Name = "private-subnet-${count.index + 3}"
  }
}
