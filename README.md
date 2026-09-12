# Task Manager

A complete, working Task Manager full-stack web application.

## Commands to Run

```bash
docker compose up -d --build
docker compose ps
docker compose logs
docker compose down
docker compose down -v
```

## Architecture

- **Frontend**: React SPA built with Vite. Exposed locally on port specified by `FRONTEND_PORT` (default `8081`).
- **Backend**: FastAPI Python application. Exposed locally on port specified by `BACKEND_PORT` (default `8000`).
- **Database**: MySQL (persistent).
- **Host Nginx**: The host machine's Nginx (`/etc/nginx/sites-available`) will act as the reverse proxy, routing traffic to the exposed containers.

## Request Flow

1. Browser requests `http://your-domain.com`. The request hits the **Host Nginx** (Reverse Proxy).
2. Host Nginx forwards `/` to the **React Frontend** container on `http://127.0.0.1:8081`.
3. API requests like `http://your-domain.com/api/tasks` hit the Host Nginx, which proxies them to the **FastAPI Backend** on `http://127.0.0.1:8000` (or your configured `BACKEND_PORT`).
4. The Backend communicates with the **MySQL Database** internally over the Docker network using SQLAlchemy.

## Sample Nginx Config (`/etc/nginx/sites-available/taskmanager`)

```nginx
server {
    listen 80;
    server_name your-domain.com; # Or your IP address

    location / {
        proxy_pass http://127.0.0.1:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /health {
        proxy_pass http://127.0.0.1:8000/health;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
