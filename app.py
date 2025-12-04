from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello world!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", 5000)))
