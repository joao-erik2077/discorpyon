import discord
from discord.ext import commands, tasks
import random

class Joke(commands.Cog):
    jokes = [
        'What kind of exercise do lazy people do? Diddly-squats.',
        'What do you call a pony with a cough? A little horse!',
        'What is Forrest Gump\'s password? 1Forrest1.',
        'Why did the M&M go to school? He wanted to be a Smartie.',
        'What did one traffic light say to the other? Stop looking at me, I\'m changing!'
        ]

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def joke(self, ctx):
        i = random.randint(0, 4)
        await ctx.send(self.jokes[i])

def setup(bot):
    bot.add_cog(Joke(bot))