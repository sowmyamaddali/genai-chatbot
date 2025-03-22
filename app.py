# app.py
import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
HPI_API_KEY = os.getenv("HPI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]

    # Hugging Face Inference API endpoint
    API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-small"
    headers = {
        "Authorization": f"Beater {os.getenv('HF_API_KEY')}"
    }

    payload = {
        "inputs": user_input
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            ai_reply = result[0]["generated_text"]
        
        elif "error" in result:
            ai_reply = f"Error: {result['error']}"
        
        else:
            ai_reply = "Unexpected response from Hugging Face."
    
    except Exception as e:
        ai_reply = f"Failed to parse response: {str(e)}"
    
    return jsonify({"response": ai_reply})


    # return jsonify({"response" : f"You said: {user_input}"})

#if __name__ == "__main__":
#    app.run(debug=True)