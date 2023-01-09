import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import responses

print(os.getcwd())
load_dotenv()
token = os.environ.get('token')

class MyBot(commands.Bot):
  def __init__(self):
    intents=discord.Intents.default()
    intents.message_content = True
    super().__init__(
      command_prefix='!',   
      intents=intents,
      application_id=1060249173166936124
    )

  async def setup_hook(self):
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        print(filename)
        await self.load_extension(f'cogs.{filename[:-3]}')
    await bot.tree.sync(guild=discord.Object(id=1057755148862099536))
    # await bot.tree.sync(guild=discord.Object(id=1057692804865855652))

  async def on_ready(self):
    print(f'We Have logged in as {self.user}')

bot = MyBot()

async def send_message(message, user_message, is_private):
# Handle response and send in PM or channel
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e: 
        print(e)

  # Message classification
@bot.event
async def on_message(message):
    print(message.content)
    # Avoid infinite loops
    if message.author == bot.user:
        return 
    
    # Grab author, content, channel
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    #"logging" chat in console
    print(f"{username} said: '{user_message}' ({channel})")

    # Determine if response will be in private message or channel it was received in
    if user_message[0] == '!':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

bot.run(token)

# def run_discord_bot():
#     # Bot token import from .env, fix weird intents issue
#     my_secret = os.environ['TOKEN']
#     intents = discord.Intents.default()
#     intents.message_content = True
#     client = discord.Client(intents=intents)

#     # Announce bot login
#     @client.event
#     async def on_ready():
#         print(f'{client.user} is now running!')
    
    

<<<<<<< HEAD
=======
        #"logging" chat in console
        print(f"{username} said: '{user_message}' ({channel})")

        # Determine if response will be in private message or channel it was received in
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
    
    commands = 'The commands I can perform are:\n!schedule\n!lookup\n!helpbot\n!chatbot\n!win\n!latest draw'
    
    # dm commands on request
    @client.event
    async def on_message(message):
        if message.content.startswith('!commands'):
            await message.author.send(commands)
    
    # set message to new users
    newUserDM = 'Hi, Welcome to the server! Type !commands in the server to receive a list of commands that I can perform!'

    # welcome a new member
    @client.event
    async def on_member_join(member):
        gen_channel = client.get_channel(1057692805704712315)
        print(member)
        print('Bot notices ' + member.name + ' joined')
        await member.send(newUserDM)
        await gen_channel.send(f'{member.name} has joined! Everyone say hello!')
>>>>>>> 0ec535af554e4234438853d1b8009bf6d88a0304
    
#     client.run(my_secret)
