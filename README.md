🏦 Bankproject: End-to-End CI/CD Pipeline
This project demonstrates a full DevOps lifecycle: from local development to a containerized deployment on AWS EC2, integrated with an AWS RDS PostgreSQL database via Jenkins.

🏗 Architecture Overview
Local Development: Code is pushed to GitHub.

CI/CD (Jenkins): Jenkins triggers a build, pulls the code, and builds a Docker image.

Security (Vault): Database credentials are securely pulled from Jenkins Credentials.

Database (RDS): Jenkins verifies connectivity to the PostgreSQL instance.

Deployment (Docker): The old container is replaced by a new one with a restart: always policy.

🚀 Deployment Workflow
1. AWS Infrastructure Setup
EC2 Instance: Ubuntu 24.04 LTS, t2.micro.

Security Group: Ports 22 (SSH), 8080 (Jenkins), and 8000 (App) open to My IP.

RDS Database: PostgreSQL 17.

Security Group: Port 5432 open only to the EC2 Security Group ID.

2. Jenkins Configuration
Credentials: Added Secret Text with ID RDS_DB_PASSWORD.

Tools Installed: Docker, Java 17, Jenkins, and postgresql-client.

💻 Essential Commands
☁️ Connecting to Infrastructure
Bash
# Connect to EC2
ssh -i bank-key.pem ubuntu@<EC2_IP>

# Check if the app is running
docker ps

# Check the Auto-Restart policy
docker inspect bank-app | grep RestartPolicy -A 3
🗄️ Database Management (Direct Access)
To verify your bank data manually from the EC2 terminal:

Bash
# Connect to the project database
PGPASSWORD=$DB_PASSWORD psql -h <RDS_ENDPOINT> -U postgres -d bankdb

# Useful SQL Commands:
\dt                  # List all tables
SELECT * FROM users;  # View customer data
\q                   # Exit PostgreSQL
🛠 Jenkins Pipeline (The "Engine")
The Jenkinsfile automates the following stages:

Build: docker build -t bankproject:latest .

Security Check: Verifies RDS connection using withCredentials.

Deploy:

Stops old container: docker rm -f bank-app || true

Starts new container: docker run -d -p 8000:8000 --restart always --name bank-app bankproject:latest

🔒 Security Best Practices Implemented
✅ No Hardcoded Passwords: Used Jenkins Secret Text for RDS credentials.

✅ Security Group Isolation: RDS is not public; it only accepts traffic from the EC2.

✅ Auto-Healing: Docker containers are set to restart: always to survive server reboots.

# Bank Application Project(local on docker hub)

This is a Django-based bank application containerized using Docker for consistent deployment across environments.

## 🚀 Quick Start (Running via Docker Hub)
If you have Docker installed, you don't even need to download the source code. Simply run:

```bash
docker run -d -p 8000:8000 --name running-bank-app harshinishashank/bank-app:v1
Last Updated: Mon Apr  6 20:31:04 UTC 2026
