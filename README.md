# ACME Devops Project

## Overview

The assignment is divided into two parts: 
1. Create AWS objects using Terraform 
2. List AWS services by region using AWS API (boto3)



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
