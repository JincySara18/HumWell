# my_script.py
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Allow requests from your HTML page

@app.route('/chatbox', methods=['POST'])
def handle_chatbox_input():
    user_input = request.get_json().get('input', '')
    
    try:
        output = subprocess.check_output(
            ['python', 'your_script.py', user_input],
            stderr=subprocess.STDOUT
        )
        reply = output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        reply = f"Error: {e.output.decode('utf-8')}"
    
    return jsonify({'output': reply})

if __name__ == '__main__':
    app.run(debug=True)
"""

# test_response.py
# Simple Gemini API test script for generating a single response

import google.generativeai as palm
import traceback

# TODO: Replace with your actual key
API_KEY = "AIzaSyDeFj6s8wcOP_LwXzuKJAtB55kSb9PjxQw"

# Configure the API key
palm.configure(api_key=API_KEY)

try:
    # Select the correct Gemini model
    model = palm.GenerativeModel("models/gemini-1.5-pro-latest")

    # Prompt for response
    user_prompt = "Give me a mindfulness quote"
    print(f"\n🧠 Prompting Gemini with: {user_prompt}")

    # Generate content
    response = model.generate_content(user_prompt)

    print("\n✅ Gemini Response:")
    print(response.text)

except Exception as e:
    print("\n❌ Error communicating with Gemini:")
    traceback.print_exc()
