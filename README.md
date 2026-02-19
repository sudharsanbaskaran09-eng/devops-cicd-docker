# CI/CD Pipeline using GitHub Actions and Docker

This project demonstrates a Continuous Integration (CI) pipeline implemented using GitHub Actions and Docker. The objective of this project is to automate the process of building a Docker image whenever code is pushed to the GitHub repository, following real-world DevOps practices.

The application is a simple Python Flask web service that is containerized using Docker. GitHub Actions is configured to automatically trigger a workflow on every push to the main branch, where the source code is checked out and a Docker image is built. This ensures consistent builds, early detection of issues, and reduced manual effort.

Technologies used in this project include Python (Flask) for the application, Docker for containerization, GitHub Actions for CI automation, Git for version control, and GitHub for source code hosting.

Project structure:
devops-cicd-docker/
app.py
requirements.txt
Dockerfile
README.md
.github/workflows/ci.yml

CI pipeline working flow: A developer pushes code to the main branch of the GitHub repository. This triggers the GitHub Actions workflow defined in the ci.yml file. The workflow checks out the repository and builds a Docker image using the Dockerfile. The build status is displayed in the GitHub Actions dashboard, indicating success or failure.

To run the application locally, first build the Docker image using the command: docker build -t devops-cicd-app . Then run the container using: docker run -p 5000:5000 devops-cicd-app. Once the container is running, the application can be accessed in a browser at http://localhost:5000.

The CI pipeline configuration is located in the .github/workflows/ci.yml file and is automatically executed on every push to the main branch.

Through this project, key learnings include writing Dockerfiles, building and running Docker containers, setting up CI pipelines using GitHub Actions, understanding automated build workflows, and gaining hands-on experience with real-world DevOps CI practices.

Resume point: Implemented a CI pipeline using GitHub Actions and Docker to automatically build Docker images on every code push.
