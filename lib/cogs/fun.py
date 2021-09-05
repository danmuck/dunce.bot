import discord, random
# discord.py ---
from discord import Member
from discord.ext import commands
from discord.errors import HTTPException
from discord.ext.commands import Cog 
from discord.ext.commands import command
# random ---
from random import choice, randint
from typing import Optional

from discord.ext.commands.errors import BadArgument
# define cog object ---
class fun(Cog):

# cog initialization ---
    def __init__(self, bot):
        self.bot = bot 

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up('fun')

#        await self.bot.stdout.send(f'cogs: fun cog ready')                  # spam to channel on ready

# commands ---
    @command(name = "hello", aliases=["hi"])
    async def  say_hello(self, ctx):
        await ctx.send(f"{choice(('hello','hi','hey','hiya'))} {ctx.author.mention}")

    # roll [x]d[y] where x = how many die and y = sides per die
    @command(name = "dice", aliases=["roll"])
    async def  roll_dice(self, ctx, die_string: str):
        dice, value = (int(term) for term in die_string.split('d'))

        if dice <= 35:
            rolls = [randint(1, value) for i in range(dice)]

            await ctx.send(f' + '.join([str(r) for r in rolls]) + f' = {sum(rolls)}')

        else:
            await ctx.send(f'too many dice for my lil hands')


    # slap a homie
    @command(name = 'slap', aliases=['hit'])
    async def  slap_member(self, ctx, member: Member, *, reason: Optional[str] = 'no reason'):
        await ctx.send(f'{ctx.author.display_name} slapped {member.mention} for {reason}!')

    @slap_member.error
    async def slap_member_error(self, ctx, exc):
        if isinstance(exc, BadArgument):
            await ctx.send(f'cant find that homie')

    # send bot message
    @command(name = 'echo', aliases=['say'])
    async def  echo_message(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)



# MOVE THESE ---
    @command(name = "yeeter", aliases=["ytr"])
    async def  yeeter(self, ctx, amount=250):
        await ctx.channel.purge(limit=amount)


# cog setup ---
def setup(bot):
    bot.add_cog(fun(bot))