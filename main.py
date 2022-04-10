import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix='$')

for file in os.listdir("./commands"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"commands.{name}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(os.getenv('TOKEN'))