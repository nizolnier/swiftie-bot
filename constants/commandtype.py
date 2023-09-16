from enum import Enum

COMMAND_IDENTIFIER = "!"

class CommandType(Enum):
    GUESS_ALBUM = f"{COMMAND_IDENTIFIER}guess album" + " "
    GUESS_SONG = f"{COMMAND_IDENTIFIER}guess song" + " "


    PRACTICE = f"{COMMAND_IDENTIFIER}practice"
    PLAY = f"{COMMAND_IDENTIFIER}play"
    SCOREBOARD = f"{COMMAND_IDENTIFIER}scoreboard"
    HELP = f"{COMMAND_IDENTIFIER}help"


    UNKNOWN = "UNKNOWN"
