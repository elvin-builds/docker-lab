from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

def get_db():
    return psycopg2.connect(
        host='db',
        database='devops',
        user='postgres',
        password=os.environ.get('DB_PASSWORD', 'secret123')
    )

@app.route('/')
def home():
    cache.incr('visits')
    count = cache.get('visits').decode('utf-8')
    return f"Ziyaretci sayi: {count}"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

