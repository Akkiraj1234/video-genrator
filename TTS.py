# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello, this is an offline TTS.")
# engine.runAndWait()


# print("Audio saved to output.wav")



# from gtts import gTTS

# text = "Hello, world! and a reality check no one loves you dummy :)"
# tts = gTTS(text=text, lang='en')
# tts.save("output.mp3")
# print("Audio saved as output.mp3")


class Tts:
    def __init__(self, TTS_INFO:dict):
        self._load_info()
    
    def _load_info(self, TTS_INFO):
        pass
    
    def create(self, script):
        pass
