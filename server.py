from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mini ilova uchun

user_scores = {}

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    user_id = data["user_id"]
    score = data["score"]
    user_scores[user_id] = score
    return {"status": "ok"}

@app.route("/")
def index():
    return open("webapp/index.html").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
