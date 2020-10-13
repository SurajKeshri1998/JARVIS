import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('WQH7P3-PU9ELJ92WW')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
        
greetMe()

speak('Hello Suraj Sir, I am your digital assistant LARVIS!')
speak('How may I help you Sir?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        #print("TEXT: "+r.recognize_google(audio , language = 'En-IN'))
        print("TEXT: "+r.recognize_google(audio))
        query = r.recognize_google(audio, language ='En-In')
        print(f"User Said: {query}\n")
        
    except Exception as e:
        print(e)
        
        print("Say that again please...")
        
        return "None"
        
    
    return query
    

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('https://www.facebook.com/')
            
        elif 'open amazon' in query:
            speak('okay')
            webbrowser.open('https://www.amazon.in/')
            
        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('https://web.whatsapp.com/')
            
        elif 'open linkedin' in query:
            speak('okay')
            webbrowser.open('https://www.linkedin.com/in/suraj-keshri-511b65166/')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("GMAIL", 'PASSWORD')
                    server.sendmail('YourUsername', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'C:\\Users\\user\\OneDrive\\Desktop\\Special Folder\\SongS'
            music = ['02 Tujhe Kitna Chahne Lage - Kabir Singh', '03 Photo - Luka Chuppi', '04 Ve Maahi - Kesari', '03 Bekhayali - Arijit Singh Version', 'Mera_Raanjha']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
#            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')