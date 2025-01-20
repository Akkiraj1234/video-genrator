# This file is responsible for adding subtitles to an audio file by estimating word durations 
# or using silence detection.

# Method 1: Word Duration Estimation
# -----------------------------------
# This method estimates word durations based on the total audio duration and the length of the text. 
# It assumes a uniform distribution of words across the audio and calculates timestamps accordingly.

# Formula:
# - Duration per word = Total audio duration / Number of words
# - Start time (i-th word) = (i - 1) * Duration per word
# - End time (i-th word) = i * Duration per word

# Issues with Word Duration Estimation:
# - Assumes uniform word spacing: The method assumes that each word will take roughly the same amount 
#   of time to speak, which may not always be accurate.
# - Inconsistent word gaps: If there are pauses, silences, or varied speech speeds between words, the 
#   timestamps might not align correctly with the actual audio.
# - Doesn't handle silence at the start or end: If there's silence before the first word or after the 
#   last word, it will not be accounted for, potentially causing an offset in the word timestamps.

# Method 2: Silence Detection
# ---------------------------
# This method analyzes the audio file to detect periods of speech and silence. It identifies the start 
# and end points of spoken segments and trims or analyzes these intervals.

# Formula:
# - Amplitude < Silence Threshold: Marks a segment as silence.
# - Speech Segments = [(Start time, End time) for all non-silent segments]
# - Trimmed Audio = Audio without silent segments at the start and end.

# Issues with Silence Detection:
# - False positives/negatives for silence: The method might misinterpret softer sounds or background noise 
#   as silence, or it might miss short silences between words, especially in noisy environments.
# - Depends on silence threshold: The accuracy of detection depends on setting the correct silence threshold,
#   which may need fine-tuning for different types of audio or speech.
# - May not work well with quiet or abrupt speech: If a speaker talks very softly or with sudden breaks, 
#   the detection algorithm may struggle to detect the proper speech boundaries.

# Hybrid Approach:
# ----------------
# A hybrid approach combines the strengths of both methods. It first uses silence detection to identify the
# speech segments and remove unwanted silence at the start and end of the audio. Then, word duration 
# estimation is applied to the non-silent segments to distribute the words accurately.

from .TTS import Tts
from .assets import TTS_INFO
from .utility import (
    AudioSegment,
    convert_to_wave
)

obj = Tts(TTS_INFO)
text = "if its quack like duck and walk like duck, its must be a duck."
audio_path = obj.create(text, "en")

def count_words(sentence:str):
    count = 0
    for i in sentence:
        if i.isalpha() or i.isdecimal():
            count += 1
        if i in "%$%*+-/":
            count += 1
        
    return count

class Word_Duration_Estimation:
    """
    Estimates word durations based on the total duration of the audio and the length of the text.

    Args:
        script (str): The text corresponding to the spoken words in the audio.
        audio_path (str): The path to the audio file.

    Attributes:
        script (str): The input text/script.
        audio_path (str): The path to the audio file.
        audio (AudioSegment): The loaded audio file.
    """
    def __init__(self, script: str, audio_path: str):
        self.script = script
        self.audio_path = audio_path
        self.audio = AudioSegment.from_file(audio_path)

    def synctext(self) -> list[tuple]:
        """
        Calculates the start and end times for each word based on the audio's duration.

        Returns:
            list[tuple]: A list of tuples where each tuple contains:
            - word (str): The word from the script.
            - start_time (float): The estimated start time (in ms) of the word.
            - end_time (float): The estimated end time (in ms) of the word.
        """
        words = self.script.split() 
        total_duration = len(self.audio)
        total_char = sum(map(len,words))

        word_durations = []
        current_time = 0

        for word in words:
            word_length = len(word)
            word_duration = (word_length / total_char) * total_duration  # Duration in ms
            end_time = current_time + word_duration

            word_durations.append(end_time)
            current_time = end_time
        
        self.words = words

        return word_durations

