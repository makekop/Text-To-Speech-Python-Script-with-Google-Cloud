# Text-To-Speech Web App (Flask + Google Cloud)

This is a Flask-based web interface for converting text into natural-sounding speech using Google Cloud's Text-to-Speech API.

## Features

- Submit custom text from the browser
- Uses Google Cloud's high-quality voices (e.g., Studio models)
- Saves MP3 audio output to `/static/audio/`
- Automatically overwrites previous output with the latest result

## Requirements

Install Python dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
Flask==2.2.5
google-cloud-texttospeech==2.15.0
```
## Configuration

1. **Google Cloud Service Account**

- Follow the setup guide from the [google_cloud file](../google_cloud/README.md) to enable the API and create a service account.
- Save the JSON file locally (e.g., `authorization.json`).

2. **Edit the credential path in `CloudSpeechflask.py`:**

```python
credential_path = "/your/local/path/authorization.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
```

3. **Set Up Directory Structure:**

Your folder should look like this:

```
Text-To-Speech-Python-Script-with-Google-Cloud/
│
├── CloudSpeechflask.py
├── requirements.txt
├── static/
│   └── audio/
│       └── output.mp3
└── templates/
    └── index.html
```

## Run the App

```bash
python3 CloudSpeechflask.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```
## **Environment Configuration**  
You may set your environment variable differently depending on your operating system:  

### **MacOS/Linux:**  
Add the following line to your terminal or shell configuration file (e.g., `~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):  
```bash  
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/authorization.json"  
```  
Then run:  
```bash  
source ~/.zshrc  # or ~/.bashrc, ~/.bash_profile depending on your shell  
```  

Alternatively, you can set the environment variable directly in the Python script:  
```python  
import os  
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/authorization.json"  
```  

### **Windows (Command Prompt):**  
Run the following command in Command Prompt:  
```cmd  
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\authorization.json  
```  

Or in PowerShell:  
```powershell  
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\authorization.json"  
```  

Alternatively, set it directly in the Python script:  
```python  
import os  
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\path\\to\\your\\authorization.json"  
```  

---

## Notes

- Do **not** commit your `authorization.json` file to GitHub.
- Add it to `.gitignore` to keep credentials private.

## License

MIT