import os
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route("/")
def home():
    return "Hello from my Kubernetes app!"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/visits")
def visits():
    count = cache.incr('visit_count')
    return {"total_visits": count}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
