import discord
import os
import psycopg2
from dotenv import load_dotenv
from cryptography.fernet import Fernet


class botBot():
    def __init__(self):
        load_dotenv()
        ##Bot token
        # self.BOT=os.environ['BOT']
        ##a password to a user wihtin postgresql is required to connect to postgresql
        self.PASSWORD=os.environ['PASSWORD']
        ##a consistent encryption key is required to consistently encrypt and decode database information
        self.ENCRIPTION_KEY=os.environ['ENCRIPTION_KEY']
        self.encryption_object=Fernet(self.ENCRIPTION_KEY)
        ##this conn object connects to database and allows saving
        self.conn = psycopg2.connect(
        host="localhost",
        database="group_project",
        user="sevastians",
        password=self.PASSWORD)
        ##config of psycopg2 connection
        self.cursor = self.conn.cursor()
        self.cursor.execute("select version()")
        data = self.cursor.fetchone()
        print("Connection established to: ",data)
        #database set up
        self.cursor.execute("drop database if exists group_project;")


        ##this logs every discord message into the database, by encrypting it so it is unable to break postgresql
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            else:
                encrypted=self.encryption_object.encrypt(message.content.encode())
                encrypted=str(encrypted, 'UTF-8')
                postgres_insert=f"INSERT INTO user_messages (message_content) values ('{encrypted}')"
                # decrypted=encryption_object.decrypt(encrypted)
                # print(postgres_insert)
                # print(encrypted)
                # print(decrypted)
                self.cursor.execute(postgres_insert)
                self.conn.commit()
            if message.content.startswith('$hello'):
                await message.channel.send('nobody likes you!')


