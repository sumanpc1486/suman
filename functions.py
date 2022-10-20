import speech_recognition as sr
import pyttsx3 
import datetime
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am VISTA boss.... Please tell me how may I help you") 

def hear():
    listener = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(src)

    try:
        print("Recognizing...")    
        query = listener.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query