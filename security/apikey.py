import json
import sys

from util import model as types

KEY_FILE = '.apikey'

def get_key(type = types.CHAT_CLIENT):
    org = None
    proj = None
    role = 'user'
    audio_model = 'whisper-1'
    chat_model = 'gpt-3.5-turbo'
    image_model = 'dall-e-2'

    try:
        with open(KEY_FILE) as f:
            data = json.load(f)
            if 'organization' in data:
                org = data['organization']

            if 'project' in data:
                proj = data['project']

            if 'role' in data:
                role = data['role']

            if type == types.IMAGE_CLIENT:
                if 'image_model' in data:
                    model = data['image_model']
                else:
                    model = image_model
            elif type == types.AUDIO_CLIENT:
                if 'audio_model' in data:
                    model = data['audio_model']
                else:
                    model = audio_model

            if type == types.CHAT_CLIENT:
                if 'chat_model' in data:
                    model = data['chat_model']
                else:
                    model = chat_model

            if 'key' not in data:
                print(f'API key not found.')
                sys.exit(1)
            return org, proj, role, data['key'], model
    except FileNotFoundError:
        print(f'API key file {KEY_FILE} not found.')
        sys.exit(1)
# end def: get_key

if __name__ == '__main__':
    org, proj, role, key, model = get_key()
    print(f'Organization: {org}')
    print(f'Project: {proj}')
    print(f'Role: {role}')
    print(f'Key: {key}')
    print(f'Model: {model}')
# end if: __name__
