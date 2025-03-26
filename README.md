# Text-To-Speech Python Script with Google Cloud

This is a Python-based text-to-speech application that reads text from a text file and converts it into an audio file (MP3) using Google Cloud's Text-to-Speech API. The generated audio files are saved with unique filenames to avoid overwriting.

---

## Features:
- Converts text from a text file into speech.
- Supports Google Cloud's natural-sounding voices.
- Saves audio output with unique filenames to avoid overwriting.

---

## Requirements:
- Python 3.x
- Google Cloud Python Client Library: Install it using:
  ```bash
  pip3 install google-cloud-texttospeech
- Google Cloud Service Account Credentials.

# Part 1: Google Cloud Text-to-Speech API Setup Guide (If you already have the API Key or required Credentials you can skip to Part 2)

Create a Google Cloud Project:
1. Log in or Sign Up to Google Cloud Console: https://console.cloud.google.com/
2. Click "Create Project"
3. Enter a project name and click "Create".

Enable the Text-to-Speech API:
1. From the top left navigation menu, go to APIs & Services > Library.
2. Search for "Cloud Text-to-Speech API".
3. Click on the API and press "Enable".

Create Service Account & Credentials:
1. Go to APIs & Services > Credentials.
2. Click "+ Create Credentials" > "Service Account".
3. Enter a name for the service account (e.g., `tts-service-account`).
4. Click "Create and Continue".
5. Under Role, search for "Cloud Text-to-Speech Agent" and select it.
6. Click "Done".

Generate JSON Key:
1. Under Service Accounts, find your new account and click on it.
2. Go to the Keys tab.
3. Click "Add Key" > "Create New Key".
4. Select "JSON" and click "Create".
5. Save the file and rename it to something relevant

# Part 2: Script Conguration.

Replace these paths in the script before running:
- Google Cloud Credentials: credential_path = "/Users/yourname/demofile/authorization.json" # Replace with your desired JSON key path
- Input Text File: text_path = "/Users/yourname/demofile/textfile.txt"  # Replace with your desired text file path
- Output Audio Folder: output_folder = ""/Users/yourname/demofile/audiofiles" # Replace with your desired output folder

Notes:
Keep the JSON file private (avoid committing it to public repos).
Ensure the path in your code matches your local file location.


