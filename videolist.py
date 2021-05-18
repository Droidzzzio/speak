from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import datetime
import pyfiglet
###### Chris Rivas start
import requests
import keyboard
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup as bs
import pyperclip

# global variable
# variable = 'test'
# print(variable)
# n = '5'



# def video_list(query,number):
    
#     num = int(number)
#     num -=1
#     videos = []
#     global variable
    
#     variable = 'change'
#     results = YoutubeSearch(query, max_results=10).to_dict()
    
#     for video in results:
#         tmp = video['url_suffix']
        
#         videos.append(tmp)
#     return videos[num]


# url = video_list('this',n)
# print(url)
# print(variable)
# videos = []
  
# results = YoutubeSearch("this is a test", max_results=10).to_dict()
# print(results)
# for i in results:
#     tmp = i['url_suffix']
#     videos.append(tmp)
#     print(tmp)

# from youtubesearchpython import VideosSearch

# videosSearch = VideosSearch('No Copy right Sounds', limit = 2)

# print(videosSearch.result())

import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : 'this is a test'})

html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
print(html_content)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("http://www.youtube.com/watch?v=" + search_results[0])