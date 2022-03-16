########################################################
########################################################


##INSERTS INTO index.py's dedicated space

import random

watching_status = ["Netflix", "Youtube"]
playing_status = ["Among Us", "games"]
listening_status = ["Music", "Podcast"]

def random_status():
    randomNum = random.randint(0, 2)
    if randomNum == 0:
        return client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(watching_status)))
    elif randomNum == 1:
        return client.change_presence(activity=discord.Game(name=random.choice(playing_status)))
    elif randomNum == 2:
        return client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=random.choice(listening_status)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if client.user.mentioned_in(message):
        if "change status" in message.content:
            await random_status()

########################################################
########################################################
