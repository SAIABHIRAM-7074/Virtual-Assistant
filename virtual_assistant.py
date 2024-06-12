import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return "None"
        return command.lower()

# Function to tell the date and time
def tell_date_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"The current date and time is {date_time}")

# Function to greet the user
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

# Function to open the browser and search something
def open_browser_search(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Main function to run the assistant
def run_assistant():
    wish_me()
    while True:
        command = listen()
        if command == "none":
            continue
        if "date" in command or "time" in command:
            tell_date_time()
        elif "open browser" in command:
            speak("What should I search for?")
            query = listen()
            if query != "none":
                open_browser_search(query)
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can only tell date and time, or open browser and search something for now.")

if __name__ == "__main__":
    run_assistant()
