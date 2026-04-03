#LockPad

LockPad is a secure note-sharing web application built to demonstrate a complete
end-to-end DevOps workflow. The project focuses on infrastructure automation,
continuous deployment, secure configuration management, and production-grade
application deployment on AWS.

---

## Project Overview

The application allows users to access encrypted notes using a key. The system
is designed with a static frontend, a REST-based backend, and a managed database.
All infrastructure and deployments are fully automated.

This repository serves as a practical demonstration of real-world DevOps
engineering practices rather than just application development.

---

## Architecture

User requests flow through the following components:

- Frontend hosted as a static website on Amazon S3
- Reverse proxy and HTTPS handled by Caddy
- Backend API served by Django using Gunicorn
- MongoDB Atlas used as a managed database service
- DNS configured using a custom domain
- Infrastructure provisioned using Terraform
- Configuration and application setup managed using Ansible
- CI/CD pipeline implemented using GitHub Actions

---

## Technology Stack

### Backend
- Python
- Django
- Django REST Framework
- Gunicorn
- Fernet encryption

### Frontend
- HTML
- CSS
- JavaScript

### Infrastructure and DevOps
- AWS EC2
- AWS S3
- Terraform
- Ansible
- GitHub Actions
- Caddy
- MongoDB Atlas

---

## Deployment Workflow

1. Infrastructure is provisioned using Terraform.
2. Terraform outputs are passed to the CI pipeline.
3. Frontend files are uploaded to Amazon S3.
4. Ansible configures the EC2 instance:
   - Installs dependencies
   - Clones the repository
   - Creates environment configuration files
   - Configures Gunicorn and Caddy
5. Services are restarted and the application is deployed.
6. The application is accessible via a custom HTTPS domain.

---

## Configuration and Secrets Management

Sensitive values such as database credentials, encryption keys, and Django
settings are managed using GitHub Actions secrets. These secrets are injected
into the EC2 instance during deployment using Ansible and stored securely as
environment variables.

No secrets are committed to the repository.

---

## Cost Considerations

The infrastructure is designed to be cost-efficient and suitable for learning
and portfolio demonstration purposes. Services are kept minimal to avoid
unnecessary cloud expenditure while still reflecting real production patterns.

---

## Author

Charan Sai Ramisetti
