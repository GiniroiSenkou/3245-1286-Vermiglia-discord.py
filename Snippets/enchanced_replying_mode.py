########################################################
########################################################

##INSERTS INTO index.py's dedicated space


import random

greetings = ["hey",  "hello", "hi", "hello there", "hi there", "hey there", "hi", "greetings"]

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    message.content = message.content.lower()


    def client_replies(content):
        content = random.choice(content)
        #If you want to log messages from its DMs
        if config.getboolean('SETTINGS', 'debug'):
            if message.guild is None:
                print(current_time() + "-------DM------- \n" + message.author.name + ": " + message.content)
            else:
                print(f"{client_name}: {content}")
                print("----------------")
                print(f'To: {message.author.name} \n{current_time()}{client_name}: {content}\n ----------------')

        randomNum = random.randint(0, 2)
        if randomNum == 0:
            return message.channel.send(content)
        elif randomNum == 1:
            return message.channel.send(f"{message.author.mention} {content}")
        elif randomNum == 2:
            return message.reply(content)

    if client.user.mentioned_in(message) or message.guild is None:
        print(message.content)
        if any(word in message.content for word in greetings):
            await client_replies(greetings)
