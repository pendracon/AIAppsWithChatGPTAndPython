from openai import OpenAI
from security import apikey
from util import model as types

def __get_client(type = types.CHAT_CLIENT):
    org, proj, role, key, model, voice = apikey.get_key(type)

    if org and proj:
        client = OpenAI(organization = org, project = proj, api_key = key)
    elif org:
        client = OpenAI(organization = org, api_key = key)
    elif proj:
        client = OpenAI(project = proj, api_key = key)
    else:
        client = OpenAI(api_key = key)

    if type in [types.AUDIO_CLIENT, types.IMAGE_CLIENT]:
        return client, model
    elif type == types.SPEECH_CLIENT:
        return client, model, voice
    else:
        return client, role, model
# end def: get_client

def get_audio_client():
    client, model = __get_client(types.AUDIO_CLIENT)
    return client, model
# end def: get_chat_client

def get_chat_client():
    client, role, model = __get_client(types.CHAT_CLIENT)
    return client, role, model
# end def: get_chat_client

def get_code_client():
    client, role, model = __get_client(types.CODE_CLIENT)
    return client, role, model
# end def: get_code_client

def get_image_client():
    client, model = __get_client(types.IMAGE_CLIENT)
    return client, model
# end def: get_image_client

def get_search_client():
    client, role, model = __get_client(types.SEARCH_CLIENT)
    return client, role, model
# end def: get_search_client

def get_speech_client():
    client, model, voice = __get_client(types.SPEECH_CLIENT)
    return client, model, voice
# end def: get_speech_client
