import discord
from discord import app_commands
from discord.ext import commands

class help_cog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
    self.help_message = """
    ```
    General\n\n!win: generates a random lottery number based on data collected from all MegaMillion's winning numbers\n!latest draw: returns the last drawn winning numbers\n!help: view all available commands\n!hello: receive a wonderful greeting\n!meow: generate a random cat picture\n!lookup {character name}-{server}: check WoW profile for Gladiator achievement\n\nChatBot\n\n!chatbot: engage the bot\n!helpbot: list all commands for chatbot\n!server: display server statistics\n\nMusic\n\n/play: searches YouTube with input search terms, puts song in queue\n/queue: displays currently playing song and songs in queue\n/pause: pauses current song in queue\n/resume: resume playing current song from queue\n/skip: skips current song\n/clear: clears current queue\n/leave: kicks bot from current voice channel\n/playlist: play a playlist from youtube\n!create_playlist: create a playlist associated with your account\n!list_playlists: list all playlists associated with your account\n!list_songs {playlist name}: list all songs within a playlist\n!add {youtubeURL} to {playlist name}: add a song to a playlist\n!delete_song {youtubeURL from {playlist name}}: delete a song from your playlist\n!delete_playlist {playlist name}: delete an entire playlist\n\nDungeons & Dragons\n\n!roll xdy: roll x number of y value die\n!init -mod/+mod (ie. +3 or -1): roll initiative\n!dm_init <NPC:str> +/-int: roll initiative for non-player character\n!run_init: sorts, prints, and clears out the initiative roll pool\n!condition <search_term:str>: return the rules regarding the input condition\n!condition list: return a list of all valid conditions/search terms
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
