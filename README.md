# FastAPI Microservices Architecture 🚀  

This repository contains a **microservices-based architecture** built using python **FastAPI** framework, with separate services for users and tasks. It integrates **Docker**, **Jenkins**, **Git**, and **DockerHub** for CI/CD.  

## 🛠️ Tech Stack  

- **FastAPI** – Python web framework  
- **SQLite / PostgreSQL** – Database (configurable)  
- **Docker** – Containerization  
- **DockerHub** – Image registry  
- **Jenkins** – CI/CD pipeline  
- **Pytest** – Testing  

## 🚀 Features  

- ✅ Two microservices: **User** & **Task**  
- ✅ REST API endpoints with **FastAPI**  
- ✅ Dockerized microservices  
- ✅ Jenkins pipeline to build & push images to **DockerHub**  
- ✅ Unit tests with **Pytest**  

## ⚙️ Running Locally  

### 1️⃣ Clone the Repository  
git clone https://github.com/sachinkiet/fastapi-microservice-docker-jenkins.git
cd fastapi-microservice-docker-jenkins

## Build and Start Containers
docker compose up --build

**Access Services**
Task Service → http://<localhost **/** ip-address>:8001
User Service → http://<localhost **/** ip-address>:8002

## Run Test manually->
pytest

## Microservice Endpoints  

### Task Service  

| Method | Endpoint          | Description                                |
|--------|-------------------|--------------------------------------------|
| GET    | `/`               | Welcome to the Task Service                |
| GET    | `/callme`         | Called from another service                |
| POST   | `/tasks/`         | Create a new task                          |
| GET    | `/tasks/{task_id}`| Get task by ID                             |

### User Service  

| Method | Endpoint                 | Description                                |
|--------|--------------------------|--------------------------------------------|
| GET    | `/`                      | Welcome to the User Service                |
| GET    | `/call-task-service`     | Calls Task Service from User Service       |
| POST   | `/user/`                 | Create a new user                          |
| GET    | `/user/{user_id}`        | Get user by ID                             |


