from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.route("/")
def home():
    return "<h1>Hello world!</h1>"

@app.route("/items")
def items():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO items (name) VALUES ('sample item');")
    conn.commit()

    cur.execute("SELECT * FROM items;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", 5000)))
