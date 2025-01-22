from .error import AssetsNotAvailableError, InvalidFontError
from .utility import json, os, logging

def setup_logging():
    # terminal level logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # file level logger
    file_handler = logging.FileHandler(os.path.join(dir_name,"app.log"))
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s [ %(lineno)s ] : %(message)s")
    file_handler.setFormatter(file_formatter)

    # the root logger
    logging.basicConfig(
        level=logging.DEBUG, 
        handlers=[console_handler, file_handler]
    )


# Directory paths
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Default settings
DEFAULT_SETTINGS = {
    "TTS_info": {
        "use_services": "gtts",
        "slow": False,
    },
    "Fonts_info": {
        "default": "Rain Night",
        "size":24
    },
    "Download_path": os.path.expanduser("~/Downloads"),
    "Temp_path": os.path.join(dir_name, "trash"),
}

# File paths
SETTINGS_FILE = os.path.join(dir_name, "assets", "settings.json")
FONTS_PATH = os.path.join(dir_name, "fonts")

# Load available fonts
try:
    Fonts_List = os.listdir(FONTS_PATH)
    if not Fonts_List:
        raise AssetsNotAvailableError("No fonts found in the fonts directory.")
except FileNotFoundError:
    raise AssetsNotAvailableError(f"Fonts directory not found: {FONTS_PATH}")

# Functions


def load_settings() -> dict:
    """Load or initialize the settings file."""
    if not os.path.exists(SETTINGS_FILE):
        logging.info("Settings file not found. Creating a new one with default settings.")
        with open(SETTINGS_FILE, "w") as file:
            json.dump(DEFAULT_SETTINGS, file, indent=4)
        return DEFAULT_SETTINGS

    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)

        # Validate and populate missing keys with defaults
        for key, default_value in DEFAULT_SETTINGS.items():
            settings.setdefault(key, default_value)

        # Update settings file if defaults were added
        with open(SETTINGS_FILE, "w") as file:
            json.dump(settings, file, indent=4)

        return settings

    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in settings file: {e}")
        return DEFAULT_SETTINGS
    except IOError as e:
        logging.error(f"Error reading settings file: {e}")
        return DEFAULT_SETTINGS


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
settings = load_settings()
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
        Temporary_File_Path = DEFAULT_SETTINGS["Temp_path"]

# Exported variables and functions
__all__ = ["Temporary_File_Path", "clear_current_session", "TTS_INFO", "Download_Path", "font_byname"]
