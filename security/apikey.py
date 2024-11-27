import json
import sys

KEY_FILE = '.apikey'

def get_key():
    org = None
    proj = None
    role = 'user'
    model = 'gpt-4o-mini'

    try:
        with open(KEY_FILE) as f:
            data = json.load(f)
            if 'organization' in data:
                org = data['organization']
            if 'project' in data:
                proj = data['project']
            if 'role' in data:
                role = data['role']
            if 'model' in data:
                model = data['model']
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
