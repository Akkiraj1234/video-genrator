import logging
import os


def setup_logging():
    dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # terminal level logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # file level logger
    log_file_path = os.path.join(dir_name, "app.log")
    file_handler = logging.FileHandler(log_file_path, mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s [ %(lineno)s ] : %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    # the root logger
    logging.basicConfig(
        level=logging.DEBUG, 
        handlers=[console_handler, file_handler]
    )

    info_message = f"Logging setup complete. Logs will be saved to {log_file_path}"
    logging.info(info_message)
    
    console_handler.handle(
        logging.LogRecord(
            name="root", 
            level=logging.INFO, 
            pathname=__file__, 
            lineno=59,  
            msg=info_message, 
            args=None, 
            exc_info=None
        )
    )