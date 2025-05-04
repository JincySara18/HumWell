# app.py — using Gemini 1.5 Pro Latest
# added by jincy on 13-11-2023
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as palm
import traceback

app = Flask(__name__)
CORS(app)


palm.configure(api_key="AIzaSyDeFj6s8wcOP_LwXzuKJAtB55kSb9PjxQw")
#palm.configure(api_key="AIzaSyAQ31sOr3lDaVR_5Eo1IZCsvFhVanvUwaY")


model = palm.GenerativeModel("models/gemini-1.5-pro-latest")

@app.route('/chatbox', methods=['POST'])
def handle_chatbox_input():
    user_input = request.get_json().get('input', '')
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        print("Gemini Error Traceback:")
        traceback.print_exc()
        reply = f"Gemini error: {e}"

    return jsonify({'output': reply})

if __name__ == '__main__':
    app.run(debug=True)
