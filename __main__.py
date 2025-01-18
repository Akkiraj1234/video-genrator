from .error import Video_Gen_ERROR
from .utility import is_path
from .video_generator import Generate

import argparse
import os

parser = argparse.ArgumentParser(description="A simple python code to create video clips")
parser.add_argument("script", type=str, help="script or file path to the script")
parser.add_argument("--video", type=str, help="path to the video")
parser.add_argument("--audio", type=str, help="path to the audio file")

def open_script(object: str) -> str:
    """
    Opens the script if it's a valid path or returns the text directly.
    Resolves paths to absolute paths.
    """
    if is_path(object):  # Check if the input looks like a path
        absolute_path = os.path.abspath(object)  # Resolve to absolute path
        if os.path.exists(absolute_path):  # Check if the path exists
            with open(absolute_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            raise Video_Gen_ERROR(f"PATH '{absolute_path}' is not valid")
    elif object is None:
        return "some text"
    
    return object

if __name__ == "__main__":
    args = parser.parse_args()
    
    text = open_script(args.script)
    video = None
    audio = None
    
    if args.video:
        video = "some video yay"
        
    if args.audio:
        audio = "some audio yay"
        
    with Generate(text, video, audio) as obj:
        obj.execute()
        
        if obj.status_code:
            print("video saved in path: ",obj.path)
        else:
            print("video generation failed error: ", obj.error)