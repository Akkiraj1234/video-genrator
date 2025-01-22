from .logger import setup_logging
from .assets import assets
from .error import VideoGenError
from .utility import is_path, logging, os
from .parser import VideoConfigParser
from .video_generator import Generate
import argparse


def open_script(object: str) -> str:
    """
    Opens the script if it's a valid path or returns the text directly.
    Resolves paths to absolute paths.
    """
    logging.debug(f"Processing input: {object}")
    
    if is_path(object):
        absolute_path = os.path.abspath(object)
        logging.info(f"File found: {absolute_path}. Attempting to open.")
        try:
            with open(absolute_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error reading file {absolute_path}: {e}")
            raise
    
    elif object is None:
        logging.warning("No input provided; `object` is None. Input cannot be None.")
        raise ValueError("Input cannot be None.")
    
    logging.info("Input is treated as raw script text.")
    return object

def initialize_argparse():
    """
    Initializes and returns an ArgumentParser for the video generation tool.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Video Generator Tool: A command-line utility to create video clips from a script. "
            "Provide either a path to a script file or the script text directly as input."
        ),
        epilog=(
            "Example usage:\n"
            "  python video_generator.py 'path/to/script.txt'  # Process a script file\n"
            "  python video_generator.py 'Raw script text here'  # Process inline script text\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter 
    )
    
    parser.add_argument(
        "script", type=str,
        help=(
            "The script to be used for generating the video. "
            "Provide either:\n"
            "  - A valid file path to a script file, or\n"
            "  - The raw script text enclosed in quotes."
        ),
    )
    return parser

def main() -> int:
    # setting up logging and assets
    setup_logging()
    logging.info("Application Started")
    assets.load_Assets()
    
    #setting up parser and stuff
    parser = initialize_argparse()
    args = parser.parse_args()
    text = open_script(args.script)
    
    # creating parser object
    parser = VideoConfigParser(text)
    video = Generate(parser)
    video.execute()
    
    if video.status_code:
        logging.debug(f"Video successfully created. Output saved to: {video.path}")
    else:
        logging.error(f"Video generation failed. Error: {video.error}")
        raise VideoGenError(video.error)
    
    return 0


if __name__ == "__main__":
    main()