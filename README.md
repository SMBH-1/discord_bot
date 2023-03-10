# Waddle Bot

![](https://marketsplash.com/content/images/2022/03/Group-83.png)


Waddle Bot is a software application that can be run in your Discord server. The bot provides various features to spruce up and add some flavor to your server. These features include:

- Chat Bot
- YouTube Notification Functionality
- YouTube Music Functionality in Voice Channels
- DnD Functionality
- WoW Functionality
- Lottery Drawings and Information
- Notification System
- And an assortment of gifs, reactions, and art


## Installation
You will need to install pip, the Python package installer, and create and activate a virtual environment (venv) before installing the required dependencies from the requirements.txt file in this repo. Run the following commands:

Note: The following commands are for Linux and macOS
```
pip install pip
python3 -m venv [NAME OF VENV HERE]
source [FILE PATH OF YOUR VENV HERE]/bin/activate
pip install -r requirements.txt
```

## Using Waddle Bot
In order to use this application, check the Waddle Bot landing page [HERE](https://discord.com/oauth2/authorize?client_id=1060252204461740173&permissions=4398046511091&scope=bot) to add Waddle Bot to your Discord server. 



## API Keys
You will need keys from the following APIs to access all of Waddle Bot's functionality:
- [Cat API](https://thecatapi.com/)
- [World of Warcraft API](https://develop.battle.net/documentation/world-of-warcraft/game-data-apis)
- [OpenAI API](https://openai.com/api/)
- [GIPHY API](https://developers.giphy.com/)


## Database Setup
You will also need to have a database to track your music playlist. Waddle Bot is set up with PostgreSQL and psycopg2. Add your RDBMS User and Password information into the .env file:

```
USER = [YOUR PSYCOPG2 USERNAME]
PASSWORD = [YOUR PSYCOPG2 PASSWORD]
```

## YouTube Notification Setup
In order to alert one of your discord channels of a video upload, you will need to modify the youtube_data.json file in the waddleBot folder as such:
```
{"[INSERT YOUTUBE CHANNEL ID HERE]": {"channel_name": "[INSERT THE YOUTUBE CHANNEL NAME HERE]", "latest_video_url": "none", "notifying_discord_channel": "[INSERT YOUR DISCORD CHANNEL ID HERE - the Discord channel you want the videos posted to]"}}
```


## Connecting Waddle Bot to Your Discord Server
After connecting Waddle Bot, you will need to:
1. Create a .env file inside the waddleBot folder
2. Add your bot's token in your .env file

    `TOKEN = [YOUR BOT TOKEN HERE]`

3. Run your bot

    `python3 main.py` 


## Waddle Bot Features


### Chat Bot
Waddle Bot provides basic chat functionality while also using OpenAI's text-davinci-002 model for supplemental support. 

Commands Include:
```
!helpbot //Lists all bot commands
!chatbot //Engages chat functionality
!server //Provides server specific information (server name, owner, and member count) 
```


### Play Music in Voice Channels (YouTube)
Waddle Bot can play music from YouTube. The following commands allow voice channel users to modify playlists.

Commands Include:
```
!create_playlist
!list_playlists
!list_songs
!add
!delete_song
!delete_playlist
```

WaddleBot can also use slash commands in your text box to perform similar commands:
```
/clear //Stops current song and clears queue
/help //Displays available commands
/play 
/pause
/resume
/skip
/playlist //Shows playlist
/queue //Displays current queue
/leave //Removes bot from voice channel
```



### Notifications for YouTube Videos
The feature is set to check the specified YouTube channel every 5 minutes for new uploads. When a video is uploaded, Waddle Bot will post a message with a link to the new video and will tag everyone in the server. See YouTube Notification Setup section above for more information.


### DnD Functionality
Waddle Bot can perform a series of actions for your DnD game:
```
!roll //rolls die and generates number
!init 
!run_init
!condition list //shows list of all possible conditions
!condition [name of condition] //provides a summary of the specified condition
!clear_init
```

### Lottery Functionality
Waddle Bot will generate random lottery numbers for you to use (that have not been used before). The Bot will also provide you with the latest winning numbers for the Mega Millions Lottery.

```
!win //Generates numbers for you
!latest_draw //Shows latest drawing numbers
```


### GIFs, Reactions, and Images
Using a series of commands, Waddle Bot can return gifs and images.

```
!meow //Generates random cat picture
!waddle draw [INSERT YOUR REQUEST HERE] //Waddle will draw you an image
!gif [INSERT YOUR SEARCH HERE] //Returns a gif that matches your search term 
```



### WoW Functionality
[Under Construction]


### Notification System
[Under Construction]




## Additional API Documentation

- [Discord API](https://discord.com/developers/docs/intro)
  - [discord.py API](https://discordpy.readthedocs.io/en/stable/api.html)
- [YouTube API](https://developers.google.com/youtube/v3)
    - [YouTube DL](https://github.com/ytdl-org/youtube-dl)
- [OpenAI API](https://beta.openai.com/overview)
- [Mega Millions API](https://rapidapi.com/avoratechnology/api/mega-millions/details)
- [Cat API](https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t)
- [GIPHY API](https://developers.giphy.com/docs/api#quick-start-guide)
- [WoW API](https://develop.battle.net/documentation/world-of-warcraft/game-data-apis)
