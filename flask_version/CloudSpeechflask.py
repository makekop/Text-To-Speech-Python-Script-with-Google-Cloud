from flask import Flask, render_template, request
from google.cloud import texttospeech
import os

app = Flask(__name__)

credential_path = "/Users/markuskoponen/Coding/TextToSpeech/authorizationgoogle.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file_path = None
    if request.method == "POST":
        text = request.form["text"]
        audio_file_path = text_to_speech(text)
    return render_template("index.html", audio_path=audio_file_path)

def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Studio-O"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1,
        pitch=1
    )

    output_folder = "static/audio"
    os.makedirs(output_folder, exist_ok=True)

    filename = "output.mp3"
    filepath = os.path.join(output_folder, filename)

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(filepath, "wb") as out:
        out.write(response.audio_content)

    return filepath

if __name__ == "__main__":
    app.run(debug=True)
