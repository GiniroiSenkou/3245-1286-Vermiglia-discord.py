client_logo = """ 
_________                .__.__  .__        
\_   ___ \  ____   _____ |__|  | |__|____   
/    \  \/_/ __ \ /     \|  |  | |  \__  \  
\     \___\  ___/|  Y Y  \  |  |_|  |/ __ \_
 \______  /\___  >__|_|  /__|____/__(____  /
        \/     \/      \/                \/ (Discord) """

import asyncio
import configparser
from datetime import datetime
import os, os.path
import platform
import time

### Current Date&Time Function
def current_time():
    cdate = datetime.now().strftime('[%D]{%H:%M}--> ')
    return cdate

### Check If Libraries are loaded (Add anything that you install on Later )
try:
    import discord
    from discord.ext import commands
except ImportError:
    print(f"This package is missing: {ImportError}\n (python -m pip install -r requirements.txt)")
    exit()

### Check if config.ini exists
config = configparser.ConfigParser(allow_no_value=True)
if os.path.isfile('config.ini') and os.path.getsize('config.ini') > 0:
    pass
else:
    print(current_time() + 'ERROR! config.ini file is missing or is empty!')
    quit()

### Load external configuration file
try:
    config.read('config.ini')
except Exception as err:
    print(current_time() + 'ERROR! config.ini file might be corrupted!')
    quit()

#INTENTS are mandatory to let the bot access data. On your developer discord page you must enable the Intents.
intents = discord.Intents(guild_messages = True, members = True, guilds=True, emojis=True, voice_states=True, presences=True, message_content = True)
client = commands.Bot(command_prefix = "!", intents=intents)

client_name = config['SETTINGS']['client_name']

is_client_already_connected = False


@client.event
async def on_ready():
    global is_client_already_connected
    if not is_client_already_connected:
        if config.getboolean('SETTINGS', 'debug'):
            print(client_logo + "debugging mode")
            print('-' * 50)
            print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,platform.python_version()))
            print("Discord Intent status:  ")
            print(' | '.join(map(str, intents)))
            print('-' * 50)
        else:
            print(client_logo)

        is_client_already_connected = True
        print(current_time() + client_name + ' is Online and Ready.')
    else:
        print(current_time() + client_name + 'Successfully reconnected and back Online!')


########################################################
########################################################


##INSERTS SNIPPETS HERE FROM THE GITHUB FOLDER SNIPPETS



########################################################
########################################################

is_client_offline = False
while True:
    try:
        client.run(config['SETTINGS']['client_token'])
    except KeyboardInterrupt:
        print(current_time() + 'Ctrl+C Pressed! Quitting '+ client_name)
        exit()
    except BaseException:
        if not is_client_offline:
            print(current_time() + client_name + ' is disconnected! Attempting to reconnect every {} seconds!'.format(
                config['SETTINGS']['reconnect_client_every_sec']))
            is_client_offline = True
        time.sleep(int(config['SETTINGS']['reconnect_client_every_sec']))
