import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import json
import requests
import subprocess
import ctypes

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Weather API function
def get_weather(city):
    api_key = "b0b9b1814e84cd4c4d458f5bf8c58417"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = round(data['main']['temp'] - 273.15, 2)
        weather_desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {weather_desc}."
    else:
        return "Sorry, I couldn't fetch the weather."

# Listen to user input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
        except Exception:
            speak("Sorry, I didn't get that. Could you say it again?")
            return "none"
        return query.lower()

# Save preferences to a file
def save_preferences(preferences):
    with open("preferences.json", "w") as file:
        json.dump(preferences, file)

# Load preferences from a file
def load_preferences():
    try:
        with open("preferences.json", "r") as file:
            preferences = json.load(file)
    except FileNotFoundError:
        preferences = {}
    return preferences

# Open system apps
def open_app(app_name):
    apps = {
        "spotify": "spotify",
        "notepad": "notepad.exe",
        "word": "winword",
        "excel": "excel",
        "vs code": "code",
        "cmd": "cmd",
    }
    if app_name in apps:
        subprocess.Popen([apps[app_name]])
        speak(f"Opening {app_name}.")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

# Lock the system
def lock_system():
    ctypes.windll.user32.LockWorkStation()
    speak("Locking the system.")

# Sleep the system
def sleep_system():
    speak("Sleeping the system.")
    subprocess.call("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# Shutdown the system
def shutdown_system():
    speak("Shutting down the system.")
    subprocess.call(["shutdown", "/s", "/t", "1"])

# Restart the system
def restart_system():
    speak("Restarting the system.")
    subprocess.call(["shutdown", "/r", "/t", "1"])

# Global variable for command mode
is_command_mode = False  # Initially, we are not in command mode

# Process user commands
def process_command(query, preferences):
    global is_command_mode  # Declare as global

    if is_command_mode:
        # Handling known commands
        if 'play' in query:
            song = query.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            os.system("start https://www.youtube.com")

        elif 'search for' in query:
            search_query = query.replace("search for", "").strip()
            speak(f"Searching for {search_query} on the web.")
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            search_url = f"https://www.bing.com/search?q={search_query}"
            subprocess.Popen([edge_path, search_url])

        elif 'weather' in query:
            speak("Which city's weather would you like to know?")
            city = take_command()
            weather_info = get_weather(city)
            speak(weather_info)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'wikipedia' in query:
            search_query = query.replace("wikipedia", "").strip()
            speak("Searching Wikipedia...")
            try:
                results = wikipedia.summary(search_query, sentences=2)
                speak(results)
            except:
                speak("No results found.")

        elif 'remember' in query:
            if 'my name is' in query:
                name = query.replace("remember my name is", "").strip()
                preferences['name'] = name
                save_preferences(preferences)
                speak(f"Got it, I'll remember your name is {name}.")

        elif 'what is my name' in query:
            name = preferences.get('name', "I don't know your name yet.")
            speak(f"Your name is {name}.")

        elif 'exit' in query or 'sleep' in query:
            speak("Goodbye! Call me if you need anything.")
            exit()

        # System access commands
        elif 'lock' in query:
            lock_system()

        elif 'sleep' in query:
            sleep_system()

        elif 'shutdown' in query:
            shutdown_system()

        elif 'restart' in query:
            restart_system()

        elif 'open' in query:
            app_name = query.replace("open", "").strip()
            open_app(app_name)

        else:
            # If the command is not recognized, perform a web search using Microsoft Edge
            speak("Let me search that on the web for you...")
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            search_url = f"https://www.bing.com/search?q={query}"
            subprocess.Popen([edge_path, search_url])

    else:
        speak("Please activate command mode first by saying 'activate command mode'.")

# Main function
if __name__ == "__main__":
    preferences = load_preferences()

    # Personalized greeting based on time of day
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How can I assist you today? Please say 'activate command mode' to begin.")

    while True:
        query = take_command()
        if query != "none":
            # If the user doesn't activate command mode yet, only allow command mode activation
            if 'activate command mode' in query or 'command mode activate' in query or 'command mode' in query:
                is_command_mode = True
                speak("Command mode activated.")
            else:
                process_command(query, preferences)
