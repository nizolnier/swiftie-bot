from datetime import datetime
from typing import Text


# PRIVATE METHODS
def format(message: Text) -> Text:
    current_date_time = __get_current_date_time()

    return "\n".join([
        "=====",
        f"[EVENT LOG @ {current_date_time}]\n",
        f"Message: {message}",
        "====="
    ])

def format_with_error(message: Text, error: Exception) -> Text:
    current_date_time = __get_current_date_time()

    return "\n".join([
        "=====",
        f"[EVENT LOG @ {current_date_time}]\n",
        f"Message: {message}",
        f"Error: {error}",
        "====="
    ])

def __get_current_date_time() -> Text:
    current_date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return current_date_time

# PUBLIC METHODS
def log(message: Text) -> None:
    log_message = format(message)
    print(log_message)

def log_with_error(message: Text, error: Exception) -> None:
    log_message_with_error = format_with_error(message, error)
    print(log_message_with_error)