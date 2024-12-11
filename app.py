from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key="AIzaSyDHXjg_HPToDno9hGqBn0j13j37nQSqbFI")
model = genai.GenerativeModel("gemini-1.5-flash")

conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    conversation_history.append(user_input)
    prompt = "\n".join(conversation_history)
    
    response = model.generate_content(prompt)
    conversation_history.append(response.text)

    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)