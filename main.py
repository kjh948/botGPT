import kws
import subprocess  # needed to run external program raspistill
import speech_recognition as sr
import signal
import sys
import POE
import tts

asr = sr.Recognizer()

def run_once():
    print("waiting wakeup word")
    # kws.wait_keyword()
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
        prompt = "한문장으로 대답해주세요. "
        response = POE.ask(prompt + str)
        print("what gpt said: "+response)
        tts.runtts_google("네네. "+response)
    except:
        str = 'ERROR'
        print( "can't understand")
        return

def signal_handler(signal, frame):
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    while 1:
        run_once()
         