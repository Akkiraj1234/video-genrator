class VideoGenError(Exception):
    """
    Base class for all custom exceptions in the Video Generator application.
    """
    def __init__(self, message: str = "An error occurred in the Video Generator application"):
        super().__init__(message)


class InternetError(VideoGenError):
    """
    Raised when there is an internet-related error.
    """
    def __init__(self, message: str = "Internet connectivity issue detected"):
        detailed_message = f"INTERNET ERROR: {message}"
        super().__init__(detailed_message)


class AssetsNotAvailableError(VideoGenError):
    """Raised when required assets are not available."""
    def __init__(self, message="Assets not available. Please check the assets directory."):
        super().__init__(message)


class InvalidFontError(VideoGenError):
    """Raised when a specified font is not found."""
    def __init__(self, message="The requested font is invalid or not found."):
        super().__init__(message)
        
class FileLoadError(VideoGenError):
    """Raised when a file provided by the user cannot be loaded."""
    def __init__(self, message="The provided file could not be loaded. Please check the file path and format."):
        super().__init__(message)

