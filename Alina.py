import speech_recognition as sr
import pyttsx3
import datetime 
import requests
import os
import serpapi
from dotenv import load_dotenv
load_dotenv()


recognizer=sr.Recognizer()
speech=pyttsx3.init()

api_key=os.getenv('key')
client=serpapi.Client(api_key=api_key)


def speaking(text):
    speech.say(text)
    speech.runAndWait()

with sr.Microphone() as source :
    
 while True:
     print("Listening ...")
     audio=recognizer.listen(source)

     try:
        text=recognizer.recognize_google(audio)
        print(f'You said : {text} ')
        
        if "hello" in text.lower():
            speaking("Hello , how can i help you")
        
        if "time" in text.lower():
          x = datetime.datetime.now()
          speaking('The time is '+x.strftime("%X"))  
        
        if"stop" in text.lower():
            break  
        
        if "search" in text.lower():
            result=client.search(
                q=text,
                engine="google",
                
            )
            speaking("Here is what i found ")
            for item in result['organic_results']:
                print(item['title'])
                print(item['link'])
                print(item['snippet'])
                print("------------------")
            

     except:
        speaking('Sorry i could not recognize your voice')









