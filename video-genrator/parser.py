import os
import configparser
from typing import TextIO
import logging

logger = logging.getLogger(__name__)

class VideoConfigParser:
    def __init__(self, file_obj: TextIO):
        """
        Initialize the VideoConfigParser with a configuration file as a TextIO object.
        """
        self.config = configparser.ConfigParser()
        self.config.read_file(file_obj)
        self.assets = {}
        self.clips = {}
        self.metadata = {}
        self.parse_config()

    def parse_config(self):
        """
        Parse and validate the configuration file, organizing clip information
        and other metadata into dictionaries.
        """
        self._validate_and_parse_assets()
        self._parse_clips()
        self._parse_metadata()

    def _validate_and_parse_assets(self):
        """
        Validate the existence of assets and store their paths.
        """
        if "assets" not in self.config:
            raise ValueError("The configuration is missing the [assets] section.")
        
        self.assets = {key: value.strip('"') for key, value in self.config.items("assets")}
        missing_assets = [name for name, path in self.assets.items() if not os.path.exists(path)]

        if missing_assets:
            raise ValueError(f"The following assets are missing: {', '.join(missing_assets)}")

    def _parse_clips(self):
        """
        Parse clip-related settings into a structured dictionary.
        """
        if "video-settings" not in self.config:
            raise ValueError("The configuration is missing the [video-settings] section.")

        self.clips = {}
        for key, value in self.config.items("video-settings"):
            clip_id, attr = key.split(".", 1)
            if clip_id not in self.clips:
                self.clips[clip_id] = {}
            self.clips[clip_id][attr] = self._resolve_value(value)

        # Map clip video assets
        for clip_id, clip_data in self.clips.items():
            if "video" in clip_data:
                asset_key = clip_data["video"]
                if asset_key not in self.assets:
                    raise ValueError(f"Asset '{asset_key}' in {clip_id} is not defined in the [assets] section.")
                clip_data["video_path"] = self.assets[asset_key]

    def _parse_metadata(self):
        """
        Parse non-clip-related metadata (e.g., script settings and video creation settings).
        """
        self.metadata = {}
        for section in self.config.sections():
            if section not in ["assets", "video-settings"]:
                self.metadata[section] = {key: self._resolve_value(value) for key, value in self.config.items(section)}

    def _resolve_value(self, value):
        """
        Convert string values to appropriate types (e.g., list, int, or bool).
        """
        value = value.strip()
        # Handle list-like values
        if value.startswith("[") and value.endswith("]"):
            return [item.strip() for item in value[1:-1].split(",")]
        # Handle integers
        try:
            return int(value)
        except ValueError:
            pass
        # Handle booleans
        if value.lower() in ("true", "false"):
            return value.lower() == "true"
        # Default to string
        return value

    def get_clip(self, clip_id: str):
        """
        Retrieve information for a specific clip.
        """
        return self.clips.get(clip_id, None)

    def get_metadata(self, section: str):
        """
        Retrieve metadata for a specific section.
        """
        return self.metadata.get(section, None)


# Example Usage
if __name__ == "__main__":
    from io import StringIO

    # Example configuration as a string
    config_data = """
    [assets]
    video1 = "assets/video1.mp4"
    video2 = "assets/video2.mp4"

    [video-settings]
    clip1.video = video1
    clip1.effects-begin = "fadeup"
    clip1.effects-end =  "fadeout"
    clip1.duration = 3
    clip2.video = video2
    clip2.effects = "snowfall"
    clip2.duration = 5

    [script-settings]
    script-time-exceed-video-increase = True
    script-printing-style = "normal"
    script-style = "fading"

    clip1.script = "Welcome to the best video editing tool!"
    clip2.script = "Here are your steps to success:\\n1. Plan.\\n2. Create.\\n3. Edit.\\n4. Share."

    [video-creation]
    video-size-aspect-ratio = "16:9"
    sequence = [clip1, countdown.3, clip2]
    """

    # Simulate reading from a file
    config_file = StringIO(config_data)

    # Parse the configuration
    parser = VideoConfigParser(config_file)

    # Access parsed data
    print("Assets:", parser.assets)
    print("Clips:", parser.clips)
    print("Metadata:", parser.metadata)

    # Get specific clip information
    print("Clip1 Info:", parser.get_clip("clip1"))
    print("Video Creation Metadata:", parser.get_metadata("video-creation"))
