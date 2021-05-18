#!/usr/bin/python3

from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import datetime
import pyfiglet
import requests
import keyboard
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup as bs
import pyperclip

global search_query
search_query = 'test'

print('#Usage\n#say"open youtube.com" to open youtube.\n#say "exit" to exit the program.')

#fuction takes video selection and returns video URL
def video_list(query,number):
    
    num = int(number)
    num -=1
    videos = []
    results = YoutubeSearch(query, max_results=10).to_dict()
    for i in results:
        tmp = i['url_suffix']
        videos.append(tmp)
    return videos[num]

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

    elif 'search' in storeCommand: #types search query in youtube search bar
        reg = re.search('search (.+)', storeCommand)
        if reg:
            keyboard.send("/")
            keyboard.send('Command+a')
            keyboard.send('delete')
            keyboard.write(reg.group(1))
            keyboard.send('enter')
            global search_query
            search_query = reg.group(1)
        else:
            pass

    elif 'select option' in storeCommand:
        reg = re.search('select option (.+)', storeCommand)
        if reg:
            video_choice = video_list(search_query,reg.group(1))
            keyboard.send('Command+l') #url searchbar
            keyboard.send('delete')
            print(video_choice +'printed')
            keyboard.write('https://www.youtube.com'+ video_choice) #writes url_suffix for selected video from search results
            keyboard.send('enter')
        else:
            pass

    elif 'play' in storeCommand:  #play or pause video
        reg = re.search('play', storeCommand)
        if reg:
            keyboard.send("space")            
        else:
            pass
        
    elif 'speed up' in storeCommand: #speeds up video
        reg = re.search('speed up', storeCommand)
        if reg:
            keyboard.send("Shift+>")            
        else:
            pass

    elif 'slow down' in storeCommand: #slows down video
        reg = re.search('slow down', storeCommand)
        if reg:
            keyboard.send("Shift+<")            
        else:
            pass

    elif 'go forward' in storeCommand: #skips 10 seconds forward
        reg = re.search('go forward', storeCommand)
        if reg:
            keyboard.send('l')
        else:
            pass

    elif 'go back' in storeCommand: #skips 10 seconds backward
        reg = re.search('go back', storeCommand)
        if reg:
            keyboard.send('j')
        else:
            pass

    elif 'full screen' in storeCommand: #makes video full screen
        reg = re.search('full screen', storeCommand)
        if reg:
            keyboard.send('f')
        else:
            pass
    elif 'skip' in storeCommand: #skips ad
        reg = re.search('skip', storeCommand)
        if reg:
            keyboard.send('Tab+Shift+Enter')
        else:
            pass
        
    elif 'exit' in storeCommand:
        exit()

banner()
greetTime()
while True:
    virtualAssist(ownerCommand())
    







        
    
    
        
        
