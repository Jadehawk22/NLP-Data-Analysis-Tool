from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=data['message'],
            max_tokens=150
        )
        return jsonify({"response": response.choices[0].text.strip()})
    except openai.error.OpenAIError as e:
        app.logger.error(f"OpenAI error: {e}")
        return jsonify({"error": "Error processing your request."}), 500

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True)
