# Devops Project

## Overview

This project is divided into two main parts:

## Part 1: Infrastructure Creation with Terraform
1. **VPC Setup**
   - Created a Virtual Private Cloud (VPC) to serve as the foundational network for the infrastructure.

2. **Subnets and Networking**
   - Configured private and public subnets within the VPC.
   - Associated each subnet with its respective security groups and route tables.

3. **Elastic Load Balancer (ELB)**
   - Set up an ELB to distribute incoming requests evenly across all subnets for improved reliability and performance.

4. **Route 53 Configuration**
   - Configured Route 53 for DNS resolution, enabling access to VPC resources via a domain name instead of direct IP addresses.

## Part 2: AWS Services Listing by Region (using AWS API and boto3)
- List all relevant AWS resources across each region, including:
  - **EC2** (Elastic Compute Cloud)
  - **RDS** (Relational Database Service)
  - **S3** (Simple Storage Service)
  - **ELB** (Elastic Load Balancer)


## Setup:

1. **Terraform setup**

    Download Terraform from the original website
    https://developer.hashicorp.com/terraform/downloads

2. **Navigate to the Project Directory:**
   ```bash
   cd acme-devops-project
   ```

3. **Clone the Repository:**

   ```bash
   git clone git@github.com:Saroni0504/acme-devops-project.git
   ```

4. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

5. **Activate the Virtual Environment:**
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    - **Windows:**
        ```bash
        venv\Scripts\activate
        ```

6. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

7. **AWS Key and Secret**

    Create an AWS account, generate AWS key and secret key. Then, define environment variables.

    - **macOS/Linux:**
        ```bash
        export AWS_ACCESS_KEY_ID=aws_access_key_id
        export AWS_SECRET_ACCESS_KEY=aws_secret_access_key
        export AWS_REGION=aws_region
        ```

    - **Windows:**
        ```bash
        $env:AWS_ACCESS_KEY_ID = "aws_access_key_id"
        $env:AWS_SECRET_ACCESS_KEY = "aws_secret_access_key"
        $env:AWS_REGION = "aws_region"
        ```

8. **Initialize Terraform**
   ```bash
   terraform init
   ```

9. **Create resources**
   ```bash
   terraform apply
   ```

9. **Run main.py**
   ```bash
   python main.py
   ```

11. **Profit!**
