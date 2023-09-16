import discord
from typing import Text, Optional
from constants.commandtype import COMMAND_IDENTIFIER, CommandType
from events.logging.event_logger import log, log_with_error


def handle_valid_command_response(message, command: CommandType) -> None:
    log(f"{message.author} called command '{command.name}' with message: '{message.content}'")

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
            handle_valid_command_response(message, command)
            return f"{message.author} called {command.name}"
        else:
            log(f"Command '{message_content}' is not a valid command.")
            return "wtf is that bro"
    
    return None