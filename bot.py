import discord, json, command_response_handler
from events.logging import log, log_with_error
from typing import Optional, Text

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

token = config['TOKEN']

async def send_message(message):
    try:
        response: Optional[Text] = command_response_handler.handle_message(message)

        if response:
            await message.channel.send(response)
    except Exception as error:
        log_with_error(f"Something went wrong with sending a message", error)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        log(f"{client.user} is now running")
    
    @client.event
    async def on_message(message):
        if message.author != client.user:
            await send_message(message)

    client.run(token)