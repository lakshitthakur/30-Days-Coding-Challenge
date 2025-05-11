import random
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Slower speech rate
    engine.say(text)
    engine.runAndWait()

def get_random_affirmation(file_path="affirmations.txt"):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return random.choice([line.strip() for line in lines if line.strip()])

if __name__ == "__main__":
    affirmation = get_random_affirmation()
    print(f"💬 Today's Affirmation: {affirmation}")
    speak(affirmation)
