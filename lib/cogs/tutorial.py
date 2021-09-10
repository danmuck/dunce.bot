# discord.py ---
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown

# random ---
import random
from random import choice, randint, random
from typing import Optional
# aiohttp ---
from aiohttp import request

from discord.ext.commands.errors import BadArgument


class tutorial(Cog):

    # cog initialization ---
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('tutorial')

#        await self.client.stdout.send(f'cogs: tutorial cog ready')                  # spam to channel on ready

# commands ---
    @command(name="hello", aliases=["hi"])
    async def say_hello(self, ctx):
        await ctx.send(f"```{choice(('hello','hi','hey','hiya'))}``` {ctx.author.mention}")

    # roll [x]d[y] where x = how many die and y = sides per die
    @command(name="dice", aliases=["roll"])
    # can use [1] time every [60] seconds if you are [any user]
    @cooldown(1, 60, BucketType.user)
    async def roll_dice(self, ctx, die_string: str):
        dice, value = (int(term) for term in die_string.split('d'))

        if dice <= 35:
            rolls = [randint(1, value) for i in range(dice)]

            # BUG: make it return in codeblock
            await ctx.send((f"```{f' + '.join([str(r) for r in rolls]) + f' = {sum(rolls)}'}```"))

        else:
            await ctx.send(f'```too many dice for my lil hands```')

    # slap a homie

    @command(name='slap', aliases=['hit'])
    async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = 'bein a dick'):
        await ctx.send(f'{ctx.author.display_name} slapped {member.mention} for {reason}!')

    @slap_member.error
    async def slap_member_error(self, ctx, exc):
        if isinstance(exc, BadArgument):
            await ctx.send(f'```cant find that homie```')


    # send client message
    @command(name='echo', aliases=['say'])
    # can use [1] time per [15] seconds if you are [server member]
    @cooldown(1, 15, BucketType.guild)
    async def echo_message(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    # animal facts
    @command(name='fact')
    # @cooldown(3, 60, BucketType.guild)                  # can use [3] times per [60] seconds if you are [server member]
    async def animal_fact(self, ctx, animal: str):
        if animal.lower() in ('dog', 'cat', 'panda', 'koala', 'fox', 'bird', 'red panda', 'raccoon', 'kangaroo'):
            URL = f'https://some-random-api.ml/animal/{animal.lower()}'

            async with request('GET', URL, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    # await ctx.send(data['fact'])          # send fact (in embed below)

                    embed = Embed(title=f'{animal.title()} fact',
                                            description=data['fact'],
                                            colour=ctx.author.colour)
                    embed.set_image(url=data['image'])
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f'```api returned a {response.status} status```')

        else:
            await ctx.send(f'```no facts for that animal```')
# MOVE THESE ---
    @command(name='8ball', aliases=["fortune"])
    async def ball8(self, ctx, *, question=f'am i a fortunate son?\n(type a question after the command)'):
        responses = ['hell nahh',
                    'sure dude',
                    'seems sufficient',
                    'right...',
                    'yeah',
                    'nope',
                    'absolutely bro',
                    'too late']
        await ctx.send(f'```question: {question}\nanswer: {choice(responses)} \n```')

    @command(name = "jeb8ball", aliases=["jeb8" , "misfortune"])
    async def  jeb8ball(self, ctx, *, question='did i wish for misfortune?\n(type a question after the command)'):
        responses = ['hell nahh', 'nope', 'no', 
                    'not a chance', 'no way', 'for sure... not', 
                    'definitely not', 'hard pass', 'ha no', 
                    'probs not', 'maybe next time', 'fuck yes', 
                    'please no', 'give it up', 'noooooooo',
                    'not so much', 'move on', 'trust me, no',
                    'cant say yes to that', 'nein', 'no sir',
                    'no ma\'am', 'leave it', 'NO', 'nah b']
        await ctx.send(f"```question: {question}\nanswer: {choice(responses)} \n```")

    @command(name = "g8ball", aliases=["g8" , 'rg8' , 'gr8'])
    async def  g8ball(self, ctx, *, question='pick a random logic gate for joe'):
        responses = ['and', 'or', 'not', 'nand', 'nor', 'xor', 'xnor']
        await ctx.send(f"```question: {question}\nanswer: {choice(responses)} \n```")

    @command(name = "booleanDecider", aliases=["ran" , 'tf' , 'coin' , 'flip' , 'bd'])
    async def  booleanDecider(self, ctx):
        await ctx.send(f"```fine, i pick: {choice(['true','false'])}```")

    @command()
    async def cb(self, ctx, *, message):
        await ctx.send(f'``` {message} \n\n```')


# run cog ---
def setup(client):
    client.add_cog(tutorial(client))
