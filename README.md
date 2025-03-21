# JarvisAI
Voice Assistant
This is a simple voice assistant program that allows users to interact with their computer through voice commands. The assistant can perform various tasks such as opening applications, fetching weather information, playing music on YouTube, searching Wikipedia, and more. The assistant can also lock, sleep, shutdown, or restart the system.

Features
Voice Commands: The assistant listens to and processes voice commands.
Command Mode: The assistant can be activated by saying "activate command mode," and only then will it start accepting commands.
Weather Information: You can ask for the weather in any city.
YouTube: Play music on YouTube by voice command.
Wikipedia Search: Search for topics on Wikipedia.
System Operations: Lock, sleep, shutdown, or restart the system via voice commands.
Customizable: The assistant can remember user preferences (e.g., user's name) and use them in subsequent interactions.
Web Search: If the command is not recognized, it will perform a web search using Microsoft Edge.
Requirements
To run this voice assistant, you need the following libraries installed:

pyttsx3: A library for text-to-speech conversion.
speech_recognition: A library to recognize speech from the microphone.
wikipedia: A Python library to search and get information from Wikipedia.
pywhatkit: A Python library for various web-related tasks (like playing YouTube videos).
requests: A library to make HTTP requests, used for fetching weather data.
json: To save and load preferences.
subprocess: To interact with system applications.
ctypes: To lock the system.
You can install the required libraries using the following command:

bash
Copy
pip install pyttsx3 speechrecognition wikipedia pywhatkit requests
How It Works
Command Mode: The assistant starts in a non-command mode. To activate command mode, you need to say activate command mode, command mode activate, or command mode. Once command mode is activated, you can give various commands, such as opening applications, playing YouTube videos, fetching weather information, and more.

Voice Commands: After command mode is activated, the assistant listens for commands. It processes the input and performs the requested action. If the command is recognized, the corresponding action is executed. For example, saying "play song" will play the song on YouTube.

Fallback: If the assistant doesn't recognize a command, it will search for it on the web using Microsoft Edge and display the results via Bing search.

System Operations: The assistant can also perform system operations like locking the system, putting it to sleep, shutting down, or restarting the computer.

Personalization: The assistant can remember your name and use it in future interactions. You can say "remember my name is [name]" and the assistant will store that information in a preferences file.

Available Commands
Here are some example commands the assistant can understand:

activate command mode: Activates command mode.
play [song name]: Plays a song on YouTube.
open youtube: Opens YouTube in the browser.
search for [query]: Searches the web using Bing.
weather: Asks for the weather of a specific city.
wikipedia [topic]: Searches for a topic on Wikipedia.
lock: Locks the computer.
sleep: Puts the system to sleep.
shutdown: Shuts down the system.
restart: Restarts the system.
what is my name: Tells you the name the assistant remembers.
Example Usage
Activate Command Mode:

User: "Activate command mode"
Assistant: "Command mode activated."
Play a Song:

User: "Play Shape of You"
Assistant: "Playing Shape of You on YouTube."
Get Weather:

User: "Weather in London"
Assistant: "The temperature in London is 15°C with clear sky."
Search Wikipedia:

User: "Wikipedia Python programming"
Assistant: "Searching Wikipedia for Python programming..."
Assistant reads a summary from Wikipedia.
Perform System Operations:

User: "Lock the system"
Assistant: "Locking the system."
Fallback Web Search:

User: "What is the tallest building in the world?"
Assistant: "Let me search that on the web for you..."
Assistant opens a Bing search for the query.
Saving and Loading Preferences
The assistant can remember your name by saying:

Remember my name is [name]
It will store the information in a preferences.json file and use it in subsequent interactions. You can also check what the assistant remembers by saying:

What is my name?
Requirements
Operating System: Windows (the code uses Microsoft Edge for web searches)
Python Version: 3.6 or higher
Microphone: Required for voice input
