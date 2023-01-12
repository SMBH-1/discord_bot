import openai       # pip install openai
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# DISCORD_TOKEN = os.getenv('spence_bot_token')

openai.api_key = os.getenv('openai_api_key')

# intents = discord.Intents.all()
# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!', intents=intents) 

# bot.remove_command('help')

# @bot.command()
async def helpbot(ctx):
    embed = discord.Embed(
        title = 'Bot Command',
        description = 'Welcome to the help section. Here are all the commands for the chatbot.',
        color = discord.Color.green()
    )

    embed.set_thumbnail(url='https://www.longboarderlabs.com/wp-content/uploads/2019/11/DGK-X-BRUCE-LEE-STICKERS-FIERCE-25PK-001-500x500.jpg')

    embed.add_field(
        name = '!helpbot', 
        value = 'List all the commands',
        inline = False
    )

    embed.add_field(
        name = '!chatbot',
        value = 'Engage the bot',
        inline = False
    )
    return embed



# @bot.command()
def chatbot(prompt):
    prompt=prompt[8:]
    print(prompt)
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
    print(response)
    return response


# @bot.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description

    owner = ctx.guild.owner
    id = ctx.guild.id
    memberCount = ctx.guild.member_count    

    embed = discord.Embed(
        title = name + "Server Information",
        description = description,
        color = discord.Color.blue()
    )
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Penguin_%28Oswald_Cobblepot%29.png/220px-Penguin_%28Oswald_Cobblepot%29.png")
    embed.add_field(
        name = "Owner", 
        value = owner, 
        inline = False
    )
    embed.add_field(
        name = "Server ID", 
        value = id, 
        inline = False
    )
    embed.add_field(
        name = "Member Count", 
        value = memberCount, 
        inline = False
    )

    await ctx.send(embed=embed)


# bot.run(DISCORD_TOKEN)
