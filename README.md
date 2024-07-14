# Video to Speech Chatbot

This project downloads the audio from a YouTube video, transcribes it using OpenAI's Whisper model, and allows interaction with the transcript using an OpenAI chat model in a command-line interface.

## Setup

### Prerequisites

- Python 3.7+
- OpenAI API Key

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/video-to-speech-chatbot.git
   cd video-to-speech-chatbot
   ```

2. **Create a virtual environment and activate it**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```sh
   pip install openai pytube
   ```

4. **Create a `config.py` file with your OpenAI API key**:
   ```python
   # config.py
   API_KEY = "your_openai_api_key_here"
   ```

## Usage

1. **Run the script**:

   ```sh
   python video_to_speech_chatbot.py
   ```

2. **Follow the prompts to interact with the transcript of the video**:
   - The script will download the audio from the provided YouTube URL.
   - The audio will be transcribed using the Whisper model.
   - You can interact with the transcript using the chatbot.
   - Type `exit`, `quit`, or `q` to exit the chatbot.

## Example

Here's an example of how the interaction works:

```sh
You: Summarize the transcript.
Assistant: The video is about...
You: Who is speaking in the video?
Assistant: The speaker in the video is...
```
