from enum import Enum

COMMAND_IDENTIFIER = "!"

class CommandType(Enum):
    GUESS_ALBUM = f"{COMMAND_IDENTIFIER}guess album" + " "
    GUESS_SONG = f"{COMMAND_IDENTIFIER}guess song" + " "
    SCOREBOARD = f"{COMMAND_IDENTIFIER}scoreboard"
    HELP = f"{COMMAND_IDENTIFIER}help"
    UNKNOWN = "UNKNOWN"
