# 🏦 BankProject - CI/CD & Cloud Infrastructure

A full-stack banking application deployed on **AWS EC2** using a modern DevOps pipeline. This project demonstrates automated deployment, reverse proxy configuration, and real-time system monitoring.

## 🏗️ Architecture Overview
* **Cloud Provider:** AWS (EC2 t3.micro)
* **Database:** AWS RDS (PostgreSQL)
* **Containerization:** Docker
* **Web Server:** Nginx (Reverse Proxy)
* **CI/CD Pipeline:** Jenkins (GitHub Webhooks)
* **Monitoring:** Netdata

---

## 🚀 Deployment Pipeline
The project utilizes a **Jenkinsfile** pipeline that automates the following stages:
1.  **Build:** Generates a Docker image from the source code.
2.  **Test:** Verifies connectivity to the AWS RDS instance.
3.  **Deploy:** * Removes existing containers to prevent conflicts.
    * Deploys the new container with resource limits (`--memory=512m`, `--cpus=0.5`).
    * Ensures high availability with `--restart always`.

---

## 🌐 Web Server & Security
The application is served via **Nginx** acting as a reverse proxy.
* **Public Access:** Port 80 (HTTP)
* **Internal Routing:** Nginx forwards traffic to the Docker container on port 8000.
* **Security:** Public access to port 8000 is blocked at the AWS Security Group level, forcing all traffic through the Nginx layer for better security.

---

## 📊 Monitoring
Real-time infrastructure and container health are tracked via **Netdata**.
* **URL:** `http://<EC2-IP>:19999`
* **Metrics:** CPU utilization, RAM usage, and per-container statistics for the `bank-app`.

---

## 🛠️ Local Setup & Commands
To run this application locally using Docker:

```bash
# Build the image
docker build -t bankproject .

# Run the container
docker run -d -p 8000:8000 --name bank-app bankproject


