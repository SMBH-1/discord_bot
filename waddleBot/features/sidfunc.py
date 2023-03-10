import discord
from discord.ext import commands
import requests 
import os
import pytz
import datetime
from dotenv import load_dotenv
import json
import openai
import giphy_client
from giphy_client.rest import ApiException
import random

load_dotenv()

  # if message.content.startswith('$arson_bot, make me '):

  #   #The following will allow arson_bot to call OpenAI API to generate DALL-E image
intents = discord.Intents.all()
# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!', intents=intents) 


def generate_dall_e_img(prompt):
  openai.api_key = os.environ['OPEN_AI_DALLE']
  openai.Model.list() #Validates whether authentication has been completed
  response = openai.Image.create(
    prompt = prompt[21:],
    n = 1,
    size = '512x512',
  )
  image_url = response['data'][0]['url']
  return image_url



def gif_finder(q):
  q=q[5:]
  giphy_api_key = os.environ['GIPHY_KEY']
  api_use = giphy_client.DefaultApi()

  try:
    api_response = api_use.gifs_search_get(giphy_api_key, q, limit=5, rating='g')
    response_list = list(api_response.data)
    gif = random.choice(response_list)
    # print(gif)
    # gif_embed = discord.Embed(title=q)
    # embed = gif_embed.set_image(url=f"https://media.giphy.com/media/{gif.id}/giphy.gif")
    return gif.embed_url
    
  except ApiException as r:
    print("Exception from API")


