from enum import Enum

COMMAND_IDENTIFIER = "!"

class CommandType(Enum):
    GUESS_ALBUM = f"{COMMAND_IDENTIFIER}guess album" + " "
    GUESS_SONG = f"{COMMAND_IDENTIFIER}guess song" + " "


    PRACTICE = f"{COMMAND_IDENTIFIER}practice"
    PRACTICE_EASY = f"{COMMAND_IDENTIFIER}practice easy"
    PRACTICE_MEDIUM = f"{COMMAND_IDENTIFIER}practice medium"
    PRACTICE_HARD = f"{COMMAND_IDENTIFIER}practice hard"


    PLAY = f"{COMMAND_IDENTIFIER}play"
    PLAY_EASY = f"{COMMAND_IDENTIFIER}play easy"
    PLAY_MEDIUM = f"{COMMAND_IDENTIFIER}play medium"
    PLAY_HARD = f"{COMMAND_IDENTIFIER}play hard"


    SCOREBOARD = f"{COMMAND_IDENTIFIER}scoreboard"
    HELP = f"{COMMAND_IDENTIFIER}help"


    UNKNOWN = "UNKNOWN"
