import discord
from discord import app_commands
from discord.ext import commands
import math
from youtube_dl import YoutubeDL
from features.sevfunc import intialize_server, add_to_playlist, play_playlist






class music_cog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

    self.is_playing = False
    self.is_paused = False

    self.current_song = None

    self.music_queue = []
    self.YDL_OPTIONS = {'format': 'bestaudio'}
    self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    self.vc = None
    intialize_server()

  def search_yt(self, item):
    with YoutubeDL(self.YDL_OPTIONS) as ydl:
      try:
        info = ydl.extract_info('ytsearch:%s' % item, download=False)['entries'][0]
      except(Exception):
        return False
    song_info = {'source': info['formats'][0]['url'], 'title': info['title'], 'artist': info['uploader'], 'duration': str(math.floor(info['duration']/60))+':'+str(info['duration']%60), 'thumbnail': info['thumbnail']}
    return song_info

  def play_next(self):
    if len(self.music_queue) > 0:
      self.is_playing = True

      m_url = self.music_queue[0][0]['source']

      self.music_queue.pop(0)

      self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e:self.play_next())

    else:
      self.is_playing = False

  async def play_music(self, interaction):
    if len(self.music_queue) > 0:
      self.is_playing = True
      m_url = self.music_queue[0][0]['source']

      if self.music_queue == None or self.vc == None:
        self.vc = await self.music_queue[0][1].connect()

        if self.vc == None:
          await interaction.response.send_message('Could not connect to the voice channel.')
          return
      else:
        await self.vc.move_to(self.music_queue[0][1])

      self.current_song = self.music_queue[0][0]
      self.music_queue.pop(0)

      self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())

    else:
      self.is_playing = False

  @app_commands.command(name='play', description='Play the selected song from Youtube.')
  async def play(self, interaction: discord.Interaction, search: str):

    if interaction.user.voice != None:
      voice_channel = interaction.user.voice.channel
    else:
      voice_channel = None

    if voice_channel is None:
      await interaction.response.send_message('Connect to a voice channel!')
    else:
      song = self.search_yt(search)

      if type(song) == type(True):
        await interaction.response.send_message('Could not download the song. Incorrect format, try a different keyword.')
      else:
        await interaction.response.send_message('Song added to the queue.')
        add_to_playlist(song['source'])
        self.music_queue.append([song, voice_channel])

        if self.is_playing == False:
          await self.play_music(interaction)
          
  @app_commands.command(name='pause', description='Pauses the current song being played.')
  async def pause(self, interaction: discord.Interaction):
    if self.is_playing:
      self.is_playing = False
      self.is_paused = True
      self.vc.pause()
      await interaction.response.send_message('Song paused.')
    elif self.is_paused:
      self.is_playing = True
      self.is_paused = False
      self.vc.resume()
      await interaction.response.send_message('Song resumed.')

  @app_commands.command(name='resume', description='Resumes playing the current song.')
  async def resume(self, interaction: discord.Interaction):
    if self.is_paused:  
      self.is_playing = True
      self.is_paused = False
      self.vc.resume()
      await interaction.response.send_message('Song resumed.')
    
  @app_commands.command(name='skip', description='Skips the currently played song.')
  async def skip(self, interaction: discord.Interaction):
    if self.vc != None and self.vc:
      self.vc.stop()
      await self.play_music(interaction)
      await interaction.response.send_message('Song skipped.')

  @app_commands.command(name='queue', description='Displays all the songs currently in the queue.')
  async def queue(self, interaction: discord.Interaction):
    if self.music_queue == [] and self.current_song == None:
      await interaction.response.send_message('There is no music in the queue.')
    else:
      queue_string = ''
      i = 1
      duration = self.current_song['duration']
      title = self.current_song['title']
      artist = self.current_song['artist']
      queue_string += f'**CURRENTLY PLAYING:**\n [{duration}] {title} <by: {artist}>\n\n**QUEUE:**\n'
      for song in self.music_queue:
        duration = song[0]['duration']
        title = song[0]['title']
        artist = song[0]['artist']
        print(song[0]['duration'], song[0]['title'], song[0]['artist'])
        queue_string += f'{i}) [{duration}] {title} <by: {artist}>\n'
        i += 1

      embed = discord.Embed(description=queue_string, color=discord.Color.random())
      thumbnail = self.current_song['thumbnail']
      embed.set_thumbnail(url=thumbnail)
      await interaction.response.send_message(embed=embed)

  @app_commands.command(name='clear', description='Stops the current song and clears the queue.')
  async def clear(self, interaction: discord.Interaction):
    if self.vc != None and self.is_playing:
      self.vc.stop()
    self.music_queue = []
    await interaction.response.send_message('Music queue cleared.')

  @app_commands.command(name='leave', description='Kick the bot from the voice channel.')
  async def leave(self, interaction: discord.Interaction):
    self.is_playing = False
    self.is_paused = False
    await self.vc.disconnect()
    await interaction.response.send_message('GOODBYE CRUEL WORLD.')
  
  @app_commands.command(name='playlist', description='List your playlist name and play the contents on shuffle.', )
  async def playlist(self, interaction: discord.Interaction, playlist:str):
    url_list=play_playlist(playlist, interaction.user)
    print(url_list)
    if interaction.user.voice != None:
        voice_channel = interaction.user.voice.channel
    else:
        voice_channel = None
    for url in url_list:
      try:
        if voice_channel is None:
          pass
        else:
            song = self.search_yt(url)
            add_to_playlist(song['source'])
            self.music_queue.append([song, voice_channel])
      except:
        pass

    if self.is_playing == False:
            await self.play_music(interaction)
    else:
        await interaction.response.send_message("playing...")
    # await interaction.response.send_message("playing...")
    


async def setup(bot: commands.Bot):
    await bot.add_cog(
      music_cog(bot),
      guilds=[discord.Object(id=1057755148862099536), discord.Object(id=1057692804865855652)])