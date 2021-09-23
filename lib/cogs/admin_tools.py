import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands.core import has_permissions, has_role, bot_has_permissions
import re, os
from re import search
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

class admin_tools(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('admin_tools')

    @command(name="yeeter", aliases=["ytr"], hidden=True)
    @has_role(881287992382197850)  # admin role id
    async def yeeter(self, ctx):
        await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)
        # await ctx.channel.purge(limit=amount)

    @command(hidden=True)
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)

    @command(hidden=True)
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    @has_role((int(os.getenv('ADMIN_ROLE'))) or (int(os.getenv('MOD_ROLE'))))
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @command(hidden=True)
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    @has_role((int(os.getenv('ADMIN_ROLE'))) or (int(os.getenv('MOD_ROLE'))))
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

# end ---
def setup(client):
    client.add_cog(admin_tools(client))
