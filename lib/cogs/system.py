from ..db import db
from discord.ext.commands import command, has_permissions, when_mentioned_or
from discord.ext.commands import Cog, CheckFailure
from discord.utils import get
from discord import Embed
from dotenv import load_dotenv
load_dotenv()
import re
from re import search



class system(Cog):
    def __init__(self, client):
        self.client = client
        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    # command prefix ---
    @command(name='prefix', hidden=True)
    @has_permissions(manage_guild=True)
    async def change_prefix(self, ctx, new: str):
        if len(new) > 1:
            await ctx.send(f'```pick one character please```')
        else:
            db.execute(
                "UPDATE guilds SET Prefix = ? WHERE GuildID = ?", new, ctx.guild.id)
            db.commit()
            await ctx.send(f'```prefix set to: {new}``` <@876630793974345740> ')

    @change_prefix.error
    async def change_prefix_error(sef, ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send(f'```error: user role cannot manage_guild```')

    @command(name='dunce_ping', aliases=["png", 'ping'], hidden=True)
    async def dunce_ping(self, ctx):
        await ctx.send(f"{round(self.client.latency * 1000)}ms")
    
    @command(name = 'ddf87hf73', aliases=['?????????????????????????????'], hidden=True)

    async def ddf87hf73(self, ctx):
        await ctx.send(f'``` hey! {ctx.message.author.display_name} fuck you lol :) ```')


    # def get_roleT(client, message):
    #     roleT = db.field(
    #         "SELECT RoleID FROM roles WHERE GuildName = ?", str(message.guild.name))
    #     if roleT == None:
    #         print(f'db: roles added to database...')
    #         db.execute(
    #             'INSERT INTO roles (RoleID, GuildName) VALUES (?, ?)', client.guild.roles, str(message.guild.name))
    #         db.commit()
    #         roleT = db.field(
    #             "SELECT RoleID FROM guilds WHERE GuildName = ?", client.guild.roles, str(message.guild.name))
    #         # set up for multiserver bot
    #         return when_mentioned_or(roleT)(client, message)
    #     else:
    #         return when_mentioned_or(roleT)(client, message)

# end ---
    @Cog.listener()
    async def on_message(self, message):
        if search(self.url_regex, message.content) and not message.author.bot:
            url = re.findall(self.url_regex, str(message.content))
            actual_url = ([actual_url[0] for actual_url in url])
            for urls in actual_url:
                print(f'\nNEWS: {urls} in #{message.channel}')
    
                embed = Embed(title=f'{urls}',
                                url=f'{urls}',
                                description=f'[ new post by {message.author.display_name} in <#{message.channel.id}> ]',
                                color=0x000)
                embed.set_author(name='dunce.news', url='https://github.com/danmuck/dunce.bot')
                await self.news_channel.send(embed=embed)
                await self.logs_channel.send(f'``` #{message.channel}: [ {urls} ] ```')
                # await self.news_channel.send(f'[ {message.author.display_name} posted {f"{urls}"} in <#{message.channel.id}> ]')

                db.execute("INSERT OR IGNORE INTO links (ChannelID, Link, Category, OrigMessage) VALUES (?, ?, ?, ?)", message.channel.id, (urls), message.channel.name, str(message.content))

                db.commit()
    
    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.logs_channel = self.client.get_channel(884851550206435410)
            self.news_channel = self.client.get_channel(881174749877776394)
            self.client.cogs_ready.ready_up('system')

            # these lines need work
            # roles = str(self.client.guild.roles)
            # db.execute("INSERT INTO roles (Roles, GuildID) VALUES (?, ?)", roles, self.client.guild.id) # this needs to pull the ids from the roles list only
            # db.commit()

        




def setup(client):
    client.add_cog(system(client))
