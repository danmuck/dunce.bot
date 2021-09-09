import discord
from discord.ext import commands
from discord.ext.commands import Cog, CheckFailure, Greedy
from discord.ext.commands import command
from discord.ext.commands.core import has_permissions, has_role, bot_has_permissions
import re
from re import search
from typing import Optional

from ..db import db
class admin_commands(Cog):
    def __init__(self, client):
        self.client = client
        # self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('admin_commands')

    @command(name="yeeter", aliases=["ytr"])
    @has_role(881287992382197850)  # admin role id
    async def yeeter(self, ctx):
        await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)
        # await ctx.channel.purge(limit=amount)

    @command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)

    @command()
    # @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @command()
    # @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
# end ---
    # @Cog.listener()
    # async def on_message(self, message):
    #     if search(self.url_regex, message.content):
    #         url = re.findall(self.url_regex, str(message.content))
    #         print(f'NEW LINKS: {[x[0] for x in url]} in #{message.channel}')

            
            # db.execute("UPDATE links SET Link = ?, ChannelID = ?, Category = ?", ((([x[0] for x in url]))), ((message.channel.id)), ((message.channel.name)))
            # db.commit()
            # print(f'TESTING!!! {([x[0] for x in url])}')

def setup(client):
    client.add_cog(admin_commands(client))



# s = '''http://www.santa.com'''
# match = re.search(r'href=[\'"]?([^\'" >]+)', s)
# if match:
#     print match.group(0)