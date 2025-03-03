# Installation Guide

## Prerequisites

Before running the application, ensure you have the following:

### Required Services and Subscriptions

- **OpenAI API Key**: Required for DALL-E image generation
- **Oracle Cloud Infrastructure (OCI) Account**: 
  - Needed for image storage in the `generative_images` bucket
  - Configure OCI credentials (Access Key ID and Secret Access Key)
  - Set up an OCI Object Storage bucket named `generative_images`

### Software Requirements

- Python 3.9.2
- Node.js 22.13.1
- MySQL 8.0 or later
- Docker and Docker Compose (for containerized deployment)

# Local Development
Download and install Python version 3.9.2, you can find it [HERE](https://www.python.org/downloads/release/python-392/).

Install poetry:
```bash
pip install poetry==2.0.1
```

Install Node & pnpm:
```bash
winget install Schniz.fnm # restart shell
fnm install 22.13.1 # restart shell
node -v # if it doesn't work, add it to PATH
npm -v
npm install -g pnpm
```

## Set up environment variables
Create `.env` files in each service directory with the required environment variables (you can start from `env.example`):
```yaml
# For chat_service/.env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=app_user
MYSQL_PASSWORD=app_password
MYSQL_DB=chainlit_db
OPENAI_API_KEY=your_openai_api_key
CHAINLIT_AUTH_SECRET=your_auth_secret
# Add other required variables
```

Repeat this process for each service directory.

## Chat Service

### Installation
```bash
cd chat_service
poetry install --no-root
```

### Run
```bash
poetry shell
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Round Manager Service

### Installation
```bash
cd round_manager_service
poetry install --no-root
```

### Run
```bash
poetry shell
uvicorn app:app --host 0.0.0.0 --port 8001
```

## Admin Service

### Installation
```bash
cd admin_service
poetry install --no-root
```

### Run
```bash
poetry shell
uvicorn app:app --host 0.0.0.0 --port 8002
```

## User Interface

### Installation
```bash
cd user_interface
pnpm install
pnpm buildUi
```

### Run
```bash
cd app
pnpm dev --port 5174
```

## Admin Interface

### Installation
```bash
cd admin_interface
poetry install --no-root
```

### Run
```bash
poetry shell
streamlit run app.py
```

# Docker Compose

## Set up environment variables
Create `.env-docker` files in each service directory with the required environment variables (you can start from env.example):
```yaml
   # For chat_service/.env-docker
   MYSQL_HOST=database_service
   MYSQL_PORT=3306
   MYSQL_USER=app_user
   MYSQL_PASSWORD=app_password
   MYSQL_DB=chainlit_db
   OPENAI_API_KEY=your_openai_api_key
   CHAINLIT_AUTH_SECRET=your_auth_secret
   # Add other required variables
```

Repeat this process for each service directory.

## Build and Launch
Build each component and launch it:
```bash
docker-compose up --build
```

## Access the application
- User Interface: `http://localhost:3000`
- Admin Interface: `http://localhost:8501`
