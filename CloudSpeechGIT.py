import os 
from google.cloud import texttospeech 

credential_path = "demofile/authorization.json" 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

client = texttospeech.TextToSpeechClient()

text_path = "demofile/textfile.txt"
with open(text_path, "r", encoding="utf-8") as text_file:
    text_block = text_file.read().strip()

synthesis_input = texttospeech.SynthesisInput(text=text_block)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1,
    pitch=1
)

response = client.synthesize_speech(
    input=synthesis_input, 
    voice=voice, 
    audio_config=audio_config
)

output_folder = "demofile/audiofiles"

def get_unique_filename(base_filename="output.mp3"):
    filename, extension = os.path.splitext(base_filename)
    counter = 1

    while os.path.exists(os.path.join(output_folder, base_filename)):
        base_filename = f"{filename}_{counter}{extension}"
        counter += 1
    return os.path.join(output_folder, base_filename)

unique_filename = get_unique_filename("output.mp3")

with open(unique_filename, "wb") as out:
    out.write(response.audio_content)

print(f"Audio file saved as {unique_filename} ")
