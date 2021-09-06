# discord.py ---
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType, CheckFailure
from discord.ext.commands import command, cooldown, has_permissions
from discord.utils import get

# random ---
from random import choice, randint
from typing import Optional
# aiohttp ---
from aiohttp import request
# database ---
from ..db import db

class system(Cog):
    def __init__(self, client):
        self.client = client 

# command prefix ---
    @command(name='prefix')
    @has_permissions(manage_guild=True)
    async def change_prefix(self, ctx, new: str):
        if len(new) > 1:
            await ctx.send(f'pick one character please')
        else:
            db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", new, ctx.guild.id)
            await ctx.send(f'```prefix set to: {new}``` <@876630793974345740> ')

    @change_prefix.error
    async def change_prefix_error(sef, ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send(f'error: user role cannot manage_guild')

# end ---
    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('system')
def setup(client):
    client.add_cog(system(client))