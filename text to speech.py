from gtts import gTTS 
from flask import Flask, render_template, Response, request, redirect, url_for
import os


msg=form.user_message.data
  
mytext = 'Welcome to geeksforgeeks!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 