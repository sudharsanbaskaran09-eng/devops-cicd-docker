# CI/CD Pipeline with GitHub Actions and Docker

## Overview
This project implements a Continuous Integration (CI) pipeline using GitHub Actions and Docker. The pipeline automatically builds a Docker image whenever code is pushed to the main branch of the GitHub repository. The goal of this project is to demonstrate practical DevOps automation used in real-world software delivery workflows.

The application is containerized using Docker, ensuring consistent builds and environment parity. GitHub Actions is used as the CI tool to automate the build process and validate integration on every code change.

---

## Objectives
- Implement an automated CI pipeline
- Containerize an application using Docker
- Trigger automated builds on every Git push
- Follow real-world DevOps CI best practices
- Gain hands-on experience with GitHub Actions workflows

---

## Technologies Used
- Python (Flask) – Sample web application
- Docker – Containerization
- GitHub Actions – Continuous Integration
- Git – Version control
- GitHub – Source code management

---

## Architecture
Developer Commit
|
v
GitHub Repository
|
v
GitHub Actions CI Workflow
|
v
Docker Image Build

---

## Project Structure
devops-cicd-docker/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
└── workflows/
└── ci.yml

---

## CI Pipeline Workflow
1. Developer pushes code to the `main` branch
2. GitHub Actions workflow is triggered automatically
3. The workflow checks out the source code
4. Docker image is built using the Dockerfile
5. Build status is reported in the GitHub Actions dashboard

---

## Running the Application Locally

### Build the Docker Image
```bash
docker build -t devops-cicd-app .
docker run -p 5000:5000 devops-cicd-app
http://localhost:5000
.github/workflows/ci.yml




