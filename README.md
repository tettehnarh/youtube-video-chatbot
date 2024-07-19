# Video to Speech Chatbot

This project streams the audio from a YouTube video, transcribes it using OpenAI's Whisper model, and allows interaction with the transcript using an OpenAI chat model in a command-line interface.

## Setup

### Prerequisites

- Python 3.7+
- OpenAI API Key
- pip

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
   pip install openai pytube requests
   ```

4. **Create a `config.py` file in the root folder with your OpenAI API key**:
   ```python
   # config.py
   API_KEY = "your_openai_api_key_here"
   ```

### Update `cipher.py` for PyTube

Due to an issue with PyTube, you need to manually update the `cipher.py` file to enable video downloads:

1. **Locate `cipher.py`**:

   - Navigate to the `pytube` library directory. If using a virtual environment, it will be under:
     ```sh
     venv/lib/pythonX.X/site-packages/pytube/cipher.py
     ```
   - Replace `pythonX.X` with your Python version (e.g., `python3.9`).

2. **Edit `cipher.py`**:
   - Open `cipher.py` and locate line 264.
   - Replace the existing line with the following code:
     ```python
     function_patterns = [
         # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
         # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
         # var Bpa = [iha];
         # ...
         # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
         # Bpa.length || iha("")) }};
         # In the above case, `iha` is the relevant function name
         r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
         r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
         r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
     ]
     ```

## Usage

1. **Run the script**:

   ```sh
   python video_to_speech_chatbot.py
   ```

2. **Follow the prompts to interact with the transcript of the video**:
   - The script will stream the audio from the provided YouTube URL.
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
