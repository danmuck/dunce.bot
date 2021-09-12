from discord.channel import CategoryChannel
from discord.ext.commands import Cog
from discord.ext.commands import command
from typing import Optional
from discord import Member, Embed
from datetime import datetime
from ..db import db
class info(Cog):
    def __init__(self, client):
        self.client = client
#BUG: needs formatting
    @command(name='userinfo', aliases=['memberinfo', 'ui'])
    async def user_info(self, ctx, target: Optional[Member]):
        target = target or ctx.author
        embed = Embed(title='user info', colour=target.colour, timestamp=datetime.utcnow())
        fields = [      ('` name `', str(target), False),
                        ('` id `', target.id, False),
                        ('`  is bot?  `', target.bot, True),
                        ('`  top role  `', target.top_role.mention, True),
                        ('`  status  `', str(target.status).title(), True),
                        ('` activity: `', f'{str(target.activity.type).split(".")[-1].title() if target.activity else "N/A"} {target.activity.name if target.activity else ""}', True),
                        ('` created on `', target.created_at.strftime('%m/%d/%Y %H:%M'), False),
                        ('` joined server `', target.joined_at.strftime('%H:%M:%S\n %m/%d/%Y '), True),
                        ]   # ('`boosted`', bool(target.premium_since), True)
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        # embed.set_thumbnail(url=ctx.avatar_url)
        await ctx.send(embed=embed)
        # response = ctx.send(f'{ctx}')

    @command(name = 'serverinfo', aliases=['guildinfo', 'si', 'gi'])
    async def  server_info(self, ctx):
        embed = Embed(title='server info', colour=ctx.guild.owner.colour, timestamp=datetime.utcnow())
        fields = [      ('` name `', str(ctx.guild.name), False),
                        ('` id `', ctx.guild.id, True),
                        ('`  owner  `', ctx.guild.owner, True),
                        ('`  created at  `', ctx.guild.created_at.strftime('%m/%d/%Y %H:%M'), True),
                        ('`  members  `', len(ctx.guild.members), True),
                        ('` humans `', len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                        ('` bots `', len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                        ('` banned members `', len(await ctx.guild.bans()), True),
                        ('` roles `', len(ctx.guild.roles), True),
                        ('` invites `', len(await ctx.guild.invites()), True),
                        ('` text channels `', len(ctx.guild.text_channels), True),
                        ('` voice channels `', len(ctx.guild.voice_channels), True),
                        ('` categories `', len(ctx.guild.categories), True),
                        ('\u200b', '\u200b', True)]  
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        # embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('info')

    


# end ---
def setup(client):
    client.add_cog(info(client))