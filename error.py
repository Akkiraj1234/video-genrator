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
