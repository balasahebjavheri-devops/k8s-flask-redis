# Flask + Redis on Kubernetes

A Flask application with a Redis-backed visit counter, deployed on Kubernetes using Deployments and Services.

## Tech Stack
Python, Flask, Redis, Docker, Kubernetes (Minikube)

## Architecture
- `redis-deployment.yaml` / `redis-service.yaml` — Redis, exposed internally as a ClusterIP Service (`redis-service`)
- `flask-deployment.yaml` / `flask-service.yaml` — 3 replicas of the Flask app, exposed externally as a NodePort Service

The Flask app connects to Redis using Kubernetes' internal DNS (`redis-service`), with no hardcoded IPs.

## Routes
- `/` — welcome message
- `/health` — health check
- `/visits` — increments and returns a visit counter stored in Redis

## Deploy
\`\`\`bash
minikube image build -t k8s-flask-redis:latest .
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
\`\`\`

## Test
\`\`\`bash
curl $(minikube ip):30090/visits
\`\`\`
