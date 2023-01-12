import random 
from features import zackfunc, spencefunc, dariusfunc, kevfunc
from dotenv import load_dotenv
import os
load_dotenv()

def handle_response(message, author) -> str:
    # Standardize input
    p_message = message.lower()

    # Help function 
    #TODO: add all possible commands with brief description (maybe some formatting as well?)
    if p_message == 'help':
        return "```Try the following commands:\nhello - receive a friendly greeting from WaddleBot\nroll - feeling lucky? roll the dice\nmeow - generate a random kitty pic\n!lookup (characterName-realmName) - check WoW character for Gladiator achievement```"

    # if p_message == 'hello':
    #     return 'fuck off'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    

    # grab random cat picture using thecatapi
    if p_message == 'meow':
        return zackfunc.cat_picture()
    
    if p_message.startswith('!schedule'):
        return zackfunc.schedule(p_message)
    
    if p_message.startswith('!lookup'):
        return zackfunc.glad_check(p_message)

    # Chatbot commands
    if p_message == '!helpbot':
        return spencefunc.helpbot(p_message)

    if p_message == '!chatbot':
        return spencefunc.chatbot(p_message)
    

    # LottoBotto commands
    if p_message == '!win':
        return dariusfunc.generate()
    
    if p_message == '!lastest draw':
        return dariusfunc.get_latest_draw()
    
    # Server Stats
    if p_message == '!server':
        return spencefunc.server(p_message)
        
    # DnD Commands
    if p_message.startswith('!roll'):
        return kevfunc.roll(p_message)
    
    if p_message.startswith('!init'):
        return kevfunc.initiative(p_message)

    if p_message.startswith('!run_init'):
        return kevfunc.initiative()

    if p_message.startswith('!condition'):
        return kevfunc.condition(p_message)
            

    #playlist functionality
    if '!create_playlist' in p_message:
        return sevfunc.create_playlist(p_message, author)

    if '!list_playlists' in p_message:
        return sevfunc.list_playlists(author)

    if '!list_songs' in p_message:
        return sevfunc.list_song(p_message, author)

    if '!add' in p_message:
        return sevfunc.add(p_message, author)
    
    if '!delete_song' in p_message:
        return sevfunc.delete_song(p_message, author)\

    if '!delete_playlist' in p_message:
        return sevfunc.delete_playlist(p_message, author)
    
    # Generates DALL-E Image
    if p_message.content.startswith('!waddle draw'):
        return sidfunc.generate_dall_e_img(p_message)        
    
    #Generates gif from GIPHY
    if p_message.content.startswith('!gif'):
        return sidfunc.gif_finder(p_message)
    