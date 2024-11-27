import argparse
import sys

from util import openai as gpt

def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} -f <audio file> [-l <language code>]')
        sys.exit(1)
    else:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-l", "--lang", default="en")
    args = parser.parse_args(argv)

    client, gpt_model = gpt.get_audio_client()
    with open(args.file, 'rb') as f:
        text = client.audio.transcriptions.create(
            file = f,
            language = args.lang,
            model = gpt_model,
            response_format = 'text'
        )
        print(text)
    # end with: open
# end def: main

if __name__ == '__main__':
    main()
# end if: __name__
