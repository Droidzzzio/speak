#!/usr/bin/python3


from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import datetime
import pyfiglet

print('#Usage\n#say"open site.com" to open any website.\n#say "exit" to exit the program.')

def banner():
    ascii_banner = pyfiglet.figlet_format("SPEAK")
    print(ascii_banner)


#program will greet You by wishing
def greetTime():
    speak('Hello Sir!!!')
    currentTime = datetime.datetime.now()
    print(currentTime)
    if currentTime.hour < 12:
        print('Good Morning Sir')
    elif 12 <= currentTime.hour < 18:
        print('Good Afternoon master')
    else:
        print('Good Evening Boss')


#audio will be passed as arguement in this function
def speak(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)       #command to make python speak
        

#function which listen for commands given by owner
def ownerCommand():
        r = sr.Recognizer() # r variable declared in which our command will be stored
        with sr.Microphone() as source:
            print('I am Ready to serve you now')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            storeCommand = r.recognize_google(audio).lower()
            print('You asked for this site : ' +storeCommand + '\n')

            #except is given in case there is some unrecognizable speech if recieved it will continue to loopback to the main function and will listen to you again
        except sr.UnknownValueError: 
            print('I am sorry , didn\'t heard what you said')
            storeCommand = ownerCommand();

        return storeCommand

#this function will create if statements for executing all the commands asked to the program
def virtualAssist(storeCommand):
    if 'open' in storeCommand:
        reg = re.search('open (.+)', storeCommand)
        if reg:
            domain = reg.group(1) #group(1) is used in python to retrieve the captured string
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Right away sir !')
        else:
            pass

    elif 'exit' in storeCommand:
        exit()
        

banner()
greetTime()
while True:
    virtualAssist(ownerCommand())
    







        
    
    
        
        
