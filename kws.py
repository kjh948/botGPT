from pocketsphinx import LiveSpeech


# speech = LiveSpeech(lm=False,  kws='voice_cmd.kwlist', dic='voice_cmd.dic')
# speech = LiveSpeech(lm=False, keyphrase='marie', kws_threshold=1e-20)
# for phrase in speech:
#     print(speech.segments(detailed=False))

# while(1):
#     try:
#         for phrase in speech:
#             print(speech.segments(detailed=False))
#             exit(1)
#     except:
#         print("error")

# for phrase in speech:
# # while(1):    
#     print(phrase.segments(detailed=False))

def wait_keyword():
    speech = LiveSpeech(lm=False, keyphrase='marie', kws_threshold=1e-20)
    
    for phrase in speech:
        phrase.segments(detailed=True)


if __name__ == "__main__":
    print("main function")
    wait_keyword()