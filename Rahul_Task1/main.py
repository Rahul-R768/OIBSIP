import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
from datetime import datetime
import time
import os
import requests


def speak(text):
    print(text)
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)

    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio=recognizer.listen(source,timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""
    
    try:
        print("Recognizing...")
        command=recognizer.recognize_google(audio)
        print("you said:",command)
        return command.lower()
    except Exception as e:
        print(f"{e}\nSorry, I did not understand. Please try again.")
        return ""


def greet_user():
    hour=datetime.now().hour
    if hour<12:
        speak("Good Morning Rahul!")

    elif 12<=hour<18:
        speak("Good Afternoon Rahul!")

    else:
        speak("Good Evening Rahul!")

    speak("I am your voice assistant")


def execute_command(command):

    if "youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("opening google")
        webbrowser.open("https://www.google.com")

    elif "github" in command:
        speak("opening github")
        webbrowser.open("https://www.github.com") 

    elif "time" in command:
        current_time=datetime.now().strftime("%I:%M:%S %p")
        speak(f"The current time is {current_time}")    

    elif "date" in command:
        current_date=datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        search_query=command.replace("search","").strip()
        if search_query:
            speak(f"searching for {search_query} on google")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please specify what you want to search for.")

    elif  "who is" in command or "what is" in command or "tell me about" in command or "meaning" in command or "explain" in command:

        topic=command

        topic=topic.replace("who is","").strip()
        topic=topic.replace("what is","").strip()
        topic=topic.replace("tell me about","").strip()
        topic=topic.replace("meaning","").strip()
        topic=topic.replace("explain","").strip()

        try:
            info=wikipedia.summary(topic,sentences=2,auto_suggest=False)
            speak(info)

        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results for this topic. Please be more specific.")
      
        except Exception as e:
              print(e)
              speak("I could not find information,please try again.")

    elif "reminder" in command:
        speak("What should I remind you about")
        reminder=take_command()
        if reminder=="":
            speak("Please try again.")
            return True
        
        speak("Enter the reminder time in seconds?")
    
        try:
            seconds=int(input("Enter seconds: "))
        except ValueError:
            speak("Invalid input, please try again.")
            return True 
        speak(f"reminder set for {seconds} seconds")
              
        time.sleep(seconds)
        
        speak(f"Reminder: {reminder}")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "vs code" in command:
        speak("Opening visual studio code")
        os.system("code") 

    elif "weather" in command:
        API_KEY="your_api_key"

        speak("Which city would you like the weather report for?")
        city=take_command()
        try:
           url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
           response=requests.get(url)
           data=response.json()
           if str(data["cod"])!="200":
               speak("Sorry, I could not find the city weather details.")
               return True
           temperature=data["main"]["temp"]
           description=data["weather"][0]["description"]

           speak(f"The current weather in {city} is {description} with a temperature of {temperature}°C")
        except requests.exceptions.RequestException:
            speak("Internet connection error.")
            return True

    elif "hello" in command:
        speak("hello rahul, how can i help you.")

    elif "exit" in command or "quit" in command:
        speak("Thank you, Have a productive day ahead!")
        return False
    else:
        speak("Sorry, I did not understand that command.")        

    return True

greet_user()

running=True
while running:
    command=take_command()
    if command=="":
        continue
    running=execute_command(command)