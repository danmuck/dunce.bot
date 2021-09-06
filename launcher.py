# import discord, os 
# from discord.ext import commands
# from discord.ext.commands.core import command 
from lib.bot import bot
VERSION = '0.0.8'

#end ---
bot.run(VERSION)







############################ OLD ############################
#client = commands.Bot(command_prefix='?')

# login messages --------------------------------------------
# @client.event
# async def on_ready():
#     print('\nYou have logged in as {0.user}'.format(client))

# @client.event
# async def on_connect():
#     print('\nDunce connected to server.')


# @client.command()
# async def test(ctx):
#     await ctx.send(f'.help')

# @client.command()
# async def intro(ctx):
#     await ctx.send(f'hi im big idiot')

# client.run(os.getenv('TOKEN'))

