from .error import InternetError
from .assets import TTS_INFO, Temporary_File_Path, clear_current_session
from .utility import translate_text, os

from gtts import gTTS, gTTSError

# ducktyping rules for TTS function
# 1. every function should have script and lang argument
#   - script: the text to create tts
#   - lang : in which language to create the tts

# why we using the getpid for tts_output name 
    # - can only contain 1 audio file for 1 python inteparator
    # - can remove for current python inteparator all fille created
    # - update new tts in get_tts method 
    
# Available tts
# 1. gtts
# 2. 

def get_file_path() -> str:
    audio_file_name = f"tts_output_{os.getpid()}_audio.mp3"
    audio_file_path = os.path.join(Temporary_File_Path, audio_file_name)
    
    return audio_file_path


def TTS_gtts(script:str, tts_info:dict, lang:str = "en") -> str:
    """
    Generate a Text-to-Speech (TTS) audio file and save it in the temporary file path.

    Args:
        script (str): The text to be converted to speech.
        lang (str, optional): The language of the text. Defaults to "en".

    Returns:
        str: The path of the generated audio file.
    """
    try:
        tts = gTTS(
            text= script,
            lang= lang,
            slow= tts_info.get("slow",False),
            lang_check= True
        )
        audio_file_path = get_file_path()
        tts.save(audio_file_path)
        return audio_file_path
    
    except gTTSError as e:
        raise InternetError(e)


def get_tts(name:str) -> callable:
    info = {
        "gtts": TTS_gtts
    }
    
    return info.get(name,TTS_gtts)
    

class Tts:
    def __init__(self, TTS_INFO:dict):
        self._load_info(TTS_INFO)
    
    def _load_info(self, TTS_INFO) -> None:
        # if not available default to gtts
        self.tts = get_tts(TTS_INFO["use_services"])
    
    def create(self, script, lang = "en") -> str:
        translated_text = translate_text(script, lang)
        return self.tts(translated_text, lang, TTS_INFO)
        
        

    
    
        
