import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

print("initializing moses")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("hi , i am moses , how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"master said: {query}\n")

    except Exception as e:
        print("Say that again please")
        speak("say that again please...")
        return "None"
    return query


query = takeCommand()

if 'wikipedia' in query.lower():
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)

elif 'youtube' in query.lower():
    webbrowser.open("youtube.com")
    url = "youtube.com"
    #chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
    # webbrowser.get(chrome_path).open(url)
elif 'google' in query.lower():
    webbrowser.open("google.com")
    url = "google.com"
elif 'discord' in query.lower():
    webbrowser.open("discord.com")
    url = "discord.com"
elif 'music' in query.lower():
    songs_dir = "C:\\Users\\ACER\\Downloads\\music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
elif 'time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f" the time is {strTime}")
