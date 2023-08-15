import discord
from bot.responses import handle_response
import logging
from pprint import pprint
from bot.reactions import reaction_add_handler, reaction_remove_handler

logger = logging.getLogger(__name__)

def run_bot():
    with open('token.txt','r') as t:
        TOKEN = t.read()
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.reactions = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        try:
            await message.channel.send(handle_response(message))
        except Exception as e:
            print(e)
    
    @client.event
    async def on_reaction_add(reaction, user):
        print('reaction added')
        new_content = reaction_add_handler(reaction=reaction,user=user)
        message = await client.get_channel(reaction.message.channel.id).fetch_message(reaction.message.id)
        await message.edit(content=new_content)

    @client.event
    async def on_reaction_remove(reaction,user):
        print('reaction removed')
        new_content = reaction_remove_handler(reaction=reaction,user=user)
        message = await client.get_channel(reaction.message.channel.id).fetch_message(reaction.message.id)
        await message.edit(content=new_content)

    client.run(TOKEN)