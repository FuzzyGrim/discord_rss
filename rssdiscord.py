# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='add', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx, link, alias='No alias provided'):

    response = 'Nice'
    await ctx.send(response)

bot.run(TOKEN)

rss_list = []

