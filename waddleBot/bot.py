import discord
import os
from dotenv import load_dotenv
import responses
load_dotenv()
async def send_message(message, user_message, is_private):
    # Handle response and send in PM or channel
    try:
        response = responses.handle_response(user_message)
        if response:
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