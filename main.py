import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')

@client.event
async def on_typing(channel, user, when):
    await channel.send('Someone is typing...')

@client.event
async def on_message_delete(message):
    await message.channel.send('Someone deleted a message')

@client.event
async def on_message_edit(before, after):
    await before.channel.send('Someone edited a message')

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'Someone add a {reaction} reaction')

client.run(os.getenv('TOKEN'))