# -*- coding: utf-8 -*-
"""
@author: Surbhi
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Surbhi")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Surbhi")

    else:
        speak("Good Evening Surbhi")

    speak("I am Mike, Please tell me how may I help you ? ")
    
def wishPeople():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning..")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon..")

    else:
        speak("Good Evening..")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('17ce118@charusat.edu.in', 'vishalshah1999')
    server.sendmail('17ce118@charusat.edu.in', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    
        #Logic for executing tasks based on query
        if 'this is' in query:
            speak("Hi, There...")
            wishPeople()
            speak("I'm Mike Nice to meet you")
        
        elif 'Hey' in query or 'hello' in query or 'hi' in query:
            speak("Hi, Surbhi .. How's Your Day ?? ")
              
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'who are you' in query:
            speak("I'm Mike. I'm an AI Robot")
            
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            #print(songs[random.randint(0,2)])
            os.startfile(os.path.join(music_dir, songs[random.randint(0,1)]))
            
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
            
        elif 'open sublime' in query:
             codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
             os.startfile(codepath)
        
        elif 'email to vishal' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "17ce118@charusat.edu.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I'm not able to send email")
                
        elif 'quit' in query or 'bye' in query:
            speak("I'm Quitting, Thanks for using")
            sys.exit()