import discord
import os
import psycopg2
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import random
load_dotenv()
POSTGRESQL_PASSWORD =os.environ['PASSWORD']
# ENCRIPTION_KEY= os.environ['ENCRIPTION_KEY']
USER= os.environ['USER']
# encryption_object=Fernet(ENCRIPTION_KEY)
##set up psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="group_project",
        user= USER,
        password=POSTGRESQL_PASSWORD)
cursor = conn.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Connection established to: ",data)
##psycopg2 setting up tables for database
cursor.execute("""
        create table IF NOT EXISTS server (
        id serial primary key,
        server_name varchar(255)
        );
        create table IF NOT EXISTS person (
        id serial primary key,
        username varchar (255) unique,
        discord_id varchar (255),
        server_id integer references server(id) ON DELETE CASCADE
        );
        create table IF NOT EXISTS playlist (
        id serial primary key,
        name varchar (255),
        my_person integer references person (id) ON DELETE CASCADE
        );
        create table IF NOT EXISTS song(
        id serial primary key,
        link varchar (500),
        person_id varchar (255),
        my_playlist integer references playlist ON DELETE CASCADE
        );
        """)
conn.commit()


def intialize_server():
    cursor.execute("""
    select id from playlist where name='server playlist';
        """)
    try:
        id_of_new_row = cursor.fetchone()[0]
    except:
        cursor.execute("""
        insert into playlist (name) values ('server playlist') on conflict do nothing;
            """)
        conn.commit()

def add_to_playlist(link):
    cursor.execute("""
    select id from playlist where name='server playlist';
    """)
    id_of_new_row = cursor.fetchone()[0]
    # print(id_of_new_row)
    cursor.execute(f"""
    insert into song (link, my_playlist) values ('{link}', 
    {id_of_new_row})
    """)
    conn.commit()

def create_playlist(playlist, author):
    cursor.execute(f"""
    insert into person (username) values ('{author}') on conflict do nothing;
    select id from person where username='{author}';
    """)
    conn.commit()
    id_of_author = cursor.fetchone()[0]
    playlist=playlist[17:]
    # print(playlist)
    cursor.execute(f"""
    select id from playlist where name='{playlist}' and my_person={id_of_author};
    """)
    try:
        dummy_id = cursor.fetchone()[0]
    except:
        cursor.execute(f"""
        insert into playlist (name, my_person) values ('{playlist}', {id_of_author})
        """)    
        conn.commit()
    cursor.execute(f"""
        select name from playlist where my_person={id_of_author};
        """)  
    conn.commit()
    exit_string=""
    for x in cursor.fetchall():
        # print(x[0])
        exit_string+=x[0]+"\n"
    return f"Your playlists are now...\n{exit_string}"

def list_playlists(author):
    cursor.execute(f"""
    insert into person (username) values ('{author}') on conflict do nothing;
    select id from person where username='{author}';
    """)
    conn.commit()
    id_of_author = cursor.fetchone()[0]
    cursor.execute(f"""
    select name from playlist where my_person={id_of_author};
    """)  
    conn.commit()
    exit_string=""
    for count, x in enumerate(cursor.fetchall()):
        # print(x[0])
        exit_string+=str(count+1)+". "+x[0]+"\n"
    return f"Your playlists are...\n{exit_string}"

def list_song(message, author):
    cursor.execute(f"""
    insert into person (username) values ('{author}') on conflict do nothing;
    select id from person where username='{author}';
    """)
    conn.commit()
    id_of_author = cursor.fetchone()[0]
    playlist_name=message[12:]
    # print(playlist_name)
    cursor.execute(f"""
    select id from playlist where my_person={id_of_author} and name='{playlist_name}';
    """) 
    playlist_id=cursor.fetchone()[0]
    cursor.execute(f"""
    select link from song where my_playlist={playlist_id};
    """)     
    exit_string=""
    for count, x in enumerate(cursor.fetchall()):
        # print(x[0])
        exit_string+=str(count+1)+". "+x[0]+"\n"
    return f"The songs in {playlist_name} are...\n{exit_string}"




def add(message, author):
    cursor.execute(f"""
    insert into person (username) values ('{author}') on conflict do nothing;
    select id from person where username='{author}';
    """)
    conn.commit()
    id_of_author = cursor.fetchone()[0]
    message=message[5:]
    message=message.split(" to ")
    song_url=message[0]
    playlist=message[1]
    # print(song_url, playlist)
    cursor.execute(f"""
    select id from playlist where my_person={id_of_author} and name='{playlist}';
    """) 
    id_of_playlist = cursor.fetchone()[0]
    cursor.execute(f"""
    insert into song (link, my_playlist, person_id) values ('{song_url}', 
    {id_of_playlist}, {id_of_author})
    """) 
    conn.commit()
    return "Added"

def delete_song(message, author):
    cursor.execute(f"""
    insert into person (username) values ('{author}') on conflict do nothing;
    select id from person where username='{author}';
    """)
    conn.commit()
    id_of_author = cursor.fetchone()[0]
    message=message[13:]
    message=message.split(" from ")
    song_url=message[0]
    playlist=message[1]
    cursor.execute(f"""
    select id from playlist where my_person={id_of_author} and name='{playlist}';
    """)
    try:
        id_of_playlist = cursor.fetchone()[0]
    except:
        return "You do not have a playlist named this"
    string=(f"delete from song where link='{song_url}' and my_playlist={id_of_playlist}")
    # print(string)
    cursor.execute(f"""
    delete from song where link='{song_url}' and my_playlist={id_of_playlist}
    """) 
    conn.commit()
    return "Deleted"

def delete_playlist(playlist, author):
    try:
        playlist=playlist[17:]
        cursor.execute(f"""
        insert into person (username) values ('{author}') on conflict do nothing;
        select id from person where username='{author}';
        """)
        conn.commit()
        id_of_author = cursor.fetchone()[0]
        cursor.execute(f"""
            select id from playlist where my_person={id_of_author} and name='{playlist}';
            """)
        conn.commit()
        id_of_playlist = cursor.fetchone()[0] 
        cursor.execute(f"""
            delete from playlist where id='{id_of_playlist}' and my_person={id_of_author}
            """)
        conn.commit()
        return "deleted"
    except:
        return "You spelled something wrong. Please try again"
    

def play_playlist(playlist, author):
    try:
        cursor.execute(f"""
        insert into person (username) values ('{author}') on conflict do nothing;
        select id from person where username='{author}';
        """)
        conn.commit()
        id_of_author = cursor.fetchone()[0]
        cursor.execute(f"""
        select id from playlist where my_person={id_of_author} and name='{playlist}';
        """)
        conn.commit()
        id_of_playlist = cursor.fetchone()[0] 
        cursor.execute(f"""
        select link from song where my_playlist='{id_of_playlist}';
        """)
        exit_list=[]
        for x in cursor.fetchall():
            exit_list.append(str(x[0]))
        random.shuffle(exit_list)
        return exit_list
    except:
        return []
       
 ##this logs every discord message into the database, by encrypting it so it is unable to break postgresql
        
# async def on_message(message):

#     encrypted=encryption_object.encrypt(message.content.encode())
#     encrypted=str(encrypted, 'UTF-8')
#     postgres_insert=f"INSERT INTO user_messages (message_content) values ('{encrypted}')"
#     # decrypted=encryption_object.decrypt(encrypted)
#     # print(postgres_insert)
#     # print(encrypted)
#     # print(decrypted)
#     cursor.execute(postgres_insert)
#     conn.commit()
#     if message.content.startswith('$hello'):
#         await message.channel.send('nobody likes you!')


