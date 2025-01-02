#!/usr/bin/env python3
import os
from flask import Flask, render_template, request

from util import openai as gpt

app = Flask(__name__)
chat_client, role, gpt_chat_model = gpt.get_chat_client()
audio_client, gpt_audio_model = gpt.get_audio_client()

"""
Routes for the GPT chat service.
"""
@app.route('/')
def chat_index():
    return render_template('chat.html')
# end def: chat_index

@app.route('/chat', methods = ['POST'])
def chat():
    prompt = request.json['prompt']
    response = chat_client.chat.completions.create(
        messages = [
            {
                'role': role,
                'content': prompt
            }
        ],
        model = gpt_chat_model,
    )
    chatgpt = response.choices[0].message.content
    token_cost = response.usage.total_tokens

    return {
        'response': chatgpt,
        'tokens': token_cost,
    }
# end def: chat

"""
Routes for the GPT whisper (audio transcriber) service.
"""
@app.route('/transcribe', methods=['GET'])
def transcribe_index():
    return render_template('whisper.html')
# end def: transcribe_index

@app.route('/transcribe', methods = ['POST'])
def transcribe():
    if 'audio_file' not in request.files:
        return render_template('whisper.html', error = "No audio file provided.")

    audio_file = request.files['audio_file']
    audio_lang = request.form['audio_lang'] if 'audio_lang' in request.form else 'en'

    if audio_file.filename == '':
        return render_template('whisper.html', error = "Empty audio file provided.")

    audio_path = os.path.join('/tmp', audio_file.filename)
    audio_file.save(audio_path)

    try:
        with open(audio_path, 'rb') as f:
            text = audio_client.audio.transcriptions.create(
                file = f,
                language = audio_lang,
                model = gpt_audio_model,
                response_format = 'text'
            )
            #print(text)
    except Exception as e:
        return render_template('whisper.html', error = str(e))

    os.remove(audio_path)

    return render_template('whisper.html', audio_text = text)
# end def: transcribe

if __name__ == '__main__':
    app.run(debug = bool(os.getenv('GPT_DEBUG', False)))
# end if: __name__
