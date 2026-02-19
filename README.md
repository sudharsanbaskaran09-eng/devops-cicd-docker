## Project: CI/CD Pipeline with GitHub Actions and Docker

This project demonstrates a Continuous Integration (CI) pipeline that automatically builds a Docker image whenever code is pushed to a GitHub repository. The pipeline follows real-world DevOps practices to automate builds and ensure consistent application integration.

### Features
- Automated CI pipeline triggered on GitHub push
- Dockerized Python Flask application
- Consistent and repeatable builds
- Early detection of build issues
- No manual build process required

### Application Details
The application is a simple Python Flask web service exposed on port 5000 and containerized using Docker for portability and consistency.

### CI Pipeline Flow
- Developer pushes code to the `main` branch
- GitHub Actions workflow is triggered automatically
- Source code is checked out
- Docker image is built using the Dockerfile
- Build result is displayed in the GitHub Actions dashboard

### Tools and Technologies Used
- Python (Flask)
- Docker
- GitHub Actions
- Git
- GitHub

### Project Structure
- app.py – Flask application
- Dockerfile – Docker image configuration
- requirements.txt – Application dependencies
- .github/workflows/ci.yml – CI pipeline definition

### Local Testing
- Docker image built and run locally
- Application accessed via `http://localhost:5000`
- Verified successful container execution

### Validation
- Successful Docker image build on every push
- CI workflow execution verified with GitHub Actions
- Green build status confirms pipeline success

### Status
Completed ✅
