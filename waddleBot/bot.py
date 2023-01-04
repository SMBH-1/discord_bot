import discord
import os
from dotenv import load_dotenv
import responses


load_dotenv()

async def send_message(message, user_message, is_private):
    # Handle response and send in PM or channel
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e: 
        print(e)

def run_discord_bot():
    # Bot token import from .env, fix weird intents issue
    my_secret = os.environ['TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Announce bot login
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    
    # Message classification
    @client.event
    async def on_message(message):
        # Avoid infinite loops
        if message.author == client.user:
            return 
        
        # Grab author, content, channel
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #"logging" chat in console
        print(f"{username} said: '{user_message}' ({channel})")

        # Determine if response will be in private message or channel it was received in
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
    
    client.run(my_secret)
