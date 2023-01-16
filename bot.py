import discord




TOKEN = "INSERT YOUR DISCORD BOT TOKEN HERE"
client = discord.Client()


@client.event
async def on_ready():
    print('Bot {0.user} is logged on and ready to go!'.format(client))



@client.event
async def on_message(message):
    
    #Prevents looping of the bot responding to itself
    if message.author == client.user:
        return
    
    #Logs all user activity in VSCode Terminal alongside the bot responces
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    #Prints the Username, Message, and the Channel to the console
    print(f'{username}: {user_message} ({channel})')

    #Filters messages for the !Hello command and responds accordingly 
    if user_message.lower() == '!Hello':
            await message.channel.send('Hello @' + username)
    
    
#Starts the discord bot
client.run(TOKEN)
