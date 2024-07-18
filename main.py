import os.path
import random

import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import openai


Api_key=open("api_key","r").read()
openai.api_key = Api_key
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

def get_openai_response(prompt):
    text= f"Open AI response for Prompt: {prompt} \n ********************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":prompt}
        ],
        max_tokens=150
    )
    print(response['choices'][0]['message']['content'].strip())
    text+=response['choices'][0]['message']['content'].strip()
    if not os.path.exists("Openai"):
        os.mkdir("openai")

    with open(f"openai/prompt-{random.randint(1,23433432)}",'w') as f:
        f.write(text)
    return(response['choices'][0]['message']['content'].strip())
if __name__=='__main__':
    print('PyCharm')
    say('Hello I m A.I. made by Siya')
    say('Hello Siya How are You')
    while True:
     text=takeCommand()
     sites=[["youtube","https://www.youtube.com"],
           ["google","https://www.google.com"],
           ["facebook","https://www.facebook.com"],
           ["instagram","https://www.instagram.com/"],
           ["gfg","https://www.geeksforgeeks.org/"],
           ["Leetcode","https://leetcode.com/"],
           ["spotify","https://open.spotify.com/"],
           ["pinterest","https://www.pinterest.com/pinterest/"],]
     for site in sites:
        if f"Open {site[0]}".lower() in text.lower():
         say(f"Opening {site[0]} Siya.....")
         webbrowser.open(site[1])
     if "open music" in text:
          musicpath="https://www.youtube.com/watch?v=RY7qX-2JQiI"
          say(f"Opening Music Siya.....")
          webbrowser.open(musicpath)

     if "the time" in text:
         strfTime=datetime.datetime.now().strftime("%H:%M:%S")
         say(f"Siya the time is {strfTime}")

     if "using ai".lower() in text.lower():
         openai_response = get_openai_response(text)
         say (openai_response)
