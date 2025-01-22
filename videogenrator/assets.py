from .error import AssetsNotAvailableError, InvalidFontError
from .utility import logging, json, os

# setting up logging and path
logger = logging.getLogger(__name__)

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_FILE = os.path.join(APP_DIR, "assets", "settings.json")
FONTS_PATH = os.path.join(APP_DIR,"assets", "fonts")
FALLOUT_DOWNLOAD_PATH = os.path.expanduser("~/Downloads")
FALLOUT_TEMP_PATH = os.path.join(APP_DIR, "trash")


class Assets:
    
    def __init__(self):
        self.APP_DIR = APP_DIR
        self.SETTINGS_FILE = SETTINGS_FILE
        self.FONTS_PATH = FONTS_PATH
        self.FALLOUT_DOWNLOAD_PATH = FALLOUT_DOWNLOAD_PATH
        self.FALLOUT_TEMP_PATH = FALLOUT_TEMP_PATH
    
    @property
    def default_setting(self) -> None:
        return {
            "TTS_info": {
                "use_services": "gtts",
                "slow": False,
            },
            "Fonts_info": {
                "default": "Rain Night",
                "size":24
            },
            "Download_path": FALLOUT_DOWNLOAD_PATH,
            "Temp_path": FALLOUT_TEMP_PATH,
        }
        
    def __write_data_json(self, path:str, data:dict):
        pass
    
    def _load_setting_data(self) -> dict:
        """
        Load or initialize the settings file.
        """
        if not os.path.exists(SETTINGS_FILE):
            logger.info("Settings file not found. Creating a new one with default settings.")
            self.__write_data_json(SETTINGS_FILE, self.default_setting)
            
        try:
            with open(SETTINGS_FILE, "r") as file:
                settings = json.load(file)
            
            for key, default_value in self.default_setting.items():
                settings.setdefault(key, default_value)
            
            self.__write_data_json(SETTINGS_FILE, settings)
            return settings
        
        except json.JSONDecodeError as e:
            logger
            return self.default_setting
        
        except (IOError, PermissionError) as e:
            logger.error(f"Error reading settings file: {e}")
            return self.default_setting
    
    def _check_assets(self):
        media_assets = [
            "image1.jpg",
            "image2.jpg",
            "image3.jpg",
            "image4.jpg",
            "image5.jpg",
            "video1.mp4",
            "video2.mp4",
            "music1.mp3",           
        ]
        fonts_assets = [
            "Agiven-Drawn.otf",
            "BeachyLagoon.ttf",
            "Blonden-ExtrudeRight.otf",
            "BrandenRounded-Regular.otf",
            "Grownup.ttf",
            "Rain Night.ttf"
        ]
        
    
    def _check_and_clear_trash(self):
        pass
    
    def load_settings(self) -> dict:
        self._load_setting_data()
        self._check_assets()
        self._check_and_clear_trash()
        
        
    def load_Assets(self) -> None:
        pass
    
    def clear_current_session(self) -> None:
        pass
    
    def get_font_by_name(self, name:str) -> str:
        pass
    
    def create_temp(self, name:str) -> str:
        pass
    

assets = Assets()
    









# Load available fonts
try:
    Fonts_List = os.listdir(FONTS_PATH)
    if not Fonts_List:
        raise AssetsNotAvailableError("No fonts found in the fonts directory.")
except FileNotFoundError:
    raise AssetsNotAvailableError(f"Fonts directory not found: {FONTS_PATH}")

#
# Functions






def clear_current_session() -> None:
    """Clear temporary files for the current session."""
    current_pid = os.getpid()
    try:
        temp_files = os.listdir(Temporary_File_Path)
        for file in temp_files:
            file_path = os.path.join(Temporary_File_Path, file)
            if os.path.isfile(file_path) and file.startswith(f"tts_output_{current_pid}"):
                os.remove(file_path)
        logging.info("Temporary files for the current session cleared.")
    except FileNotFoundError:
        logging.warning(f"Temporary directory not found: {Temporary_File_Path}")


def font_byname(name: str) -> str:
    """Return the path of a font by its name. Defaults to the first font if no match is found."""
    for font in Fonts_List:
        font_name, _ = os.path.splitext(font)
        if font_name == name:
            return os.path.join(FONTS_PATH, font)
    logging.warning(f"No match found for font '{name}'. Returning default font.")
    if Fonts_List:
        return os.path.join(FONTS_PATH, Fonts_List[0])
    raise InvalidFontError("No fonts available to return.")


# Load the settings and validate paths
settings = {
            "TTS_info": {
                "use_services": "gtts",
                "slow": False,
            },
            "Fonts_info": {
                "default": "Rain Night",
                "size":24
            },
            "Download_path": FALLOUT_DOWNLOAD_PATH,
            "Temp_path": FALLOUT_TEMP_PATH,
        }
TTS_INFO = settings["TTS_info"]
FONTS_INFO = settings["Fonts_info"]
Temporary_File_Path = settings["Temp_path"]
Download_Path = settings["Download_path"]

# Ensure temporary file path exists
if not os.path.exists(Temporary_File_Path):
    try:
        os.makedirs(Temporary_File_Path)
        logging.info(f"Temporary directory created: {Temporary_File_Path}")
    except OSError as e:
        logging.error(f"Failed to create temporary directory: {e}")
        Temporary_File_Path = settings["Temp_path"]

# Exported variables and functions
__all__ = ["Temporary_File_Path", "clear_current_session", "TTS_INFO", "Download_Path", "font_byname"]
