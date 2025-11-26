from flask import Flask, jsonify
import time

app = Flask(__name__)

start_time = time.time()
request_count = 0


@app.before_request
def before_request():
    global request_count
    request_count += 1


@app.route("/")
def index():
    return "Сервіс працює"


if __name__ == "__main__":
    app.run(port=5000)
