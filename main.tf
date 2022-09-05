# terraform block
terraform {
    required_version = "~> 0.14"
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.0"
        }
    }
}

# provider block
provider "aws" {
  profile = "default"
  region = "ap-south-1"
}
# create instance
resource "aws_instance" "ec2demo" {
  ami = "ami-08df646e18b182346"
  instance_type = "t2.micro"
  user_data = file("${path_to_file}/file.sh") # to install user data in instance after launch
  tags = {
    "Name" = "EC2 Demo"
  }
}

# Create a VPC
resource "aws_vpc" "my-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "VPC_name"
  }
}

# Create Web Public Subnet
resource "aws_subnet" "web-subnet-1" {
  vpc_id                  = aws_vpc.my-vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-south-1"
  map_public_ip_on_launch = true

  tags = {
    Name = "Web-1a"
  }
}

# Create a database server
resource "aws_db_instance" "default" {
    allocated_storage = 10
    engine         = "mysql"
    engine_version = "8.0.20"
    instance_class = "db.t3.micro"
    name           = "db_name"
    username       = "username"
    password       = "password"
}

# Create an Network Load Balancer
resource "aws_lb" "NLB17" {
    name = "NLB17"
    internal = false
    load_balancer_type = "network"
    subnets = ["public-subnet", "public-subnet"]
    enable_deletion_protection = false/true
}
