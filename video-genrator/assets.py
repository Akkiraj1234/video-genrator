from .utility import json, os

# Default settings
DEFAULT_SETTINGS = {
    "TTS_info": {
        "use_services": "gtts",
        "slow": False
    },
    "Download_path": os.path.expanduser("~/Downloads"),
    "Temp_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
}
SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as file:
            json.dump(DEFAULT_SETTINGS, file)
        return DEFAULT_SETTINGS
    
    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)

        # Validate and populate missing keys with defaults
        for key, default_value in DEFAULT_SETTINGS.items():
            if key not in settings:
                settings[key] = default_value

        # # updated settings if any defaults were added
        # with open(SETTINGS_FILE, "w") as file:
        #     json.dump(settings, file, indent=4)

        return settings
    
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading settings file: {e}")
        return DEFAULT_SETTINGS


def clear_current_session():
    current_pid = os.getpid()
    temp_files = os.listdir(Temporary_File_Path)
    for file in temp_files:
        file_path = os.path.join(Temporary_File_Path, file)
        if os.path.isfile(file_path) and file.startswith(f"tts_output_{current_pid}"):
            os.remove(file_path)
    print("Temporary files for current session cleared.")


# Load the settings and stuff
settings = load_settings()
TTS_INFO = settings["TTS_info"]
Temporary_File_Path = settings["Temp_path"]
Download_Path = settings["Download_path"]


# checking the assets existence
if not os.path.exists(Temporary_File_Path):
    Temporary_File_Path = DEFAULT_SETTINGS["Temp_path"]
    
    if not os.path.exists(DEFAULT_SETTINGS["Temp_path"]):
        os.makedirs(Temporary_File_Path)


__all__ = ["Temporary_File_Path", "clear_current_session", "TTS_INFO", "Download_Path"]
