# AI Apps with ChatGPT and Python

Sample solutions for projects presented in the course *Build AI Apps with
ChatGPT and Python* from
[Mammoth Interactive](https://training.mammothinteractive.com).

The course is divided up into 6 modules including one for developing simple CLI
programs to access various GPT-based models using [OpenAI's](https://openai.com)
Python APIs, several web apps for doing the same, and a chrome extension for
basic chat access.

Simple CLI client programs presented in the course include for chat, image
generation, transcribing speech to text, and transcription with translation.
However, these solutions include to a program for text to speech instead of
translation. These are found in the [client](./client) directory.

The course builds each of the web apps as separate implementations with their
own (largely redundant), backends. These solutions, instead, present them as a
singular service with a combined backend. This is found in the [web](./web)
directory.

Support code for both the CLI programs and the web app is found in the
[security](./security) and [util](./util) directories. This code abstracts
creation of the various OpenAI clients and the API parameters needed by
them including the user's API key for accessing OpenAI's remote interface.

Code for the Chrome extension is found in the [chrome](./chrome) directory. The
extension utilizes the web service for backend support rather than connecting
directly to OpenAI.

Using these solutions requires creation of a JSON format API configuration file
in the solution root directory. The file must be named **.apikey** and have the
following structure:

```
{
    "organization": "org-...",
    "project": "proj_...",
    "key": "sk-proj-...",
    "role": "user",
    "audio_model": "whisper-1",
    "chat_model": "gpt-3.5-turbo",
    "image_model": "dall-e-2",
    "speech_model": "tts-1",
    "speech_voice": "alloy"
}
```

Fields "organization", "project", and "key" must contain the user's respective
information from OpenAI. The four AI models, speech voice, and role fields are
all optional, defaulting to the values shown if omitted.
