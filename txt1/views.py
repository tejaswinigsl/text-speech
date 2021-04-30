from django.shortcuts import render,redirect
import pyttsx3
from gtts import gTTS
import playsound
import random
import os
# Create your views here.
def home(request):
    return render(request,'home.html')

'''def some(request):
    value=request.POST['sample']
    obj=pyttsx3.init()
    obj.say(value)
    obj.runAndWait()
    return redirect('/')'''

def some(request):

    lang=request.POST['lang']
    value=request.POST['sample']
    try:
        tts=gTTS(text=value,lang=lang)
        r=random.randint(1,20)
        audio_file='audio'+str(r)+'.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)
        return redirect('/')
    except:
        return redirect('/')
    



