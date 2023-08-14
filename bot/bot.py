import discord
from bot.responses import handle_response
import logging
from pprint import pprint
from bot.reactions import reaction_handler

logger = logging.getLogger(__name__)

def run_bot():
    TOKEN = 'MTEzOTk5NTg5ODI0MDMwMzE4NA.G1dEm3.JE09MFVYCmk6TedBLOjdv8rNOmJdlHRDTV9QZM'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        logger.info(f'{client.user} is running!')

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
        new_content = reaction_handler(reaction=reaction,user=user)
        message = await client.get_channel(reaction.message.channel.id).fetch_message(reaction.message.id)
        await message.edit(content=new_content)

    client.run(TOKEN)