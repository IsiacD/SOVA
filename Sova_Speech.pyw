#This Is Project SOVA

import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text To Speech Conversion
def speak(text):
    """Used to speak whatever is passed to it"""


    engine.say(text)
    engine.runAndWait()

#Greeting dependant on time
from datetime import datetime

def greet_user():
    """Greets the user according to the time"""


    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 21):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I help you?")

# Recognize my Voice
import speech_recognition as sr
from random import choice
from utils import opening_text

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        key_words = ['exit',
                    'stop',
                    'sleep',
                    'done',
                    'nothing']
        try: 
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-us')
            if any(x in query for x in key_words):
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    speak(f'Good night sir, take care!')
                else:
                    speak(f'Have a good day sir!')
                    exit()
            else:
                speak(choice(opening_text))
        except Exception:
            speak('Sorry, I could not understand. Could you please repeat that?')
            query = 'None'
        return query
   

import requests
from functions.online_ops import find_my_ip, get_latest_news, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia
from functions.os_ops import open_steam, open_Discord, open_Spotify, open_Valorant, open_Code, open_Fallout4, open_Opera, open_Chrome
from pprint import pprint


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'ip' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
           

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
            

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
           

        elif 'google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)
         

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(get_latest_news(), sep='\n')
       

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
         
 
        elif 'time' in query:
            strTime=datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            speak(f"To make it easier, I'm printing it below.")
            print(f"{strTime}")
       

        elif 'Discord' in query:
            open_Discord()
       

        elif 'Valorant' in query:
            open_Valorant()
       

        elif 'Chrome' in query: 
            open_Chrome()
       

        elif 'Fallout' in query:
            open_Fallout4()
         

        elif 'Opera' in query:
            open_Opera()
         

        elif 'music' in query:
            open_Spotify()
         

        elif 'code' in query:
            open_Code()

        elif 'games' in query: 
            open_steam()
        