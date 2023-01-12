import discord
import random
from discord.ext import commands
import requests
import json

def test_command():
    return ':stuck_out_tongue_winking_eye:'

def roll(p_message):
    work_list = p_message.split(' ')
    command = work_list[1].split('d')
    number_of_dice = int(command[0])
    max_value_of_dice = int(command[1])
    results = []
    i = 1
    while i <= number_of_dice:
        die = random.randint(1, max_value_of_dice)
        results.append(die)
        i += 1
    total = sum(results)
    return f'{results} = [{total}]'

global initiative_pool
initiative_pool = {}

def initiative(p_message):
    work_list = p_message.split(' ')
    crit_message = ''
    character_id = work_list[1]
    initiative_modifier = work_list[2]
    if initiative_modifier[0] == '+':
        initiative_modifier = initiative_modifier[1:]
    elif initiative_modifier[0] == '-':
        pass
    initiative_roll = random.randint(1, 20)
    if initiative_roll == 20:
        crit_message = '\nOMG! NAT 20 \n woooo! :sunglasses:'
    elif initiative_roll == 1:
        crit_message = '\nooof, nat 1 \n aww man :cry:'
    initiative_roll = initiative_roll + int(initiative_modifier)
    initiative_pool.update({f'{character_id} rolled': initiative_roll})
    return f'{character_id} rolled: {initiative_roll}{crit_message}'

def run_initiative():
    global initiative_pool
    work_list = initiative_pool
    response = dict(sorted(work_list.item(), key=lambda item:item[1], reverse=True))
    return f'{response}'

def condition(p_message):
    parse_from_message = p_message.split(' ')
    search_term = parse_from_message[1]
    if search_term == 'list':
        return '`blinded, charmed, deafened,` \n`exhaustion, frightened, grappled,` \n`incapacitated, invisible, paralyzed,` \n`petrified, poisoned, prone,` \n`restrained, stunned, unconscious`'
    else:
        try:
            response = requests.get(f'https://www.dnd5eapi.co/api/conditions/{search_term}').json()
            name = response['name']
            description = response['desc']
            reply = ''
            for rule in description:
                reply = reply + str(rule) + '\n'
            return f'{name} \n {reply}'
        except:
            return f'{search_term} not a valid search term, try `!condition list` for a list of valid terms'

def clear_init():
    global initiative_pool
    initiative_pool = {}
    return 'The Initiative Pool has been reset.'