import discord
from responses import handle_response
import logging
from pprint import pprint

logger = logging.getLogger(__name__)

def run_bot():
    TOKEN = 'MTEzOTk5NTg5ODI0MDMwMzE4NA.GcIeA6.Voc7J3L8WEfxS243L39qSqTFUbxxOVnZAeEqGw'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        try:
            await message.channel.send(handle_response(message.content))
        except Exception as e:
            print(e)
    
    @client.event
    async def on_reaction_add(reaction, user):
        
        await reaction.message.channel.send(f'''
{user} reacted!
Reaction: {reaction.emoji}
Message: \'{reaction.message.content}\'
From: {reaction.message.author}
In: {reaction.message.channel.id}
        ''')



    client.run(TOKEN)