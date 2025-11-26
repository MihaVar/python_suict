from flask import Flask, jsonify
import time
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

app = Flask(__name__)

start_time = time.time()
request_count = 0


@app.before_request
def before_request():
    global request_count
    request_count += 1


@app.route("/")
def index():
    logging.info("Запит на /")
    return "Сервіс працює"


@app.route("/error")
def error():
    logging.warning("Запит на /error — буде згенерована помилка")
    x = 1 / 0
    return str(x)


@app.route("/status")
def status():
    logging.info("Запит на /status")
    uptime = time.time() - start_time
    return jsonify({
        "uptime_seconds": round(uptime, 2),
        "requests": request_count
    })


if __name__ == "__main__":
    app.run(port=5000)
