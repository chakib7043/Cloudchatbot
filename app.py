from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["user_message"]
    bot_response = get_chatbot_response(user_message)
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

