from videogenrator.GenrateVideo import GenerateVideo, generate_subtitles
from videogenrator.TTS import Tts
from videogenrator.SyncText import Word_Duration_Estimation
from videogenrator.utility import convert_to_wave

import os


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_FILE = os.path.join(APP_DIR, "assets", "settings.json")
FONTS_PATH = os.path.join(APP_DIR,"assets", "fonts")
FALLOUT_DOWNLOAD_PATH = os.path.expanduser("~/Downloads")
FALLOUT_TEMP_PATH = os.path.join(APP_DIR, "trash")

Tts_info = {
    "use_services": "gtts",
    "slow": False,
}
video_info = {
    "default": os.path.join(APP_DIR, "assets","fonts","Agiven-Drawn.otf"),
    "size":24
}
text = "hello this is a demo text countdown and effects will add sooner"
audio_path = Tts(Tts_info)
audio_path = audio_path.create(text,"en")
timestamps = Word_Duration_Estimation(text, audio_path)
timestamps = timestamps.synctext()

subtiles = generate_subtitles(text, timestamps)
print(subtiles)
print("\n\n")
# video generation
video = GenerateVideo(video_info)

video.create_final_video(
    video_path= os.path.join(APP_DIR,"assets","video2.mp4"),
    subtitles=subtiles,
    audio_path=audio_path,
    background_audio_path= os.path.join(APP_DIR,"assets","music1.wav"),
    output_path=os.path.join(FALLOUT_DOWNLOAD_PATH,"output.mp4")
)