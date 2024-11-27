from security import apikey
from util import openai as gpt

def main():
    client, role, gpt_model = gpt.get_client()

    while True:
        prompt = input('Prompt: ')
        if prompt == 'exit':
            break
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
        print(chatgpt)
        print(f'[Total tokens used: {token_cost}]')
        print()
# end def: main

if __name__ == '__main__':
    main()
# end if: __name__
