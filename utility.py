import re
from googletrans import Translator

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



