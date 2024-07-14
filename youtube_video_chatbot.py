from openai import OpenAI
from pytube import YouTube
import os
import config

url = "https://www.youtube.com/watch?v=uI1mYhtRRrs"

# Download the video
yt = YouTube(url)
title = yt.title
filename = 'downloaded_audio.webm'

# Get the audio stream
audio_streams = yt.streams.filter(only_audio=True)


def returnItag(audio_streams):
    for stream in audio_streams:
        if stream.mime_type == 'audio/webm':
            return stream.itag
    return None


itag = returnItag(audio_streams)

if itag:
    stream = yt.streams.get_by_itag(itag)
    stream.download(filename=filename)

    # Whisper code for transcription
    client = OpenAI(api_key=config.API_KEY)
    with open(filename, "rb") as audio_file:
        transcript_response = client.audio.translations.create(
            model="whisper-1",
            file=audio_file,
        )
        transcript = transcript_response.text  # Accessing the text attribute directly

    print(f"Transcript: {transcript}")

    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": f"The transcript of the video is: {transcript}"}
    ]

    # Chatbot loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Exiting the chatbot. Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})

        assistant_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )

        # Access the content attribute directly
        assistant_reply = assistant_response.choices[0].message.content
        print(f"Assistant: {assistant_reply}")

        # Add assistant response to conversation history
        conversation_history.append(
            {"role": "assistant", "content": assistant_reply})

else:
    print("No suitable audio stream found.")
