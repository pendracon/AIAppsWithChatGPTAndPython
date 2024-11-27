from openai import OpenAI
from security import apikey

def get_client():
    org, proj, role, key, model = apikey.get_key()

    if org and proj:
        client = OpenAI(organization = org, project = proj, api_key = key)
    elif org:
        client = OpenAI(organization = org, api_key = key)
    elif proj:
        client = OpenAI(project = proj, api_key = key)
    else:
        client = OpenAI(api_key = key)

    return client, role, model
# end def: get_client
