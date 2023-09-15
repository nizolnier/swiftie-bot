import discord, json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

token = config['token']

async def send_message(message, user_message, is_private):
    try:
        response = 'slay'

        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said "{user_message}" in channel {channel}')

    client.run(token)