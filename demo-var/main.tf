provider "aws" {
    region = "eu-central-1"
  
}

resource "aws_instance" "Instancedemo" {
  ami = "ami-0910ce22fbfa68e1d"
  instance_type = var.instance_type
  tags = {
    Name = "Trraform EC2"
  }
}
