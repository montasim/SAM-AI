#   for speak
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import subprocess
import os
import platform
from sys import platform as _platform
import smtplib
import random

#   start AI voice
engine = pyttsx3.init('sapi5')
#   use windows build in voices
voices = engine.getProperty('voices')
#   shows windows build in voice for specific id
#   print(voices[1].id)
engine.setProperty('voice', voices[0].id)


#   speak what is inside of this function
def speak(audio):
    """
    speak() function will say what is inside of this function.
    :param audio:
    :return:
    """
    #   say audio string
    engine.say(audio)
    #   say audio and wait for next input
    engine.runAndWait()


#   wish me as time goes
def wish_me():
    """
    wish_me() function will wish according to time. As time goes it will wish "Good Morning!", "Good Afternoon!" and
    "Good Evening!". After wishing it will say "This is SAM. Ask me anything".
    :return:
    """
    #   get current time as 24 hour format
    hour = int(datetime.datetime.now().hour)

    speak("Hello sir!")

    #   wish condition
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    #   this will always execute when inside wish_me() function
    speak("Ask me anything.")


def take_command():
    """
    take_command() function takes microphone input from the user and returns string output
    :return:
    """
    #   recognize class will help to recognize audio
    r = sr.Recognizer()
    #   recognize from microphone
    with sr.Microphone() as source:
        #   when recognizing from microphone print "Listening..."
        print("Listening...")
        #   time gap between a phrase. here considered 1 second.
        r.pause_threshold = 1
        #   take input as audio from audio source
        audio = r.listen(source)

        #   when error occurs try using this
        try:
            #   recognizing command
            print("Recognizing...")
            # Using google for voice recognition.
            user_query = r.recognize_google(audio, language='en-in')
            # User query will be printed.
            print(f"User said: {user_query}\n")

        except Exception as e:
            #   print current exception
            # print(e)
            # Say that again will be printed in case of improper voice
            print("Say that again please...")
            # None string will be returned
            return "None"

        #   takes audio as input and convert into string then return that string
        return user_query


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('montasim.backup@gmail.com', 'zrh8Hw77riiSlB35ZmVHd')
    server.sendmail('montasimmamun@gmail.com', to, content)
    server.close()

#   main function
if __name__ == "__main__":

    #   calling wish_me() function
    wish_me()
    #   run infinite loop
    while True:
        # if 1:
        # Converting user query into lower case
        query = take_command().lower()

        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path), 1)

        # Logic for executing tasks based on query
        # if wikipedia found in the query then this block will be executed
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')

            try:
                #   try to load the wikipedia page
                query = query.replace("wikipedia", "")
                #   determine sentence length from wikipedia
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                #   showing result
                print(results)
                #   speaks result
                speak(results)

            except wikipedia.exceptions:
                speak("Sorry! Not found in wikipedia!")
                # if error occurs, ignore it and continue
                continue

        elif 'open code' in query:
            os.startfile('C:\\Program Files\\Microsoft VS Code\\Code.exe')

        elif 'open music' in query:
            os.startfile('C:\\Program Files (x86)\\MusicBee\\MusicBee.exe')

        elif 'play music' in query:
            music_dir = 'D:\\ENTERTAINMENT\\AUDIO SONGS\\ENGLISH AUDIO SONGS\\Time Capsule\\Adele\\21'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open files' in query:
            os.startfile('D:\\')
            continue

        elif 'exit' in query:
            exit()

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "montasimmamun@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry sir!. I am not able to send this email")

        elif 'the time' in query:
            #   says current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab("https://stackoverflow.com/")

        elif 'open github' in query:
            webbrowser.get('chrome').open_new_tab("https://github.com/")

        elif 'open facebook' in query:
            webbrowser.get('chrome').open_new_tab("https://facebook.com/")
