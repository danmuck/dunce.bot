import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands.core import has_permissions, has_role



class admin_commands(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('admin_commands')

    @command(name="yeeter", aliases=["ytr"])
    @has_role(881287992382197850)  # admin role id
    async def yeeter(self, ctx, amount=250):
        await ctx.channel.purge(limit=amount)

    @command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
# end ---


def setup(client):
    client.add_cog(admin_commands(client))
