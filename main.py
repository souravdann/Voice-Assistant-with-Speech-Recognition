import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia


listener = sr.Recognizer()
terzan = pyttsx3.init()
voices = terzan.getProperty('voices')
terzan.setProperty('voices',voices[1].id)

def talk(text):
    terzan.say(text)
    terzan.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'terzan' in command:
                command = command.replace('terzen', '')    


    except:
        pass
    return command

def run_terzen():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is '+ time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'name' in command:
        talk('My name is tarzan created by Sourav Dan')
    elif 'hi' in command:
        talk('Hello sourav how can i help you')
    elif 'open' in command:
        pywhatkit.search(command)
        print('Opening...')
    elif 'search' in command:
        pywhatkit.search(command)
    elif 'doing' in command:
        talk('I am Wating For You Sourav')
    elif 'dance with' in command:
        talk('No Actually i need permission from sourav')    
    else:
        talk('sorry sir please say it again')

while True:
    run_terzen()