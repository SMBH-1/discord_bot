import discord
from discord import app_commands
from discord.ext import commands

class help_cog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
    self.help_message = """
    ```
    /help: displays all the available commands
    /play <keywords>: finds the song on youtube and plays it in your current channel, will resume playing the current song if it was paused
    /queue: displays the current music queue
    /skip: skips the current song being played
    /clear: stops the music and clears the queue
    /leave: disconnects the bot from the voice channel
    /pause: pauses the current song, or resumes play if the song was paused
    /resume: resumes playing the current song
    ```
    """

    # self.text_channel_list = []

  # @commands.Cog.listener()
  # async def on_ready(self):
  #   print('Help cog loaded.')
  #   for guild in self.bot.guilds:
  #     for channel in guild.text_channels:
  #       self.text_channel_list.append(channel)

  #   await self.send_to_all(self.help_message)

  # async def send_to_all(self, msg):
  #   for text_channel in self.text_channel_list:
  #     await text_channel.send(msg)

  @app_commands.command(name='help', description='Displays all the available commands.')
  async def help(self, interaction):
    await interaction.response.send_message(self.help_message)

async def setup(bot: commands.Bot):
    await bot.add_cog(
      help_cog(bot),
      guilds=[discord.Object(id=1057755148862099536), discord.Object(id=1057692804865855652)])