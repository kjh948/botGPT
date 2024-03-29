import kws
import subprocess  # needed to run external program raspistill
import speech_recognition as sr
import signal
import sys
import poe_chatgpt
import tts
import os
import bard
asr = sr.Recognizer()

useBard = 1

def run_once():
    print("waiting wakeup word")
    kws.wait_keyword()
    subprocess.check_call('play sound/wakeup.mp3', shell=True,stderr=subprocess.STDOUT)
    try:
        subprocess.check_call('adinrec -lv 1000 -zc 200 rec.wav', shell=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print( "Ping stdout output:\n", e.output)
        return
    with sr.WavFile('rec.wav') as source:
        audio = asr.record(source)  # read the entire WAV file
    try:
        str = asr.recognize_google(audio, language='ko-KR')
        print(str)
        proc = subprocess.Popen('play sound/working.mp3 repeat 1000', shell=True, stdout=subprocess.PIPE    )
        print("pid = ", proc.pid)
        prompt = "한문장으로 대답해주세요. "
        if useBard:
            response = bard.ask(prompt + str)
        else:
            response = poe_chatgpt.ask(prompt + str)

        print("what gpt said: "+response)
        # os.killpg(os.getpgid(proc.pid), signal.SIGTERM)  # Send the signal to all the process groups
        # proc.kill()
        # proc.wait()
        # subprocess.check_call("kill -9 $(ps -ef | grep 'play sound' | awk '{print $2}')", shell=True)
        os.system('./kill_sound.sh')

        tts.runtts_google("네네. "+response)
    except:
        subprocess.check_call('play sound/error.mp3', shell=True,stderr=subprocess.STDOUT)
        str = 'ERROR'
        print( "can't understand")
        return

def signal_handler(signal, frame):
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    while 1:
        run_once()