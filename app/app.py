from flask import Flask, render_template, request
import subprocess
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping", methods=["POST"])
def ping():
    host = request.form.get("host", "")

    # ✅ validation simple
    if not re.match(r"^[a-zA-Z0-9.\-]+$", host):
        return "Invalid host", 400

    # ✅ no shell=True
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
