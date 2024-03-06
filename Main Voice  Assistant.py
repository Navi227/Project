import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import webbrowser
from bs4 import BeautifulSoup
import requests
import json

assis_name="Mavis"
boss_name="Naveena"
def say(text):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing......")
            text=r.recognize_google(audio,language='en-in')
            print(f"User Said :{text}\n")
        except Exception as e:
            print(e)
            print("can not recognize your voice")
            return "None"
        return text

def get_temperature():
    city = text.split("in", 1)
    soup = BeautifulSoup(requests.get(f"http://www.google.com/search?q=weather+in+{city[1]}").text, "html.parser")
    region = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
    temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    day = soup.find("div", class_="BNeawe tAd8D AP7Wnd")
    weather = day.text.split("m", 1)
    temperature = temp.text.split("c", 1)
    say("Its Currently" + weather[1]+ " and " + temperature[0] + "Celcius" + "in" + region.text)
    print("Its Currently" + weather[1]+ " and " + temperature[0] + "Celcius"+ "in" + region.text)
    return temperature
    
def tell_jokes():
    joke=pyjokes.get_joke()
    return joke

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time

def respond(text):
    if 'hi' in text:
        say("Hi Mam! Welcome to India")
    elif "who are you" in text:
        say("My name is {} i am your voice assistant".format(assis_name))
    elif "good morning" in text:
        say("A warm" +text)
        say("How are you"+boss_name+"?")
    elif "I am fine" in text:
        say("oh really good")
    elif "who I am" in text:
        say("if you talk then definately your human.")
    elif 'what is your boss name' in text:
        say("My name is "+assis_name+"!"+"My Boss Name is "+boss_name)
    elif 'where am I' in text:
        say("you are in salem")
    elif 'thank you so much' in text:
        say("it's my pleasure Sir!")
    elif 'fine' in text or "good" in text:
        say("It's good to know that your fine")
    elif 'tell me joke' in text:
        engine2=pyttsx3.init()
        engine2.setProperty('rate',150)
        engine2.say(tell_jokes())
        engine2.runAndWait()
        print("The Joke is : ",tell_jokes())
    elif 'current time' in text:
        engine3=pyttsx3.init()
        engine3.setProperty('rate',150)
        engine3.say(get_time())
        engine3.runAndWait()
        print("The Time is : ",get_time())
    elif "temperature in" in text:
        engine4=pyttsx3.init()
        engine4.setProperty('rate',150)
        engine4.say(get_temperature())
        engine4.runAndWait()
        
while True:
    text = takecommand()
    respond(text)





















    
