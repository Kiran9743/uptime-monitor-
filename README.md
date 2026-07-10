# Uptime Monitor MVP

## Run
```bash
docker compose up --build
```

Open:
- Frontend: http://localhost:5173
- Backend: http://localhost:8000/docs

## Test
POST /urls
- https://example.com
- https://this-domain-does-not-exist-123456.com

Verify one URL is UP and one is DOWN.

## Deployment Sketch
Deploy on a single EC2 instance behind an ALB using Docker Compose.
