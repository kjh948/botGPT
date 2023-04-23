from pocketsphinx import LiveSpeech


# speech = LiveSpeech(lm=False,  kws='voice_cmd.kwlist', dic='voice_cmd.dic')
# speech = LiveSpeech(lm=False, keyphrase='maria', kws_threshold=1e-17)
# for phrase in speech:
#     print(phrase)
#     # print(speech.segments(detailed=True))
#     speech.segments(detailed=True)
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
    # global speech
    speech = LiveSpeech(lm=False, keyphrase='maria', kws_threshold=1e-14)
    for phrase in speech:
        print(phrase)
        phrase.segments(detailed=True)
        return


if __name__ == "__main__":
    print("main function")
    wait_keyword()