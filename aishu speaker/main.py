import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
command = ""


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('what can i do for u')
            command = input("Say to aishu")
            print(command)


            if 'aishu' in command:
                command = command.replace('aishu', '')
                print(command)
            else:
                command = "stop"
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song , use_api=True)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who ' in command:
        person = command.replace('who ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what' in command:
        srh = command
        pywhatkit.search(srh)
        talk("buddy see in google")
    elif 'bye' in command:
        talk('This is Aishu signing off. Have a good day')
        exit()
    else:
        talk('Please say the command again to aishu.')

talk('hi i am aishu')
while True:
    run_alexa()
    continue