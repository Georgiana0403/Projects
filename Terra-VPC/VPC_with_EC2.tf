provider "aws" {
    region = "eu-central-1"
}

resource "aws_instance" "demo-server" {
    ami = "ami-0910ce22fbfa68e1d"
    key_name = "rtp-03"
    instance_type = "t2.micro"
    subnet_id = aws_subnet.subnet1.id
    vpc_security_group_ids = [ aws_security_group.sec-group.id ]
}
resource "aws_vpc" "geo-vpc" {
    cidr_block = "10.10.0.0/16"
  
}
resource "aws_subnet" "subnet1" {
    vpc_id = aws_vpc.geo-vpc.id
    cidr_block = "10.10.1.0/24"
    tags = {
        Name = "subnet1"
    }
  
}
resource "aws_internet_gateway" "igw1" {
    vpc_id = aws_vpc.geo-vpc.id
    tags = {
      Name = "igw1"
    }
  
}
resource "aws_route_table" "route1" {
    vpc_id = aws_vpc.geo-vpc.id
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw1.id
    }
    tags = {
        Name = "route-table"
    }
}

resource "aws_route_table_association" "route_table_association" {
    subnet_id = aws_subnet.subnet1.id
    route_table_id = aws_route_table.route1.id
  
}
resource "aws_security_group" "sec-group" {
    name = "sec-group"
    description = "Allow TLS inbound traffic"
    vpc_id = aws_vpc.geo-vpc.id

    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        ipv6_cidr_blocks = ["::/0"]
    }
    tags = {
      Name = "allow this"
    }
  
}
