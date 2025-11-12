# 🐳 Docker Projects Collection

A comprehensive collection of Docker and Docker Compose examples demonstrating multi-container orchestration, web applications, databases, and automated deployment workflows.

## 📚 Table of Contents

- [Project 1: Multi-Container Application with Redis](#project-1-multi-container-application-with-redis)
- [Project 2: Simple Flask Web Application](#project-2-simple-flask-web-application)
- [Project 3: Web Server with PostgreSQL Database](#project-3-web-server-with-postgresql-database)
- [Project 4: Multiple Application Versions](#project-4-multiple-application-versions)
- [Project 5: Auto-Reload Development Environment](#project-5-auto-reload-development-environment)

---

## Project 1: Multi-Container Application with Redis

A Python application that increments a counter in Redis every 2 seconds, demonstrating container networking and service dependencies.

### 📁 Project Structure
```
myapp/
 ├─ app.py
 ├─ requirements.txt
 ├─ Dockerfile
 └─ docker-compose.yml
```

### 🚀 Quick Start
```bash
cd myapp
docker-compose up -d
```

### ✅ Verify Operation
```bash
docker-compose ps
docker-compose logs -f python-app
```

### 🛑 Stop Containers
```bash
docker-compose down
```

### 🔑 Key Features
- **Service Orchestration**: Demonstrates `depends_on` for startup order
- **Custom Networks**: Isolated bridge network for inter-container communication
- **Redis Integration**: Shows how to connect Python application to Redis database

---

## Project 2: Simple Flask Web Application

A minimal Flask web server containerized with Docker, perfect for understanding basic containerization concepts.

### 📁 Project Structure
```
simple-flask/
 ├─ app.py
 ├─ requirements.txt
 └─ Dockerfile
```

### 🚀 Quick Start
```bash
# Build the image
docker build -t my-python-app .

# Run the container
docker run -d -p 5000:5000 --name my-python-app-container my-python-app
```

### ✅ Test the Application
Open your browser and navigate to:
```
http://localhost:5000
```

You should see: **"Hello from Docker!"**

### 🔑 Key Features
- **Lightweight**: Uses Python 3.12-slim base image
- **Port Mapping**: Exposes Flask on port 5000
- **Single Container**: Simple deployment model

---

## Project 3: Web Server with PostgreSQL Database

A full-stack application with Flask web server and PostgreSQL database, demonstrating multi-tier architecture.

### 📁 Project Structure
```
myapp/
 ├─ app.py
 ├─ requirements.txt
 ├─ Dockerfile
 └─ docker-compose.yml
```

### 🚀 Quick Start
```bash
cd myapp
docker compose up -d
```

### ✅ Test the Application
Visit in your browser:
```
http://localhost:5000
```

You'll see the current database time fetched from PostgreSQL.

### 🔑 Key Features
- **Multi-Tier Architecture**: Separate web and database services
- **Environment Variables**: Configuration through environment variables
- **Persistent Storage**: PostgreSQL data stored in Docker volume
- **Health Checks**: `depends_on` ensures database starts before web server

### 📊 Architecture
```
┌─────────────┐         ┌──────────────┐
│   Web App   │────────▶│  PostgreSQL  │
│  (Flask)    │         │   Database   │
│  Port 5000  │         │              │
└─────────────┘         └──────────────┘
```

---

## Project 4: Multiple Application Versions

Deploy multiple versions of the same application simultaneously, useful for A/B testing or gradual rollouts.

### 📁 Project Structure
```
myapp_versions/
 ├─ app_v1.py
 ├─ app_v2.py
 ├─ requirements.txt
 ├─ Dockerfile
 └─ docker-compose.yml
```

### 🚀 Quick Start
```bash
cd myapp_versions
docker compose up -d --build
```

### ✅ Test Both Versions
**Version 1:**
```
http://localhost:5001
```
→ "Hello from App Version 1!"

**Version 2:**
```
http://localhost:5002
```
→ "Hello from App Version 2!"

### 🔑 Key Features
- **Build Arguments**: Uses Docker ARG to select application version
- **Parallel Deployment**: Both versions run simultaneously
- **Port Differentiation**: Each version exposed on different port
- **Blue-Green Deployment**: Foundation for zero-downtime deployments

---

## Project 5: Auto-Reload Development Environment

A development setup with automatic code reloading, eliminating the need to rebuild containers during development.

### 📁 Project Structure
```
myapp_autoreload/
 ├─ app.py
 ├─ requirements.txt
 ├─ Dockerfile
 └─ docker-compose.yml
```

### 🚀 Quick Start
```bash
cd myapp_autoreload
docker compose up
```

### ✅ Test Auto-Reload
1. Open browser: `http://localhost:5000`
2. Edit `app.py` and change the return message
3. Save the file
4. Refresh browser - see changes immediately!

### 🔑 Key Features
- **Volume Mounting**: Local code mounted into container
- **Flask Debug Mode**: Automatic server restart on code changes
- **Fast Iteration**: No container rebuild needed
- **Development Workflow**: Optimized for rapid development cycles

### 💡 Development Tips
- Flask's debug mode automatically detects file changes
- Changes to `requirements.txt` still require container rebuild
- Use `Ctrl+C` to stop the containers gracefully

---

## 📖 Common Commands

### Docker Compose
```bash
# Start services
docker compose up -d

# View logs
docker compose logs -f [service-name]

# Stop services
docker compose down

# Rebuild services
docker compose up -d --build

# View running containers
docker compose ps
```

### Docker
```bash
# List containers
docker ps -a

# View logs
docker logs [container-name]

# Execute command in container
docker exec -it [container-name] bash

# Remove container
docker rm [container-name]

# Remove image
docker rmi [image-name]
```

## 🔒 Security Notes

- Never commit secrets or passwords to version control
- Use `.env` files for sensitive configuration (add to `.gitignore`)
- Update base images regularly for security patches
- Use specific version tags instead of `latest` in production

**Happy Dockerizing! 🐳**
