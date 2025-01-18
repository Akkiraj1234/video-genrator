from .TTS import Tts
from .assets import TTS_INFO




class Generate:
    def __init__(self, script, video, audio):
        self.status_code = True
        self.error = "None"
        self.path = None
        
        self.script = script
        self.video = video
        self.audio = audio
    
    def __enter__(self):
        self.initialize_component()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False

    def initialize_component(self):
        self.tts = Tts(TTS_INFO)
    
    def execute(self):
        audio_path = Tts.create(self.script)
    
    
    
        
    