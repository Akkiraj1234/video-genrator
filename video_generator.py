from .TTS import Tts
from .assets import TTS_INFO, Download_Path




class Generate:
    def __init__(self, script:str, video:str, audio:str) -> None:
        self.status_code = True
        self.error = None
        self.path = None
        
        self.script = script
        self.video_path = video
        self.audio_path = audio
    
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
        audio_path = self.tts.create(self.script)
    
    
    
        
    