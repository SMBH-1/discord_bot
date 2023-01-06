import openai       # pip install openai
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('spence_bot_token')

openai.api_key = os.getenv('openai_api_key')

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents) 

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Bot Command',
        description = 'Welcome to the help section. Here are all the commands for the chatbot.',
        color = discord.Color.green()
    )

    embed.set_thumbnail(url='https://www.longboarderlabs.com/wp-content/uploads/2019/11/DGK-X-BRUCE-LEE-STICKERS-FIERCE-25PK-001-500x500.jpg')

    embed.add_field(
        name = '!help', 
        value = 'List all the commands',
        inline = False
    )

    embed.add_field(
        name = '!chatbot',
        value = 'Engage the bot',
        inline = False
    )
    await ctx.send(embed=embed)



@bot.command()
async def chatbot(ctx, *, prompt: str):
    # Use ChatGPT to generate a response
    completions = openai.Completion.create(
        engine="text-davinci-002", 
        prompt=prompt, 
        max_tokens=1024, 
        n=1,
        stop=None,
        temperature=0.5
        )
    response = completions.choices[0].text
    await ctx.send(response)



bot.run(DISCORD_TOKEN)
