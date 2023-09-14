import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

test_messages = []


def chatbot_response(user_message):
    test_messages.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::7yJAKiCC", messages=test_messages, temperature=0, max_tokens=500
    )
    test_messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    return response["choices"][0]["message"]["content"]


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run()