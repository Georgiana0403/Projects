This project creates a fully functional VPC setup in AWS using CloudFormation, consisting of:

1. **VPC**: A Virtual Private Cloud (VPC) with a CIDR block of `10.0.0.0/16`.
2. **Public Subnets**: Two public subnets in different availability zones (`10.0.1.0/24` and `10.0.2.0/24`).
3. **Private Subnets**: Two private subnets in different availability zones (`10.0.3.0/24` and `10.0.4.0/24`).
4. **Internet Gateway**: Allows traffic from the public subnets to reach the internet.
5. **NAT Gateway**: Provides internet access to the private subnets.
6. **EC2 Instances**: 
   - **Public EC2**: An EC2 instance in the public subnet running a web server (Apache), open to the internet.
   - **Private EC2**: An EC2 instance in the private subnet, accessible only from the public EC2 instance via SSH.
