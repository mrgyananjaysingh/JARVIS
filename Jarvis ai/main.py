# 📌 Importing required libraries
import pyttsx3
import speech_recognition as sr
import random 
import webbrowser
import datetime

# 🎤 Initialize text-to-speech engine
engine = pyttsx3.init()

# 🔊 Voice & rate setup
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[0].id)  # Set to system's default voice
engine.setProperty('rate', 170)  # Speed of speech (adjusted for clarity)

# 🗣️ Speak function
def speak(audio):
    engine.say(audio)  # Speak the given audio
    engine.runAndWait()

# 🎧 Function to take voice input from user
def command():
    content = ""
    while content == "":
        r = sr.Recognizer()  # Create recognizer object
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            r.adjust_for_ambient_noise(source)  # Reduce background noise
            audio = r.listen(source)  # Listen from microphone

        try:
            content = r.recognize_google(audio, language='en-in')  # Recognize using Google
            print("⚡ Voice command recognized...")
            print("🧠 Command: " + content)
        except Exception as e:
            print("⚠️ System couldn't process your voice. Try again.")

    return content

# 🚀 Main logic starts here
def main_process():
    request = command().lower().strip()  # Convert to lowercase and trim

    # 🧠 Respond to greeting
    if request == "hello":
        speak("Hello! I am Gyananjay Singh's personal AI assistant. 👋")
    
    # 🎶 Music playing
    elif "play music" in request:
        print("🎵 Playing Music...")
        song = random.randint(1, 3)  # Randomly pick a song
        if song == 1:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif song == 2:
            webbrowser.open("https://youtu.be/VJxppgsHjF8?si=jTy-euNOP11Pe7vm")
        elif song == 3:
            webbrowser.open("https://youtu.be/UBcu8hJwRq8?si=bBiacvF4veBEx3Rq")

    # ⏰ Time response
    elif "time" in request or "tell me the time" in request or "what is the time" in request:
        now_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("⏰ Gyananjay, the current time is " + now_time)

    # 📅 Date response
    elif "date" in request or "what's the date" in request or "today's date" in request:
        now_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak("📅 Today is " + now_date)

    # ❓ Unrecognized command
    else:
        speak("Sorry Gyananjay, I didn't understand that. Can you please repeat? 😅")

# 🏁 Start the assistant
main_process()
