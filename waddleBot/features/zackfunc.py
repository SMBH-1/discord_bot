import requests 
import os
import pytz
import datetime
from dotenv import load_dotenv

load_dotenv()

def cat_picture():
    print('CAT')
    cat_key = os.environ['CAT']
    response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={cat_key}')
    data = response.json()
    url = data[0]['url']
    print(url, data)
    return url

def glad_check(p_message):
    wow_key = os.environ['WOW']
    args = p_message[8:].split('-')
    print(args)
    realm = args[1].split()
    print('realm: ' ,realm)
    if len(realm) > 1:
        realmSlug = f'{realm[0]}-{realm[1]}'
        print('f realm: ', realm)
    else:
        realmSlug = realm[0]
    char_name = args[0]
    print('name: ',char_name)
    response = requests.get(f'https://us.api.blizzard.com/profile/wow/character/{realmSlug}/{char_name}/achievements?namespace=profile-us&locale=en_US&access_token={wow_key}')
    data = response.json()
    achievements = data['achievements']
    glads = []
    glad_str = ''
    for item in achievements:
        print(item.get('Gladiator'))

        if 'Gladiator' in item['achievement']['name'] and "'s" not in item['achievement']['name']:
            print('list', item['achievement']['name'])
            glad = item['achievement']['name']
            glad_str += f'{glad}\n'
    if len(glad_str) < 1:
        print('empty glad list')
        return f'`{char_name} is boosted.`'
    else:
        return f'```{char_name.title()}:\n{glad_str}```'
    
def schedule(p_message):
    print('schedule')
    events = {}
    # Split message into a list of arguments
    args = p_message.split()

    # The first argument is the event name
    event_name = args[1]
    
    # The second argument is the timezone
    timezone = args[2]
    
    # The third argument is the date and time in the format "YYYY-MM-DD HH:MM"
    event_time_str = args[3]
    event_time = datetime.datetime.strptime(event_time_str, "%m%d%H%M")
    
    # Set the event time to the specified timezone
    tz = pytz.timezone(timezone)
    event_time = tz.localize(event_time)
    
    # Store the event in the dictionary
    events[event_name] = event_time
    
    # Send a confirmation message
    return f"Event '{event_name}' scheduled for {event_time}."