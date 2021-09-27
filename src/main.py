import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import os 
import sys
import json
import requests
import platform 
import socket,json,psutil,logging

# Voice Engine Init
voice_id = "english"
engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
engine.setProperty('voice',voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)


#Small TTS Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Greet Function 
def greeting():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        speak("Awaiting command.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        speak("Awaiting command.")
    else:
        speak("Good Evening")
        speak("Awaiting command.")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as src:
        audio=r.listen(src)

        try:
            input=r.recognize_google(audio,language='en-us')
            print(f"User said:{input}\n")

        except Exception as e:
            return "None"
        return input

speak("Loading up Reaper")
time.sleep(1)
greeting()


if __name__=='__main__':
    while True:
        statement = takeCommand().lower()
        if statement==0: #This begins the command array
            continue

        elif "goodbye" in statement or "terminate" in statement:
            speak('Shutting down Reaper')
            break

        elif 'do my homework' in statement:
            input = takeCommand().lower()
          