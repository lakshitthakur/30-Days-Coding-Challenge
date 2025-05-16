import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
    except Exception as e:
        print("❌ Could not understand. Say that again...")
        return ""
    return query.lower()

def run_jarvis():
    speak("Hello! I am your assistant.")
    while True:
        query = take_command()

        if "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "stop" in query or "exit" in query:
            speak("Goodbye!")
            break

        elif query:
            speak("I heard you say " + query)

if __name__ == "__main__":
    run_jarvis()
