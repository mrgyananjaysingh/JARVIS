"""
📌 JARVIS AI Assistant – Project Explanation (Step-by-Step from Zero to Hundred)

This project is a complete **offline voice-controlled AI assistant** named "Jarvis" created using Python.
It can listen to voice commands, respond using speech, and perform tasks like:
- Speaking current time/date
- Playing random songs
- Managing task reminders (add/remove/show tasks)
- Taking screenshots
- Opening apps/websites
- Sending WhatsApp messages (instant or scheduled)
- Searching Wikipedia/Google

We built this assistant step-by-step:

🔧 STEP 1: IMPORTING REQUIRED LIBRARIES
- `os`: for creating folders and file handling (e.g., for screenshots and TODO list)
- `pyttsx3`: for converting text to speech (offline, unlike gTTS)
- `speech_recognition`: for capturing and understanding your voice
- `random`: to select random songs
- `webbrowser`: to open URLs for music, searches, etc.
- `datetime`: to fetch current time and date
- `plyer.notification`: to show popup task notifications on the desktop
- `pyautogui`: for screen automation (screenshots, keypresses)
- `wikipedia`: for answering factual questions via summaries
- `pywhatkit`: for interacting with WhatsApp via web

🗣️ STEP 2: INITIALIZING VOICE ENGINE
- We used `pyttsx3.init()` to get the speech engine.
- We set the default voice (usually male) and speech rate (speed) to 170 words/minute.

📢 STEP 3: DEFINING 'speak()' FUNCTION
- This function takes a string input and speaks it out loud using the speech engine.
- Used repeatedly to respond back to the user.

🎤 STEP 4: DEFINING 'command()' FUNCTION
- Listens from the microphone using `speech_recognition`.
- Waits until a valid command is received (keeps retrying on errors).
- Uses Google’s recognizer to convert voice to text (`en-in` language for Indian English).
- Handles background noise via `adjust_for_ambient_noise`.

🧠 STEP 5: MAIN FUNCTION 'main_process()' — JARVIS'S BRAIN
- This runs the assistant’s logic.
- First, it listens to a voice command and cleans it (lowercase, trimmed).

✅ Features added one by one:

1. **Greetings** – If the user says "hello", it responds politely.

2. **Play Music** – Randomly opens one of three YouTube music links.

3. **Time & Date** – Uses `datetime` to speak current time or today's date.

4. **Task Management System** (via `TODO.txt` file):
    - Add task: User speaks a task, which is added with auto-numbering.
    - Speak tasks: Reads out all current tasks.
    - Show task: Displays tasks via desktop notification.
    - Remove task: Reads out tasks and deletes one based on the spoken task number.

5. **Take Screenshot**:
    - Creates a "Screenshots" folder if it doesn’t exist.
    - Saves screenshots with current date & time in filename.

6. **Open Applications**:
    - If the user says “open [app name]”, it simulates pressing the Windows key, typing the app name, and hitting Enter.

7. **Open Websites**:
    - Specific keywords like "open google", "open facebook", etc. open those sites using `webbrowser`.

8. **Wikipedia Search**:
    - Speaks the first sentence of a Wikipedia summary for a searched topic.

9. **Google Search**:
    - If user says "search [anything]", it opens a Google search tab for that query.

10. **Send WhatsApp Message**:
    - Two types:
        - `send whatsapp`: Scheduled message to a phone number at a specific time.
        - `send message immediately`: Sends the message instantly.

11. **Fallback**:
    - If a command isn’t understood, it politely asks the user to repeat.

🚀 STEP 6: RUNNING THE ASSISTANT
- `main_process()` is called at the end to start listening.

💡 HIGHLIGHTS:
- Offline TTS (pyttsx3) makes it fast and independent of internet.
- Easy to extend with more skills or APIs.
- Can be combined with GUI (Tkinter) later.
- Modular and clean for real-world usage.

📁 Files/Folders Used:
- `TODO.txt`: To store task list line-by-line.
- `Screenshots/`: Stores auto-named screenshot PNGs.

🔚 Overall, this assistant mimics the behavior of real personal assistants like Alexa or Google Assistant but is fully custom-built, offline-capable, and expandable using Python.
"""



# 📌 Importing required libraries
import os  # Used for file and directory operations
import pyttsx3  # For text-to-speech functionality
import speech_recognition as sr  # For converting voice input to text
import random  # To randomly choose songs or other elements
import webbrowser  # To open websites in browser
import datetime  # For getting current date and time
from plyer import notification  # For showing desktop notifications
import pyautogui  # For automation like taking screenshots or typing
import wikipedia  # For searching summaries from Wikipedia
import pywhatkit as pwk  # For tasks like sending WhatsApp messages
import time  # Used for sleep/delay operations

# 🎤 Initialize text-to-speech engine
engine = pyttsx3.init()  # Initializes the pyttsx3 engine

# 🔊 Voice & rate setup
voices = engine.getProperty('voices')  # Get list of available voices
engine.setProperty('voice', voices[0].id)  # Set voice to default (0 is usually male)
engine.setProperty('rate', 170)  # Set speaking speed (words per minute)

# 🗣️ Speak function
def speak(audio):
    engine.say(audio)  # Convert text to speech
    engine.runAndWait()  # Wait till speaking finishes

# 🎧 Function to take voice input from user
def command():
    content = ""  # Empty content to begin with
    while content == "":
        r = sr.Recognizer()  # Create recognizer object
        with sr.Microphone() as source:  # Use default microphone as input
            print("🎙️ Speak now...")
            r.adjust_for_ambient_noise(source)  # Reduce background noise
            audio = r.listen(source)  # Capture the audio

        try:
            content = r.recognize_google(audio, language='en-in')  # Use Google to recognize speech
            print("⚡ Voice command recognized...")
            print("🧠 Command: " + content)
        except Exception as e:
            print("⚠️ System couldn't process your voice. Try again.")

    return content  # Return recognized command

# 🚀 Main logic starts here
def main_process():
    request = command().lower().strip()  # Get command, convert to lowercase, remove spaces

    # 🧠 Respond to greeting
    if request == "hello":
        speak("Hello! I am Gyananjay Singh's personal AI assistant. 👋")
    
    # 🎶 Music playing
    elif "play music" in request or "play song" in request:
        print("🎵 Playing Music...")
        song = random.randint(1, 3)  # Randomly pick a number
        if song == 1:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Song 1
        elif song == 2:
            webbrowser.open("https://youtu.be/VJxppgsHjF8?si=jTy-euNOP11Pe7vm")  # Song 2
        elif song == 3:
            webbrowser.open("https://youtu.be/4DfVxVeqk2o?si=_MAVzW_rvT25CdMY")  # Song 3

    # ⏰ Time response
    elif "time" in request or "tell me the time" in request or "what is the time" in request:
        now_time = datetime.datetime.now().strftime("%I:%M %p")  # Get current time in 12-hour format
        speak("⏰ Gyananjay, the current time is " + now_time)

    # 📅 Date response
    elif "date" in request or "what's the date" in request or "today's date" in request:
        now_date = datetime.datetime.now().strftime("%A, %d %B %Y")  # Get full date string
        speak("📅 Today is " + now_date)

    # 🆕 Add Task with Auto-Numbering
    elif any(kw in request for kw in ["add", "remind", "note", "remember", "task to do", "i have to"]):
        speak("📝 What task do you want to add?")
        task = command().strip()
        if task:
            try:
                with open("TODO.txt", "r") as file:
                    existing_tasks = [line.strip() for line in file if line.strip()]  # Read existing tasks
            except FileNotFoundError:
                existing_tasks = []  # No tasks yet

            task_number = len(existing_tasks) + 1  # New task number
            full_task = f"{task_number}. {task}"
            existing_tasks.append(full_task)

            with open("TODO.txt", "w") as file:  # Write back with correct numbering
                for i, t in enumerate(existing_tasks, 1):
                    file.write(f"{i}. {t.split('. ', 1)[-1]}\n")

            speak(f"✅ Task added: {task}")
        else:
            speak("❌ Task was empty. Please try again.")

    # 📣 Enhanced Task Speaking
    elif "tell me my task" in request or "what are my tasks" in request:
        try:
            with open("TODO.txt", "r") as file:
                tasks = [line.strip() for line in file if line.strip()]  # Remove empty lines
                if tasks:
                    speak("📋 Here are your tasks:")
                    for idx, task in enumerate(tasks, 1):
                        print(f"Task {idx}: {task}")
                        speak(f"Task {idx}: {task}")
                else:
                    speak("📭 Your task list is empty.")
        except FileNotFoundError:
            speak("📭 You have no tasks yet.")

    # 🔔 Improved Task Notification
    elif "show work" in request or "show task" in request:
        try:
            with open("TODO.txt", "r") as file:
                task = file.read()
                if task.strip():
                    notification.notify(
                        title="🗂️ Today's Tasks",
                        message=task,
                        timeout=5
                    )
                else:
                    notification.notify(
                        title="🗂️ Task List",
                        message="📭 You have no tasks today.",
                        timeout=5
                    )
        except FileNotFoundError:
            notification.notify(
                title="🗂️ Task List",
                message="📭 You have no tasks yet.",
                timeout=5
            )

    # 🗑️ Remove Task by Number
    elif "remove task" in request or "delete task" in request:
        try:
            with open("TODO.txt", "r") as file:
                tasks = [line.strip() for line in file if line.strip()]
            if not tasks:
                speak("📭 Your task list is already empty.")
            else:
                speak("🧾 Here are your tasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                    speak(f"Task {idx}: {task}")
                speak("Please say the number of the task you want to delete.")
                num = command()

                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        removed_task = tasks.pop(num - 1)
                        with open("TODO.txt", "w") as file:
                            for task in tasks:
                                file.write(task + "\n")
                        speak(f"✅ Task {num} deleted: {removed_task}")
                    else:
                        speak("❌ Invalid task number.")
                else:
                    speak("❌ Couldn't understand the number.")
        except FileNotFoundError:
            speak("📭 No task file found.")

    # 📸 Take Screenshot
    elif "take a screenshot" in request or "capture screen" in request:
        filename = "screenshot_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
        folder = "Screenshots"
        if not os.path.exists(folder):  # Create folder if not exists
            os.makedirs(folder)
        path = os.path.join(folder, filename)
        pyautogui.screenshot(path)  # Take screenshot and save
        speak(f"📸 Screenshot taken and saved as {filename}")

    # 🪟 Open application
    elif "open" in request:
        query = request.replace("open", "").strip()  # Extract app name
        pyautogui.press("super")  # Press Windows key
        pyautogui.typewrite(query)  # Type the app name
        pyautogui.sleep(0)  # Wait (0 seconds here)
        pyautogui.press("enter")  # Press Enter to open app

    # 🌐 Open specific websites
    elif "open google" in request:
        webbrowser.open("https://www.google.com")
    elif "open stackoverflow" in request:
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in request:
        webbrowser.open("https://github.com")
    elif "open facebook" in request:
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in request:
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in request:
        webbrowser.open("https://www.twitter.com")
    elif "open youtube" in request:
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in request:
        webbrowser.open("https://www.linkedin.com")

    # 📚 Wikipedia search
    elif "wikipedia" in request:
        query = request.replace("jarvis", "").strip()
        query = request.replace("search wikipedia", "").strip()
        print(request)
        result = wikipedia.summary(request, sentences=1)  # Get 1-line summary
        print(result)
        speak(result)

    # 🔍 Google search
    elif "search" in request or "google" in request:
        query = request.replace("search", "").replace("google", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google.")
        else:
            speak("❌ Please specify what you want to search for.")    

    # 📲 WhatsApp scheduled message
    elif "send whatsapp" in request:
        pwk.sendwhatmsg("+918384038559", "Hello, this is a test message from Gyananjay's assistant.", 18, 12, 2)

    # ⚡ WhatsApp instant message
    elif "send message immediately" in request:
        pwk.sendwhatmsg_instantly(
            "+919889076625", 
            "Hello from Gyananjay's assistant !",
            wait_time=10,
            tab_close=True, 
            close_time=3
        )

    # ❓ Fallback for unknown command
    else:
        speak("Sorry Gyananjay, I didn't understand that. Can you please repeat?")
        
# 🏁 Start the assistant
main_process()
