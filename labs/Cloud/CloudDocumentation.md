# **☁️ Cloud Session Documentation**

## **🔹 Introduction to Cloud Computing**

### **What is Cloud Computing?**
Cloud computing is a technology that allows businesses and individuals to access computing resources **on demand** via the internet instead of owning physical hardware. This approach is **scalable, cost-efficient, and flexible**.

🔹 **Traditional vs. Cloud Computing**
- Before cloud computing, businesses had to buy and maintain expensive servers.
- Cloud computing eliminates this by providing **on-demand infrastructure**.
- Examples: **AWS, Google Cloud, Azure**.

🔗 **Resources to Learn More About Cloud:**
🎥 [AWS Cloud Practitioner Course](https://youtube.com/playlist?list=PLluZGtIpwF_B6IHB6q1pG8AJAIvpJHNIH&si=EmSx8rO6C5L01p57)  
🎥 [AWS Cloud Practitioner Deep Dive](https://youtube.com/playlist?list=PLJZLxa-J0VZSEVmKS8HQQoi09yB6IHigK&si=f8vSRt2ANdwqNfj6)  
📜 [AWS Official Documentation](https://docs.aws.amazon.com/)  

---

## **☁️ 1. Cloud Service Models**
Cloud computing is divided into different **service models**:
- **IaaS (Infrastructure as a Service)** – Provides virtualized computing resources (e.g., AWS EC2, GCP Compute Engine).
- **PaaS (Platform as a Service)** – Provides a platform for developers to build applications without managing infrastructure (e.g., AWS Elastic Beanstalk).
- **SaaS (Software as a Service)** – Fully managed applications available over the internet (e.g., Gmail, Dropbox, Salesforce).

### **📌 Cloud Deployment Models**
- **Public Cloud** – Resources are shared among multiple users (e.g., AWS, Google Cloud).
- **Private Cloud** – Dedicated infrastructure for a single organization.
- **Hybrid Cloud** – Combination of both public and private clouds.

🔗 **Resources to Learn About Networks & Cloud:**
🎥 [Networking Fundamentals for Cloud](https://youtube.com/playlist?list=PLH-n8YK76vIiuIZoWvHL7AvtrDV7hR3He&si=QeugLvGIipvETGQq)  
🎥 [CCNA Deep Networking Course](https://youtube.com/playlist?list=PLoP_aS_FoPQfCHLDULY7wmjz3Qgp5f7il&si=B6uKDent9_jGUCZz)  

---

## **🛠️ 2. Infrastructure as Code (IaC) & Terraform**
### **What is Infrastructure as Code (IaC)?**
Infrastructure as Code (IaC) is a method of **automating infrastructure deployment using code** instead of manual setup. It allows consistency and version control for cloud environments.

### **What is Terraform?**
Terraform is an **open-source IaC tool** that enables you to define and manage cloud resources using configuration files.

🔗 **Resources to Learn Terraform:**
🎥 [Terraform Beginner Course](https://youtube.com/playlist?list=PLX1bW_GeBRhBIT9-Nyt4_osatqokaN8ae&si=2qvKGq5X_lOIYvNd)  
🎥 [Advanced Terraform Course](https://youtube.com/playlist?list=PLQ5OGqigB8Vnymd6CwskXgHFa-Ft_8Qm-&si=23Ns4mRcT1j-oRYe)  
📜 [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)  

---

## **🚀 Task 1: Creating an EC2 Instance on AWS**
### **📌 Steps to Follow:**
1️⃣ **Login to AWS Console**
- Sign in to your AWS account.
- Search for **EC2** and select it.

2️⃣ **Launch a New EC2 Instance**
- Click on **Launch Instance**.
- Enter a name for your instance.
- Choose **Amazon Linux 2023** (Free Tier eligible).
- Select **t2.micro or t3.micro** (Free Tier eligible).

3️⃣ **Create a New Key Pair**
- Click **Create New Key Pair**.
- Enter a name and choose **RSA key type**.
- Download the **.pem** file.

4️⃣ **Configure Network Settings**
- Select **default VPC**.
- Create a **new subnet**.
- Assign an **Availability Zone**.
- Enter a valid **CIDR block**.

5️⃣ **Configure Security Group**
- Create a **new security group**.
- Allow **HTTP (Port 80) from Anywhere**.

6️⃣ **Configure Storage**
- Keep **default 8 GB storage**.

7️⃣ **User Data (Optional Web Server Setup)**
```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello world from $(hostname -f)</h1>" > /var/www/html/index.html
```

8️⃣ **Launch the Instance & Verify**
- Click **Launch Instance**.
- Find the **Public IP** of the instance.
- Open `http://<public-ip>` in a browser.
✅ You should see: `Hello world from [hostname]`

---

## **📌 Task 2: Setting Up AWS Application Load Balancer (ALB)**
### **📌 Steps to Follow:**
1️⃣ **Launch Two EC2 Instances** (Use the same user data as Task 1).

2️⃣ **Verify the Instances**
- Copy the **Public IP** of each instance.
- Open them in a browser to check Apache is running.

3️⃣ **Create an ALB**
- Go to **EC2 → Load Balancers**.
- Click **Create Load Balancer**.
- Choose **Application Load Balancer**.
- Set **Scheme: Internet-facing**.
- Select **VPC & Availability Zones**.

4️⃣ **Configure Security Group**
- Allow **HTTP (Port 80) from Anywhere**.

5️⃣ **Create Target Group & Register Instances**
- Choose **Target Type: Instances**.
- Add both **EC2 Instances**.

6️⃣ **Complete ALB Setup & Test**
- Copy the **ALB DNS Name** from AWS.
- Open `http://<ALB-DNS-Name>` in a browser.
- Refresh to see traffic distributed between instances.

✅ **Now you have a working Load Balancer distributing traffic across EC2 instances!**

---

## **🎯 Final Summary**
✅ **Cloud computing enables scalable & cost-effective infrastructure.**  
✅ **AWS EC2 allows us to deploy virtual servers in minutes.**  
✅ **Application Load Balancer distributes traffic across multiple instances.**  
✅ **Terraform helps automate cloud infrastructure setup.**  

🚀 *"Now you have the foundation to deploy and manage cloud infrastructure!"* 🎯  

---