import discord
import random
from discord.ext import commands
import requests
import json

class Dungeon_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    global initiative_pool
    initiative_pool = {}
        
    
    #* User Commands

    @commands.command()
    async def yo(self, ctx):
        #* simple test command to check that the bot is online and recieving commands
        await ctx.channel.send(':stuck_out_tongue_winking_eye:')

    @commands.command(name='roll', aliases=['r'])
    async def roll(self, ctx):
        if ctx.message.content[2] == ' ':
            #* Alias 'r' was used
            work_string = ctx.message.content[3:]
        else:
            work_string = ctx.message.content[6:]
        work_list = work_string.split('d')
        number_of_dice = int(work_list[0])
        max_value_of_die = int(work_list[1])
        results = []
        i = 1
        while i <= number_of_dice:
            die = random.randint(1, max_value_of_die)
            results.append(die)
            i += 1
        total = sum(results)
        await ctx.channel.send(f'{ctx.message.author.nick} rolled: \n{results} = [{total}]')
        return

    @commands.command(name='init', aliases=['i'])
    async def init(self, ctx):
        #*This function grabs a user nickname and their iniative modifier
        #*then stores it in a global dictionary to be called by the 'run_init' func
        #! INTENTIONAL LIMITATION: Dictionaries may not have duplicate keys
        #! therefore, a user may not have multiple key/value pairs.
        #! Dungeon Masters may use the 'dm_init' func to work around the limitation
        if ctx.message.content[2] == ' ':
            #* Alias 'i' was used
            work_string = ctx.message.content[3:]
            initiative_modifier = work_string
        else:
            work_string = ctx.message.content[6:]
            initiative_modifier = work_string
            #* Checking for '-' or '+'
            if initiative_modifier[0] == '+':
                initiative_modifier = initiative_modifier[1:]
            elif initiative_modifier[0] == '-':
                pass
            else:
                await ctx.channel.send(f'Sorry {ctx.message.author.nick} \nCommand syntax invalid.')
        initiative_modifier = int(initiative_modifier)
        initiative_roll = random.randint(1, 20)
        critical_message = ''
        if initiative_roll == 20:
            critical_message = '\nWOO! A NAT 20 :grin:'
        if initiative_roll == 1:
            critical_message = '\noof, critical fail :smiling_face_with_tear:'
        initiative_roll += initiative_modifier
        user = ctx.message.author.nick
        initiative_pool.update({f'{user} rolled': initiative_roll})
        await ctx.channel.send(f'{user} rolled: {initiative_roll}{critical_message}')

    @commands.command(name='run_init', aliases=['run', 'ri'])
    async def run_init(self, ctx):
        #* This function collects the user input data regarding initiative
        #* and returns it sorted from highest roll to lowest roll.
        global initiative_pool
        work_list = initiative_pool
        response = dict(sorted(work_list.items(), key=lambda item:item[1], reverse=True))
        await ctx.channel.send(f'{response}')
        initiative_pool = {}

    @commands.command(name='dm_init', aliases=['di', 'd', 'dmi'])
    async def dm_init(self, ctx):
        #* Alternate function to allow the game DM to input multiple initiative rolls
        #* We are looking for inputs that look like this:
            #! $di `NPC identifier` `+/-n`
        work_list = ctx.message.content.split(' ')
        npc_id = work_list[1]
        initiative_modifier = work_list[2]
        if initiative_modifier[0] == '+':
            initiative_modifier = initiative_modifier[1:]
        elif initiative_modifier[0] == '-':
            pass
        else:
            await ctx.channel.send(f'Sorry {ctx.message.author.nick} \nCommand syntax invalid.')
        initiative_roll = random.randint(1, 20) + int(initiative_modifier)
        initiative_pool.update({f'{npc_id} rolled': initiative_roll})
        await ctx.channel.send(f'{npc_id} rolled: {initiative_roll}')

    @commands.command(name='condition', aliases=['cond', 'c'])
    async def condition(self, ctx):
        parse_from_message = ctx.message.content.split(' ')
        search_term = parse_from_message[1].lower()
        if search_term == 'list':
            await ctx.channel.send('`blinded, charmed, deafened,` \n`exhaustion, frightened, grappled,` \n`incapacitated, invisible, paralyzed,` \n`petrified, poisoned, prone,` \n`restrained, stunned, unconscious`')
        else:
            try:
                response = requests.get(f'https://www.dnd5eapi.co/api/conditions/{search_term}').json()
                name = response['name']
                description = response['desc']
                reply = ''
                for rule in description:
                    reply = reply + str(rule) + '\n'
                await ctx.channel.send(f'{name} \n {reply}')
            except:
                await ctx.channel.send(f'{search_term} is not a valid command.')

    async def setup(bot: commands.Bot):
        await bot.add_cog(Dungeon_Cog(bot), guilds=[discord.Object(id=1057755148862099536), discord.Object(id=1057692804865855652)])
