import discord
from discord.ext import commands, tasks
from discord.ext import tasks
import os
from dotenv import load_dotenv
import responses
import requests
import re
import json

# from cogs import music_cog as music_cog

load_dotenv()


def run_discord_bot():
    # Bot token import from .env, fix weird intents issue
    my_secret = os.environ['TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    # Announce bot login
    @bot.event
    async def on_ready():
        check_for_videos.start()
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                # print(filename)
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.tree.sync(guild=discord.Object(id=1057692804865855652))
        print(f'{bot.user} is now running!')
    
    @bot.event
    async def send_message(message, user_message, is_private):
    # Handle response and send in PM or channel
      try:
          response = responses.handle_response(user_message, message.author)
          if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
      except Exception as e: 
          print(e)


    # Message classification
    @bot.event
    async def on_message(message):
        # Avoid infinite loops
        if message.author == bot.user:
            return 

        # Grab author, content, channel
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' ({channel})")

        # Determine if response will be in private message or channel it was received in
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        if message.content.startswith('!commands'):
            help_commands='The commands I can perform are:\n!schedule\n!lookup\n!server\n!helpbot\n!chatbot\n!win\n!latest draw\n\nThe music bot commands are:\n/play <keywords>: finds the song on youtube and plays it in your current channel, will resume playing the current song if it was paused\n/queue: displays the current music queue\n/skip: skips the current song being played\n/clear: stops the music and clears the queue\n/leave: disconnects the bot from the voice channel\n/pause: pauses the current song, or resumes play if the song was paused\n/resume: resumes playing the current song'
            await message.author.send(commands)
    


    newUserDM = 'Hi, Welcome to the server! Type !commands in the server to receive a list of commands that I can perform!'
    @bot.event
    async def on_member_join(member):
        gen_channel = bot.get_channel(1057692805704712315)
        print(member)
        print('Bot notices ' + member.name + ' joined')
        await member.send(newUserDM)
        await gen_channel.send(f'{member.name} has joined! Everyone say hello!')
    
    # For youtube notifications
    @tasks.loop(minutes=5)
    async def check_for_videos():
        with open("youtube_data.json", "r") as f:
            data = json.load(f)
        
        print("Checking for YT uploads now ...")
        
        #checking for all the channels
        for youtube_channel in data:
            channel = f"https://youtube.com/channel/{youtube_channel}"
            html = requests.get(channel+"/videos").text

            #getting the latest video's url
            try:
                latest_video_url = f"https://youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
            except:
                continue
            
            # Checking if url in json file is the same as latest video url
            if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
                data[str(youtube_channel)]["latest_video_url"] = latest_video_url

                with open("youtube_data.json", "w") as f:
                    json.dump(data, f)
                
                # Getting the channel to send the message in
                discord_channel_id = data[str(youtube_channel)]["notifying_discord_channel"]
                discord_channel = bot.get_channel(int(discord_channel_id))

                # Sending the message
                # Mention whatever role  
                msg = f"@everyone {data[str(youtube_channel)]['channel_name']} just uploaded a video to YouTube. Check it out: {latest_video_url}"

                await discord_channel.send(msg)
        # Command to add more youtube accounts to watch in the json file

    @bot.command()
    async def youtube_notification_data(ctx, channel_id: str, *, channel_name: str):
        with open("youtube_data.json", "r") as f:
            data = json.load(f)
        
        data[str(channel_id)] = {}
        data[str(channel_id)]["channel_name"] = channel_name
        data[str(channel_id)]["latest_video_url"] = "none"

        data[str(channel_id)]["notifying_discord_channel"] = "none"

        with open("youtube_data.json", "w") as f:
            data = json.dump(data, f)
        
        await ctx.send("Added account data!")

    @bot.command()
    async def start_notifying(ctx):
        check_for_videos.start()
        await ctx.send("Now Notifying")
    
    
    bot.run(my_secret)
