import datetime
import json
import os
import random
import smtplib
import sys
import webbrowser

import cv2
import pyttsx3
import pywhatkit as what
import speech_recognition as sr
import wikipediaapi


# Initialize text-to-speech engine
def initialize_tts():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    return engine

# Speak function
def speak(engine, audio):
    engine.say(audio)
    engine.runAndWait()

# Get user command using speech recognition
def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=20, phrase_time_limit=10)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
        return query.lower()
    except Exception as e:
        speak("Say that again, please.")
        return "none"

# Greeting function
def greeting(engine):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(engine, "Good Morning, Loogu")
    elif 12 <= hour < 18:
        speak(engine, "Good Afternoon, Loogu")
    elif 18 <= hour < 21:
        speak(engine, "Good Evening, Loogu")
    else:
        speak(engine, "Good Night")
    speak(engine, "Hello Sir, How can I help you today?")

# Function to extract hours and minutes from time input
def extract_time(time_input):
    parts = time_input.lower().split()
    hours, minutes = None, None

    if len(parts) >= 2:
        time_part = parts[-2]
        if ":" in time_part:
            hours, minutes = map(int, time_part.split(":"))

    if "pm" in parts and hours is not None and hours < 12:
        hours += 12

    return hours, minutes

# Send WhatsApp message function
def send_message(peoples_data):
    for person in peoples_data:
        if person["name"].lower() == name:
            speak(engine, f"What message do you want to send to {name}?")
            msg = get_command().lower()
            phone_number = person["number 1"]
            speak(engine, "Please specify the time you want to send the message.")
            time_input = get_command().lower()
            try:
                hours, minutes = extract_time(time_input)
                what.sendwhatmsg(phone_number, msg, hours, minutes)
                speak(engine, "Message sent successfully.")
            except Exception as e:
                speak(engine, f"An error occurred while sending the message: {e}")
            break
    else:
        speak(engine, f"Sorry, {name} was not found in your contacts.")

# Send email function
def send_email(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('logukaruna28@gmail.com', '@Logu2002')
    server.sendmail('logukaruna28@gmail.com', to, content)
    server.close()

# Main function
if __name__ == '__main__':
    engine = initialize_tts()
    greeting(engine)
    
    file_path = 'Python\\AI\\DB.json'
    try:
        with open(file_path, 'r') as data_file:
            peoples_data = json.load(data_file)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        peoples_data = []  # Set to an empty list if the file is not found
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        peoples_data = []  # Set to an empty list in case of other errors

    while True:
        query = get_command()

        if "open notepad" in query:
            notepad = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepad)
        elif "play music" in query:
            music_dir = "F:\\Songs\\fav songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "wikipedia" in query:
            speak(engine, "Searching in Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipediaapi.summary(query, sentences=2)
            speak(engine, "According to Wikipedia")
            speak(engine, results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak(engine, "What should I search on Google for you?")
            cm = get_command()
            webbrowser.open(f"{cm}")
        elif "send a message" in query:
            speak(engine, "To whom do I need to send a message, sir?")
            name = get_command()
            send_message(peoples_data)
        elif "play a song on youtube" in query:
            speak(engine, "What song should I play for you, sir?")
            song = get_command()
            what.playonyt(song)
        elif "send an email" in query:
            try:
                speak(engine, "What should I send in the email?")
                content = get_command()
                to = "kishoresekar7094@gmail.com"
                send_email(content)
                speak(engine, "Email has been sent successfully")
            except Exception as e:
                print(e)
                speak(engine, "Unable to send the email")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(engine, f"Sir, the time is {time}")
        elif "shutdown" in query:
            speak(engine, "Thank you, sir. Have a nice day.")
            sys.exit()
