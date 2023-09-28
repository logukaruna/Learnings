import datetime
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

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}")
        return query

    except Exception as e:
       speak("say that again please")
       return "none"
    
def greeting():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <=12:
        speak("Good Morning logu")
    elif hour >= 13 and hour <=18:
        speak("Good Afternoon logu")
    elif hour >= 19 and hour <=21:
        speak("Good Evening Logu")
    else:
        speak("Good Night")
    speak("Hello Sir How can i help you today?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('logukaruna28@gmail.com', '@Logu2002')
    server.sendmail('logukaruna28@gmail.com', to, content)
    server.close()

if __name__ == '__main__' :
    greeting()
    while True:
        query = getCommand().lower()

        if "open notepad" in query:
            notepad = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepad)
        elif "play music" in query:
            music_dir = "F:\\Songs\\fav songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
       # elif "wikipedia" in query:
            speak("Searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipediaapi.summary(query, sentences =2)
            speak("According to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("What should i search on google for you")
            cm = getCommand().lower()
            webbrowser.open(f"{cm}")
        elif "send a message" in query:
            what.sendwhatmsg("+917094685168", "Hello Music director how are you",00,34)
        elif "play a song on youtube" in query:
            speak("What song should i play for you sir")
            song = getCommand().lower()
            what.playonyt(song)
        elif "send a mail" in query:
            try:
                speak("what should i send?")
                content = getCommand().lower()
                to = "kishoresekar7094@gmail.com"
                sendEmail(to, content)
                speak("Email Has been sent successfully")
            
            except Exception as e:
                print(e)
                speak("Unable to send the mail")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {time}")

        elif "shutdown" in query:
            speak("Thank you sir have a nice day")
            sys.exit()