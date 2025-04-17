## **Setup Guide**  

### **Part 1: Google Cloud Text-to-Speech API Configuration:**  

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