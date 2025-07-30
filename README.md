
# 🤖 JARVIS - Offline AI Voice Assistant in Python

Jarvis is a fully **offline AI assistant** created using Python. It listens to your **voice commands**, responds using **speech**, and automates various desktop tasks — just like a mini version of Alexa or Google Assistant, but completely offline and customizable!

## 📌 Features

| Feature | Description |
| 🗣️ Voice Recognition | Understands spoken commands using your microphone |
| 🔊 Text-to-Speech | Responds using offline speech via `pyttsx3` |
| 🕒 Time & Date | Speaks the current time and date |
| 🎵 Music Playback | Randomly plays YouTube music links |
| 📝 Task Manager | Add, remove, speak, or display reminders via a local file |
| 📸 Screenshot Tool | Takes screenshots and saves them with timestamps |
| 🖥️ Open Applications | Launches apps using voice (via simulated keypresses) |
| 🌐 Open Websites | Opens Google, YouTube, Facebook, etc. by voice |
| 📚 Wikipedia Search | Speaks Wikipedia summaries for queried topics |
| 🔍 Google Search | Performs Google searches from voice input |
| 💬 WhatsApp Messages | Sends scheduled or instant messages using `pywhatkit` |

## 🛠️ Technologies Used

- `pyttsx3` – Offline text-to-speech
- `speech_recognition` – Voice input from microphone
- `pyautogui` – For screen automation and screenshots
- `wikipedia` – Search and speak summaries
- `webbrowser` – Open URLs in default browser
- `datetime` – Get current time and date
- `plyer` – Show desktop notifications
- `pywhatkit` – WhatsApp message automation
- `os`, `random`, `time` – System and logic support
- 
## 🧠 How It Works (Workflow)

1. **Start Assistant** → `main_process()` starts listening.
2. **Speak a Command** → e.g., *"what's the time"*, *"add task"*, *"open YouTube"*
3. **Command Executed** → Assistant speaks back or performs an action.

## 📁 File Structure

```bash
JARVIS-AI/
│
├── openaireq.py           # Main JARVIS code
├── TODO.txt               # Text file to store to-do tasks
├── Screenshots/           # Folder where screenshots are saved
├── .venv/                 # (Optional) Virtual environment
└── README.md              # You're reading this!
🏁 How to Run the Project
🐍 Prerequisites:
Make sure Python 3.8+ is installed. Then install the required libraries:

pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyautogui plyer
▶️ Run the Assistant:
python openaireq.py
The assistant will start listening. Just say: "hello", "what's the time", "take screenshot", etc.

🧪 Example Commands to Try
"Hello"

"What’s the time?"

"Add task: submit project"

"Remove task number 2"

"Take screenshot"

"Open Google"

"Search Python tutorials"

"Send WhatsApp message"

🚀 Future Improvements
Add GUI using Tkinter or PyQt

Integrate weather APIs, email automation, or chatbot functionality

Add wake-word detection for passive listening

📄 License
This project is open source and free to use. Add your own ideas, upgrade it, or build something new on top of it!

🙋‍♂️ Author
Made with ❤️ by Gyananjay Singh

