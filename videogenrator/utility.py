from googletrans import Translator
from pydub import AudioSegment
from typing import TextIO

import os
import re
import json
import logging



def convert_to_wave(audio_path:str ) -> str:
    """
    Converts an audio file to WAV format and deletes the original file.

    This function takes the path of an audio file, converts it to WAV format,
    saves it with the same name but a `.wav` extension, and removes the original file.

    Args:
        audio_path (str): The file path of the input audio file to be converted.

    Returns:
        str: The file path of the newly created WAV file.
    """
    audio = AudioSegment.from_file(audio_path)
    wave_path = "".join(audio_path.split('.')[:-1])+".wav"
    audio.export(wave_path, format = "wav")
    os.remove(audio_path)
    return wave_path

def is_path(text):
    """
    Determine if a given text is formatted like a path.
    This does not check if the path is valid, only if it resembles a path format.
    
    Args:
        text (str): The text to evaluate.
        
    Returns:
        bool: True if the text looks like a path, False otherwise.
    """
    if "/" in text or "\\" in text:
        return True
    
    if re.search(r'\.\w+$', text):
        return True
    
    if re.match(r'^[a-zA-Z]:\\', text):
        return True
    
    return False

def translate_text(text, target_language='en'):
    translator = Translator()
    detected_language = translator.detect(text).lang
    translated = translator.translate(text, src=detected_language, dest=target_language)

    return translated.text



