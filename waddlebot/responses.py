import random 
import zackfunc
from dotenv import load_dotenv

load_dotenv()

def handle_response(message) -> str:
    # Standardize input
    p_message = message.lower()

    # Help function 
    #TODO: add all possible commands with brief description (maybe some formatting as well?)
    if p_message == 'help':
        return "```Try the following commands:\nhello - receive a friendly greeting from WaddleBot\nroll - feeling lucky? roll the dice\nmeow - generate a random kitty pic\n!lookup (characterName-realmName) - check WoW character for Gladiator achievement```"

    if p_message == 'hello':
        return 'fuck off'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    

    # grab random cat picture using thecatapi
    if p_message == 'meow':
        return zackfunc.cat_picture()
    
    if p_message.startswith('!schedule'):
        return zackfunc.schedule(p_message)
    
    if p_message.startswith('!lookup'):
        return zackfunc.glad_check(p_message)
        
        
            
            


    