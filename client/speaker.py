import argparse
import sys

from util import openai as gpt

def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} -i <text file> [-o <output file>]')
        sys.exit(1)
    else:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", default="output.mp3")
    args = parser.parse_args(argv)

    client, gpt_model, gpt_voice = gpt.get_speech_client()
    with open(args.input, 'r') as f:
        text = ''.join(f.readlines())
        print(text)
    # end with: open

    with client.audio.speech.with_streaming_response.create(
        input = text,
        model = gpt_model,
        voice = gpt_voice,
        response_format = 'mp3'
    ) as response:
        response.stream_to_file(args.output)
    # end with: client
# end def: main

if __name__ == '__main__':
    main()
# end if: __name__
