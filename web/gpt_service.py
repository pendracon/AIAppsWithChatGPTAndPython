#!/usr/bin/env python3
import os
from flask import Flask, render_template, request

from util import openai as gpt

app = Flask(__name__)
chat_client, role, gpt_chat_model = gpt.get_chat_client()
audio_client, gpt_audio_model = gpt.get_audio_client()
image_client, gpt_image_model = gpt.get_image_client()

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
Routes for the GPT Whisper (audio transcriber) service.
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

"""
Routes for the GPT DALL-E (image generator) service.
"""
@app.route('/image', methods=['GET'])
def image_gen_index():
    return render_template('dalle.html', model = gpt_image_model.lower())
# end def: image_gen_index

@app.route('/image', methods = ['POST'])
def image_gen():
    image_model = gpt_image_model.lower()
    description = request.form['prompt']
    img_size = request.form['image_size']
    count = int(request.form['num_images']) if 'num_images' in request.form else 1
    try:
        response = image_client.images.generate(
            prompt = description,
            n = count,
            size = img_size,
            model = gpt_image_model,
        )
    except Exception as e:
        return render_template('dalle.html', model = image_model, error = str(e))

    if response.data:
        image_urls = []
        for image_data in response.data:
            image_url = image_data.url
            if image_url:
                image_urls.append(image_url)

        return render_template('dalle.html', model = image_model, images = image_urls)
    else:
        return render_template('dalle.html', model = image_model, error = 'No images generated.')
# end def: image_gen

if __name__ == '__main__':
    app.run(debug = bool(os.getenv('GPT_DEBUG', False)))
# end if: __name__
