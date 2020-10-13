import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import random
import webbrowser
import wolframalpha
import sys


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('WQH7P3-PU9ELJ92WW')

voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
        
wishMe()

speak('Hello Suraj Sir, I am your digital assistant LARVIS!')
speak('How may I help you Sir?')

def takeCommand():
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
    

    
if __name__ == "__main__":
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in query:
            speak('Okay')
            webbrowser.open('www.youtube.com')
            
        elif 'open google' in query:
            speak('Okay')
            webbrowser.open('www.google.com')
            
        elif 'open facebook' in query:
            speak('Okay')
            webbrowser.open('www.facebook.com')
            
        elif 'open amazon' in query:
            speak('Okay')
            webbrowser.open('www.amazon.com')
            
        elif 'open flipkart' in query:
            speak('Okay')
            webbrowser.open('www.flipkart.com')
            
        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('https://web.whatsapp.com/')
                  
        elif 'open linkedin' in query:
            speak('okay')
            webbrowser.open('https://www.linkedin.com/in/suraj-keshri-511b65166/')
            
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            
        elif 'play music' in query:
            speak('Okay')
            music_dir = 'C:\\Users\\user\\OneDrive\\Desktop\\Special Folder\\Musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            music = ['Ve Maahi', 'Mere Sohneya', 'Luka Chuppi', 'Hawa_Banke', 'Bekhayali']
            random_music = music_dir + random.choice(music) + '.mp3'
            os.system(random_music)
            
            speak('Okay, here is your music! Enjoy!')
            
        elif 'time' in query:
            speak('Okay')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
            
            
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



