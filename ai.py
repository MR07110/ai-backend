import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# DIQQAT: API kalitni kodga yozmaymiz, uni Render'dan olamiz
API_KEY = os.environ.get("GROQ_API_KEY") 
client = Groq(api_key=API_KEY)

@app.route('/')
def home():
    return "Backend xavfsiz ishlayapti! 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        user_code = data.get("code", "")

        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Sen aqlli AI san."},
                {"role": "user", "content": user_code}
            ],
            model="llama-3.3-70b-versatile",
        )
        return jsonify({"analysis": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
