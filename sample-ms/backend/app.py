from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import os
import redis
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

redis_host = os.getenv("REDIS_HOST", "localhost")

@app.route('/data')
def get_data():
    r = redis.Redis(host=redis_host, port=6379)
    data = r.get("sample_data")
    if data is None:
        return jsonify({"error": "Data not found"}), 404
    return jsonify(json.loads(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
