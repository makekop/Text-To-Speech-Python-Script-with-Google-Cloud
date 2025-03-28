# Text-To-Speech Python Script with Google Cloud  

This is a Python-based text-to-speech application that reads text from a specified text file and converts it into an audio file (MP3) using Google Cloud's Text-to-Speech API. The generated audio files are saved with unique filenames to avoid overwriting. This repository includes a sample text file and audio file to demonstrate how the text-to-speech application works in practice.

---

## **Features:**  
- Converts text from a text file into natural-sounding speech.  
- Supports various Google Cloud voice configurations (e.g., language, pitch, speed).  
- Automatically saves audio output with unique filenames to avoid overwriting existing files.

---

## **Requirements:**  
Make sure you have the following installed:  
- **Python 3.x**  
- **Google Cloud Python Client Library**  
  Install it using:  
  ```bash
  pip install google-cloud-texttospeech
  ```  

Additionally, you will need Google Cloud Service Account credentials in JSON format to authenticate API requests.  

---

## **Setup Guide**  

### **Part 1: Google Cloud Text-to-Speech API Configuration:**  
If you already have a Google Cloud Project with Text-to-Speech API enabled and credentials set up, skip to **Part 2**. Otherwise, follow the steps below:  

1. **Create a Google Cloud Project:**  
   - Log in or sign up on [Google Cloud Console](https://console.cloud.google.com/).  
   - Click "Create Project."  
   - Enter a project name and click "Create."  

2. **Enable the Text-to-Speech API:**  
   - From the top left navigation menu, go to **APIs & Services > Library**.  
   - Search for "Cloud Text-to-Speech API."  
   - Click the API and press **Enable**.  

3. **Create Service Account & Credentials:**  
   - Navigate to **APIs & Services > Credentials**.  
   - Click **+ Create Credentials** > **Service Account**.  
   - Enter a name for the service account (e.g., `tts-service-account`) and click **Create and Continue**.  
   - Under **Role**, search for **Cloud Text-to-Speech Agent** and select it. 
   - Click **Done**.  

4. **Generate a JSON Key:**  
   - Under **Service Accounts**, find your new account and click on it.  
   - Go to the **Keys** tab.  
   - Click **Add Key** > **Create New Key**.  
   - Select **JSON** and click **Create**.  
   - Save the JSON file securely (e.g., `authorization.json`).  
   - **Keep this file private and avoid uploading it to public repositories.**  

---

### **Part 2: Configuring the Python Script**  

Before running the script, replace the following paths with your actual local paths:

1. **Set the Google Cloud Credentials Path:**  
   In the Python script, update this line:  
   ```python  
   credential_path = "demofile/authorization.json"  # Replace with your JSON key path  
   ```  

2. **Set the Input Text File Path:**  
   Update the path to the text file you want to convert:  
   ```python  
   text_path = "demofile/textfile.txt"  # Replace with your text file path  
   ```  

3. **Set the Output Audio Folder Path:**  
   Update the path to where you want the MP3 audio files saved:  
   ```python  
   output_folder = "demofile/audiofiles"  # Replace with your desired output folder  
   ```  

---

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

## **Running the Script:**  
Once you have configured the paths and set the environment variable, you can run the script directly within your code editor or you can run the saved Python script by its filename with:  
```bash  
python text_to_speech.py  
```  

---

## **Example Output:**  
The script will read the text from your specified text file, convert it to speech using the Google Cloud Text-to-Speech API, and save the output as an MP3 file in the specified folder.  
The saved file will have a unique filename (e.g., `output.mp3`, `output_1.mp3`, etc.) to prevent overwriting.  

---

## **requirements.txt:**  
The `requirements.txt` file can be found in the repository:  

```
google-cloud-texttospeech==2.15.0
```

To install the dependencies, run:  
```bash  
pip install -r requirements.txt  
```  

---


