import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib
import winsound
import cv2
import pyspeedtest
import speedtest
from googlesearch import search 
import sys
import wolframalpha
import random
from selenium import webdriver 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("system online..")       

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
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 3:
        query = takeCommand().lower()


 #for websites
    driver = webdriver.Chrome() 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
    
    if 'YouTube' in query.lower(): 
        speak("Opening in youtube") 
        indx = query.lower().split().index('youtube') 
        query = query.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        

    if 'open youtube' in query:
        speak("Opening youtube..")
        webbrowser.open('https://www.youtube.com/', new=2)

    elif 'open google' in query:
        webbrowser.open('https://www.google.com/', new=2)

    elif 'open insta' in query:
        webbrowser.open('https://www.instagram.com/', new=2)


    elif 'open facebook' in query:
        webbrowser.open('https://www.facebook.com/', new=2)


    elif 'play music' in query:
        Music_dir = 'D:\\samarth dada\\songs\\audio'
        songs = os.listdir(Music_dir)
        print(songs)
        os.startfile(os.path.join(Music_dir, songs [0]))


    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query: 
        codepath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

        
    elif 'play beep sound' in query:
        speak("Playing beep sound be ready.....")
        frequency = 2500
        duration = 5000
        winsound.Beep(frequency,duration)
            
    elif 'Destory yourself' in query:
        speak("I am really sorry sir ")
        exit()

    elif 'check internet status' in query:
        speak("checking downloading speed please wait..")
        strSpeed = st = speedtest.Speedtest()
        print(st.download())
        speak("sir our download speed is...")
        speak(st.download())
        speak("checking Uploading speed please wait")
        print(st.upload())
        speak("sir our upload speed is...")
        speak(st.upload())
        speak("checking our ping ...")
        servernames =[]   
        st.get_servers(servernames) 
        print(st.results.ping)
        speak("sir our ping is ..")
        speak(st.results.ping)

def search_web (query):
    try :
        if 'search' in query or 'play' in query: 
            # a basic web crawler using selenium 
            search_web(query) 



    except : 
        speak("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = takeCommand() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(query) 
            return 

        elif "who are you" in query: 
            speak('Hello, Mr.Sam. I am Vironika Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra')
            return       

          
takeCommand()