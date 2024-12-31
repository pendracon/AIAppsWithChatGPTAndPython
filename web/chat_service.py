#!/usr/bin/env python3
import os
from flask import Flask, jsonify, render_template, request

from util import openai as gpt

app = Flask(__name__)
client, role, gpt_model = gpt.get_chat_client()

@app.route('/')
def index():
    return render_template('index.html')
# end def: index

@app.route('/chat', methods = ['POST'])
def chat():
    prompt = request.json['prompt']
    response = client.chat.completions.create(
        messages = [
            {
                'role': role,
                'content': prompt
            }
        ],
        model = gpt_model,
    )
    chatgpt = response.choices[0].message.content
    token_cost = response.usage.total_tokens
    return jsonify({
        'response': chatgpt,
        'tokens': token_cost,
    })
# end def: chat

if __name__ == '__main__':
    app.run(debug = bool(os.getenv('GPT_DEBUG', False)))
# end if: __name__
