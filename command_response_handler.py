from typing import Text, Optional
from constants.commandtype import COMMAND_IDENTIFIER, CommandType
from events.logging.event_logger import log, log_with_error


def process_command(message, command: CommandType) -> None:
    author, content = message.author, message.content
    log(f"{author} called command '{command.name}' with message: '{content}'")

    if command == CommandType.GUESS_SONG:
        user_song_guess = content[len(CommandType.GUESS_SONG.value)::]

        if len(user_song_guess) > 0:
            return f"*{message.author}* guessed the song '*{user_song_guess}*'"
        else:
            return f"Invalid guess format. Please use the **{CommandType.HELP.value}** command."

    elif command == CommandType.GUESS_ALBUM:
        user_album_guess = content[len(CommandType.GUESS_ALBUM.value)::]

        if len(user_album_guess) > 0:
            return f"*{message.author}* guessed the album '{user_album_guess}'!"
        else:
            return f"Invalid guess format. Please use the **{CommandType.HELP.value}** command."
    elif command == CommandType.SCOREBOARD:
        return f"*{message.author}* called {command.name}"
    elif command == CommandType.PRACTICE:
        return f"*{message.author}* called {command.name}"
    elif command == CommandType.PLAY:
        return f"*{message.author}* called {command.name}"
    elif command == CommandType.HELP:
        return "\n".join([
            "__**COMMANDS**__",
            f"**{CommandType.HELP.value}**    \t\t\t\t\t\t\t\tGives you the help docs for Swiftie Bot!",
            f"**{CommandType.SCOREBOARD.value}**   \t\t\t\t\tShows the scoreboard for the top 10 users by points in this server.",
            f"**{CommandType.PRACTICE.value}** \t\t\t\t\t\t\tStart practicing! You will NOT earn points for correct answers.",
            f"**{CommandType.PLAY.value}** \t\t\t\t\t\t\t\t\tStart playing! You WILL earn points for correct answers!",
            f"**{CommandType.GUESS_ALBUM.value}[album]**\tGuess an album. This must be preceded by a **{CommandType.PRACTICE.value}** or **{CommandType.PLAY.value}**",
            f"**{CommandType.GUESS_SONG.value}[song]**  \t\tGuess a song. This must be preceded by a **{CommandType.PRACTICE.value}** or **{CommandType.PLAY.value}**",
            ""
        ])


def get_command_type(message_content: Text) -> CommandType:
    for discord_command_enum_value, discord_command_enum_member  in CommandType._value2member_map_.items():
        if message_content.startswith(discord_command_enum_value):
            return discord_command_enum_member

    return CommandType.UNKNOWN

def handle_message(message) -> Optional[Text]:
    message_content = message.content

    if message_content.startswith(COMMAND_IDENTIFIER):
        command: CommandType = get_command_type(message_content)

        if command != CommandType.UNKNOWN:
            return process_command(message, command)
        else:
            log(f"Command '{message_content}' is not a valid command.")
            return "*wtf is that bro*"
    
    return None