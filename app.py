# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    return jsonify({"response" : f"You said: {user_input}"})

if __name__ == "__main__":
    app.run(debug=True)