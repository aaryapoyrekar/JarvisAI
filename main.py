import site
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import cv2

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        print("Speech service is unavailable.")
        return "Speech service is unavailable."

    return query

if __name__ == "__main__":
    print("PyCharm")
    say("Hello I'm Jarvis A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com/"], ["linkedin", "https://www.linkedin.com/feed/"], ["google", "https://www.google.com/"],
                 ["github", "https://github.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} maam...")
                webbrowser.open(site[1])

            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"The time is {strfTime}")

            if "open camera" in query.lower():
                say("Opening camera now...")

                cap = cv2.VideoCapture(0)
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        say("Failed to grab frame.")
                        break
                    cv2.imshow('Camera', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()

            app_folder = r"C:\Users\aarya\OneDrive\Documents\apps"

            apps = {
                "chatgpt": "ChatGPT Installer.exe",
                "canva": "Canva Setup 1.100.0.exe",
                "discord": "DiscordSetup.exe",
                "github": "GitHubDesktopSetup-x64.exe",
                "linkedin": "LinkedIn Installer.exe",
                "notion": "Notion Setup 4.12.1.exe",
                "visual studio code": "Visual Studio Code.lnk",  # only one .lnk shortcut
                "vlc": "vlc-3.0.21-win32.exe",
                "whatsapp": "WhatsApp Installer.exe",
                "zoom": "ZoomInstallerFull.exe",
                "anaconda": "Anaconda3-2024.10.1-Windows-x86_64.exe"
            }

            for app, exe_file in apps.items():
                if f"open {app}" in query.lower():
                    say(f"Opening {app}...")
                    app_path = os.path.join(app_folder, exe_file)
                    if os.path.exists(app_path):
                        os.startfile(app_path)
                    else:
                        say(f"Sorry, I couldn't find {app}")
