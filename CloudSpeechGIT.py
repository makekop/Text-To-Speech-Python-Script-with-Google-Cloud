import os 
from google.cloud import texttospeech # Import Text-To-Speech API from Google Cloud

# Verify your Google Cloud Credentials with using os.environ 
credential_path = "demofile/authorization.json" # Replace this part with your own file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# Set up client
client = texttospeech.TextToSpeechClient()

# Read the text file from the file path you've set
text_path = "demofile/textfile.txt" #Replace this part with your own file path
with open(text_path, "r", encoding="utf-8") as text_file:
    text_block = text_file.read().strip()

# Define the text input
synthesis_input = texttospeech.SynthesisInput(text=text_block)

# Select voice
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O"
)

# Select audio format
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1,
    pitch=1
)

# Perform the text-to-speech request
response = client.synthesize_speech(
    input=synthesis_input, 
    voice=voice, 
    audio_config=audio_config
)

# Create an output file path where you want your audio files saved
output_folder = "demofile/audiofiles" # Replace this part with your own path

# Get a unique filename 
def get_unique_filename(base_filename="output.mp3"):
    filename, extension = os.path.splitext(base_filename)
    counter = 1

# Add folder path and generate unique filename inside that folder
    while os.path.exists(os.path.join(output_folder, base_filename)):
        base_filename = f"{filename}_{counter}{extension}"
        counter += 1
    return os.path.join(output_folder, base_filename)

unique_filename = get_unique_filename("output.mp3")

# Save the audio to a file
with open(unique_filename, "wb") as out:
    out.write(response.audio_content)

# Print the filename in console
print(f"Audio file saved as {unique_filename} ")