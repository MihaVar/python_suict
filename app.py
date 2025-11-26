from flask import Flask, jsonify
import time
import logging
import socket

STATSD_HOST = "127.0.0.1"
STATSD_PORT = 9999

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def send_statsd(message: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode("utf-8"), (STATSD_HOST, STATSD_PORT))
    sock.close()

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
    try:
        x = 1 / 0
        return str(x)
    except Exception:
        logging.exception("Сталася помилка у маршруті /error")
        send_statsd("error: ZeroDivisionError")
        return "Сталася помилка!", 500


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
