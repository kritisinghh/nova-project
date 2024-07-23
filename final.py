# pip install speechrecognition pyaudio pyttsx3 pyjokes requests wikipedia

import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pyjokes
from datetime import datetime
import wikipedia
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR_NEWS_API_KEY"
weatherapi = "YOUR_WEATHER_API_KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def news():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")    
    if r.status_code == 200:
        data = r.json()
        articles = data.get('articles', [])
        for article in articles:
            speak(article['title'])

def music(song):
    music_list = {
        "symphony": "https://www.youtube.com/watch?v=aatr_2MstrI",
        "closer": "https://www.youtube.com/watch?v=PT2_F-1esPk",
        "stay": "https://www.youtube.com/watch?v=h--P8HzYZ74"
    }
    link = music_list.get(song.lower())
    if link:
        webbrowser.open(link)

def weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherapi}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        weather_desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature - 273.15:.2f}°C with {weather_desc}.")
    else:
        speak("City not found.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def tell_time():
    now = datetime.now().strftime("%H:%M")
    speak(f"The current time is {now}")

def tell_date():
    today = datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {today}")

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except Exception as e:
        speak("Sorry, I couldn't find any information on that topic.")

def set_alarm(alarm_time):
    speak(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            speak("Time to wake up!")
            break
        time.sleep(30)

def process_command(c):
    if 'open google' in c.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://youtube.com')
    elif 'open facebook' in c.lower():
        webbrowser.open('https://facebook.com')
    elif 'open linkedin' in c.lower():
        webbrowser.open('https://linkedin.com')
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]
        music(song)
    elif 'news' in c.lower():
        news()
    elif 'weather' in c.lower():
        city = c.lower().split(" ")[1]
        weather(city)
    elif 'tell me a joke' in c.lower():
        tell_joke()
    elif 'time' in c.lower():
        tell_time()
    elif 'date' in c.lower():
        tell_date()
    elif 'wikipedia' in c.lower():
        query = c.lower().split('wikipedia')[-1].strip()
        search_wikipedia(query)
    elif 'set alarm' in c.lower():
        alarm_time = c.lower().split('set alarm for')[-1].strip()
        set_alarm(alarm_time)
    elif 'exit' in c.lower():
        speak('Goodbye!!!')
        return False
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Nova..")

    # Listen for the wake word "Nova"
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == 'nova':
                speak('Yes, how may I help you?')
                # Listen for Command
                with sr.Microphone() as source:
                    print("Nova Active..")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    if not process_command(command):
                        break
        except Exception as e:
            print(f'Error: {e}')
