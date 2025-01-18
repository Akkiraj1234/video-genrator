class Video_Gen_ERROR(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    
    
class Internet_ERROR(Exception):
    def __init__(self, message:str):
        message = f"INTERNET ERROR: {message}"
        super().__init__(message)
        