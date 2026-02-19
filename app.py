from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps CI/CD Application is running successfully!"

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        service="devops-cicd-app",
        time=str(datetime.datetime.now())
    )

@app.route("/version")
def version():
    return jsonify(
        version="1.0.0",
        environment="CI/CD Demo",
        host=socket.gethostname()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
