import os
from gtts import gTTS
from .error import Internet_ERROR
from .assets import TTS_INFO, Temporary_File_Path, clear_current_session
from .utility import translate_text

# ducktyping rules for TTS function
# 1. every function should have script and lang argument
#   - script: the text to create tts
#   - lang : in which language to create the tts

# why we using the getpid for tts_output name 
    # - can only contain 1 audio file for 1 python inteparator
    # - can remove for current python inteparator all fille created
    # - update new tts in get_tts method 


def TTS_gtts(script:str, lang:str = "en") -> str:
    """
    Generate a Text-to-Speech (TTS) audio file and save it in the temporary file path.

    Args:
        script (str): The text to be converted to speech.
        lang (str, optional): The language of the text. Defaults to "en".

    Returns:
        str: The path of the generated audio file.

    Raises:
        Internet_ERROR: If there is a connectivity issue or any error during TTS generation.
    """
    try:
        tts = gTTS(
            text=script,
            lang=lang,
            slow=False,
            lang_check=True
        )
        audio_file_name = f"tts_output_{os.getpid()}.mp3"
        audio_file_path = os.path.join(Temporary_File_Path, audio_file_name)
        tts.save(audio_file_path)
        return audio_file_path

    except Exception as e:
        raise Internet_ERROR(f"An error occurred during TTS generation: {str(e)}")

def get_tts(name:str) -> callable:
    info = {
        "gtts": TTS_gtts
    }
    
    return info.get(name,TTS_gtts)
    



class Tts:
    def __init__(self, TTS_INFO:dict):
        self._load_info(TTS_INFO)
    
    def _load_info(self, TTS_INFO):
        self.tts = get_tts(TTS_INFO["use_services"])
    
    def create(self, script, lang = "en"):
        translated_text = translate_text(script, lang)
        print(translated_text)
        self.tts(translated_text, lang)
        
        

    
    
        
