
#pip install speechrecognition pyaudio
# pip install setuptools
import speech_recognition as sr
import webbrowser
#pip install pyttsx3
import pyttsx3

import music_library

#pip install pocketsphinx

import requests

# from openai import OpenAI
## pip install openai
 
# from gtts import gTTS
# import pygame


# import datetime
# import time

# import smtplib
# from email.mime.text import MIMEText

# pip install pyjokes
import pyjokes

from datetime import datetime

import wikipedia

import time

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="017c7e79c3794f02a64dd09b61b64baa"
weatherapi="b398bdb815598344527583a2bd9b422a"

def speak(text):
    engine.say(text)
    engine.runAndWait() 
'''
def aiprocess(command):
    client = OpenAI(api_key="sk-proj-WxSl7ehGk2PnwmzCHcDwT3BlbkFJMj6bYTk9jG1bqZaFTcj")
    completion = client.chat.completions.create(model="gpt-3.5-turbo",messages=[    {"role": "system", "content": "You are a virtual assistant named Nova, skilled in general tasks like Alexa, Google Cloud"},
    {"role": "user", "content": command}])

    return completion.choices[0].message.content
'''
'''
def speak_new(text):
    tts=gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
''' 
def news():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")    
    if r.status_code == 200:
        data=r.json()
        articles=data.get('articles',[])
        for article in articles:
            speak(article['title'])

def music(song):
    music_list={"symphony":"https://www.youtube.com/watch?v=aatr_2MstrI",
       "closer":"https://www.youtube.com/watch?v=PT2_F-1esPk",
       "stay":"https://www.youtube.com/watch?v=h--P8HzYZ74"}
    link=music_list[song]    
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

# def set_reminder(reminder, reminder_time):
#     reminder_time = datetime.datetime.strptime(reminder_time, "%Y-%m-%d %H:%M:%S")
#     while True:
#         if datetime.datetime.now() >= reminder_time:
#             speak(f"Reminder: {reminder}")
#             break
#         time.sleep(30)   #This checks after every 30 secs


# def send_email(subject, body, to_email):
#     from_email = "kritiiffco@gmail.com"
#     password = "your_password"

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = from_email
#     msg["To"] = to_email

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(from_email, password)
#         server.sendmail(from_email, to_email, msg.as_string())

# def load_tasks():
#     if os.path.exists(tasks_file):
#         with open(tasks_file, "r") as file:
#             return json.load(file)
#     return []

# def save_tasks(tasks):
#     with open(tasks_file, "w") as file:
#         json.dump(tasks, file)

# def add_task(task):
#     tasks = load_tasks()
#     tasks.append({"task": task, "done": False})
#     save_tasks(tasks)
#     speak(f"Task '{task}' added to your to-do list.")

# def mark_task_as_done(task_number):
#     tasks = load_tasks()
#     if 0 <= task_number < len(tasks):
#         tasks[task_number]["done"] = True
#         save_tasks(tasks)
#         speak(f"Task {task_number + 1} marked as done.")
#     else:
#         speak("Invalid task number.")

# def list_tasks():
#     tasks = load_tasks()
#     if not tasks:
#         speak("Your to-do list is empty.")
#     else:
#         for i, task in enumerate(tasks):
#             status = "done" if task["done"] else "not done"
#             speak(f"Task {i + 1}: {task['task']} - {status}")

def tell_joke():
    joke=pyjokes.get_joke()
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
        song=c.lower().split(" ")[1]
        music(song)
        
    elif 'news' in c.lower():
        news()
        
    elif 'weather' in c.lower():
        w=c.lower().split(" ")[2]
        weather(w)
    # elif 'set reminder' in c.lower():
    #     parts = c.lower().split("reminder to")
    #     reminder = parts[-1].split("at")[0].strip()
    #     reminder_time = parts[-1].split("at")[-1].strip()
    #     set_reminder(reminder, reminder_time)
    # elif 'send email' in c.lower():
    #     parts = c.lower().split("send email")
    #     details = parts[-1].split("to")
    #     subject = details[0].split("subject")[1].strip()
    #     body = details[0].split("body")[1].strip()
    #     to_email = details[-1].strip()
    #     send_email(subject, body, to_email)
    # elif 'add task' in c.lower():
    #     task = c.split("add task")[-1].strip()
    #     add_task(task)
    # elif 'mark task' in c.lower() and 'done' in c.lower():
    #     task_number = int(c.split("mark task")[-1].split("done")[0].strip()) - 1
    #     mark_task_as_done(task_number)
    # elif 'list tasks' in c.lower():
    #     list_tasks()
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
        #Let OpenAI handle the request
        output=aiprocess(c)
        speak(output)
    

        
        
        

if __name__=="__main__":
    speak("Initializing Nova..")

    #listen for the wake word "Nova"
    while True:
        #obtain audio from microphone
        r=sr.Recognizer()
        
        
        print('Recognizing...')
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower()=='nova'):
                speak('Yes how may I help you!!')
                #Listen for Command
                with sr.Microphone() as source:
                    print("Nova Active..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    process_command(command)


        except Exception as e:
            print(' Error {0}'.format(e))
            
    