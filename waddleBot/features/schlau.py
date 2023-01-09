import discord
import os
import psycopg2
from dotenv import load_dotenv
from cryptography.fernet import Fernet
load_dotenv()
##Bot token
BOT=os.environ['BOT']
##a password to a user wihtin postgresql is required to connect to postgresql
TOKEN=os.environ['TOKEN']
##a consistent encryption key is required to consistently encrypt and decode database information
ENCRIPTION_KEY=os.environ['ENCRIPTION_KEY']
encryption_object=Fernet(ENCRIPTION_KEY)
##this conn object connects to database and allows changes
conn = psycopg2.connect(
    host="localhost",
    database="group_project",
    user="sevastians",
    password=TOKEN)
cursor = conn.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Connection established to: ",data)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
##this logs every discord message into the database, by encrypting it so it is unable to break postgresql
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        encrypted=encryption_object.encrypt(message.content.encode())
        encrypted=str(encrypted, 'UTF-8')
        postgres_insert=f"INSERT INTO user_messages (message_content) values ('{encrypted}')"
        # decrypted=encryption_object.decrypt(encrypted)
        # print(postgres_insert)
        # print(encrypted)
        # print(decrypted)
        cursor.execute(postgres_insert)
        conn.commit()
    if message.content.startswith('$hello'):
        await message.channel.send('nobody likes you!')

client.run(BOT)


async def test(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('nobody likes you!')

conn.close()