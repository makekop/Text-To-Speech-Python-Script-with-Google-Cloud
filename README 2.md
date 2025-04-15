Awesome that you got it working! 🥳 Here's how I'd recommend going about organizing and updating your project for the Flask version.

---

## ✅ Step-by-Step: Create a New Branch for the Flask Version

Open your VSCode terminal and navigate to your project directory:

```bash
cd /path/to/Text-To-Speech-Python-Script-with-Google-Cloud
```

Create a new branch for the Flask version:

```bash
git checkout -b flask-version
```

Now commit your Flask-specific changes:

```bash
git add .
git commit -m "Add Flask version with web interface"
git push origin flask-version
```

This keeps your original version safe on the `main` branch while letting you develop and share the Flask app separately.

---

## 📄 Flask README.md (You can save this as `README.md` inside the `flask-version` branch)

```markdown
# Text-To-Speech Web App (Flask + Google Cloud)

This is a Flask-based web interface for converting text into natural-sounding speech using Google Cloud's Text-to-Speech API.

## 🌟 Features

- Submit custom text from the browser
- Uses Google Cloud's high-quality voices (e.g., Studio models)
- Saves MP3 audio output to `/static/audio/`
- Automatically overwrites previous output with the latest result

## 🛠️ Requirements

Install Python dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
Flask==2.2.5
google-cloud-texttospeech==2.15.0
```

## 🔧 Configuration

1. **Google Cloud Service Account**

- Follow the setup guide from the [original README](../main/README.md) to enable the API and create a service account.
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

## 🚀 Run the App

```bash
python3 CloudSpeechflask.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

## 📝 Notes

- Do **not** commit your `authorization.json` file to GitHub.
- Add it to `.gitignore` to keep credentials private.

## 📜 License

MIT