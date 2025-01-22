from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "yourapikey"  # Replace with your OpenAI API key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    try:
        user_message = request.json.get("message")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if you don't have GPT-4 access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_response = response['choices'][0]['message']['content']
        return jsonify({"response": assistant_response})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
