import json
import sys

from util import model as types

KEY_FILE = '.apikey'

def get_key(type = types.CHAT_CLIENT):
    org = None
    proj = None
    role = 'user'
    voice = None
    audio_model = 'whisper-1'
    chat_model = 'gpt-3.5-turbo'
    image_model = 'dall-e-2'
    speech_model = 'tts-1'
    speech_voice = 'alloy'

    try:
        with open(KEY_FILE) as f:
            data = json.load(f)
            if 'key' not in data:
                print(f'API key not found.')
                sys.exit(1)

            if 'organization' in data:
                org = data['organization']

            if 'project' in data:
                proj = data['project']

            if 'role' in data:
                role = data['role']

            if type == types.AUDIO_CLIENT:
                if 'audio_model' in data:
                    model = data['audio_model']
                else:
                    model = audio_model
            elif type == types.CHAT_CLIENT:
                if 'chat_model' in data:
                    model = data['chat_model']
                else:
                    model = chat_model
            elif type == types.IMAGE_CLIENT:
                if 'image_model' in data:
                    model = data['image_model']
                else:
                    model = image_model
            elif type == types.SPEECH_CLIENT:
                if 'speech_model' in data:
                    model = data['speech_model']
                else:
                    model = speech_model
                
                if 'speech_voice' in data:
                    voice = data['speech_voice']
                else:
                    voice = speech_voice

            return org, proj, role, data['key'], model, voice
    except FileNotFoundError:
        print(f'API key file {KEY_FILE} not found.')
        sys.exit(1)
# end def: get_key

if __name__ == '__main__':
    org, proj, role, key, model, voice = get_key(types.SPEECH_CLIENT)
    print(f'Organization: {org}')
    print(f'Project: {proj}')
    print(f'Role: {role}')
    print(f'Key: {key}')
    print(f'Model ({types.SPEECH_CLIENT}): {model}')
    print(f'Voice: {voice}')
# end if: __name__
