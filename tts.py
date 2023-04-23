# -*- coding: utf-8 -*-
from gtts import gTTS
import time
import subprocess

lang='ko'
def runtts_google(utt):
    tts = gTTS(text=utt, lang=lang)
    tts.save('response.mp3')
    cmdln = 'play response.mp3 speed 1.3'    
    subprocess.check_call([cmdln], shell=True)

def runtts_google_robotic(utt):
    tts = gTTS(text=utt, lang=lang)
    tts.save('response.mp3')

    #cmdln = 'AUDIODEV=hw:2,0 play response.mp3 speed 1.3'
    #cmdln = 'AUDIODEV=hw:2,0 play response.mp3 chorus 0.4 0.8 20 0.5 0.10 2 -t echo 0.9 0.8 33 0.9 echo 0.7 0.7 10 0.2 echo 0.9 0.2 55 0.5 gain 25 speed 1.3'
    cmdln = 'play response.mp3 chorus 0.4 0.8 20 0.5 0.10 2 -t echo 0.9 0.8 33 0.9 echo 0.7 0.7 10 0.2 echo 0.9 0.2 55 0.5 gain 25 speed 1.3'
    
    # cmdln = 'play response.mp3 speed 1.3'
    #cmdln = 'play response.mp3 overdrive 10 echo 0.8 0.8 5 0.7 echo 0.8 0.7 6 0.7 echo 0.8 0.7 10 0.7 echo 0.8 0.7 12 0.7 echo 0.8 0.88 12 0.7 echo 0.8 0.88 30 0.7 echo 0.6 0.6 60 0.7 gain 8'
    subprocess.check_call([cmdln], shell=True)


def runtts_espeak(utt):
    # cmdln = 'espeak '+ '--stdout "' + utt + '" | play - chorus 0.4 0.8 20 0.5 0.10 2 -t echo 0.9 0.8 33 0.9 echo 0.7 0.7 10 0.2 echo 0.9 0.2 55 0.5 gain 20 speed 1.2'
    cmdln = 'espeak '+ utt
    # call external program ro take a picture
    subprocess.check_call([cmdln], shell=True)

