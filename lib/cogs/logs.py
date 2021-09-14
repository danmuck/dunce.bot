from discord import Forbidden, Embed
from datetime import datetime
from discord.ext.commands import Cog
import logging


class logs(Cog):
    def __init__(self, client):
        self.client = client
        
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='./data/discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    def log_embed(self, title, description, color, thumbnail=None, fields=None):
        embed = Embed(title=title,
                        description=description,
                        color=color,
                        timestamp=datetime.utcnow())
        embed.set_thumbnail(url=thumbnail or self.bot.guild.me.avatar_url)
        if fields is not None:
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
        return embed

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.log_channel = self.client.get_channel(884548573730074624)      # BUG: get from database
            self.client.cogs_ready.ready_up('logs')

    @Cog.listener()
    async def on_user_update(self, before, after):
        if before.name != after.name:
            embed = Embed(title='user update', description='[username change]', colour=self.log_channel.guild.get_member(
                after.id).colour, timestamp=datetime.utcnow())

            fields = [('before:', before.name, False),
                    ('after:', after.name, False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.log_channel.send(embed=embed)

        if before.discriminator != after.discriminator:
            embed = Embed(title='user update', description='[discriminator change]', colour=self.log_channel.guild.get_member(
                after.id).colour, timestamp=datetime.utcnow())

            fields = [('before:', before.discriminator, False),
                    ('after:', after.discriminator, False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.log_channel.send(embed=embed)

        if before.avatar_url != after.avatar_url:
            embed = Embed(title='user update', description='[new profile picture]', colour=self.log_channel.guild.get_member(
                after.id).colour, timestamp=datetime.utcnow())
            embed.set_thumbnail(url=before.avatar_url)
            embed.set_image(url=after.avatar_url)
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.log_channel.send(embed=embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = Embed(title='member update',
                        description='[nickname change]', colour=after.colour, timestamp=datetime.utcnow())
            fields = [('before:', before.display_name, False),
                    ('after:', after.display_name, False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.log_channel.send(embed=embed)

        elif before.roles != after.roles:
            embed = Embed(title='member update',
                        description='[role update]', colour=after.colour, timestamp=datetime.utcnow())
            fields = [('before:', ', '.join([r.mention for r in before.roles]), False),
                    ('after:', ', '.join([r.mention for r in after.roles]), False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.log_channel.send(embed=embed)

    # @Cog.listener()
    # async def on_message_edit(self, before, after):
    #     if not after.author.client:
    #         if before.content != after.content:
    #             await self.log_channel.send(f'```edit: {before.content} === {after.content}```')

    # @Cog.listener()
    # async def on_message_delete(self, message):
    #     if message.author != self.client:
    #         await self.log_channel.send(f'```edit: {message.author} delete test```')

    @Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content: 
                embed = Embed(title="edit: message",
							description=f"by: {after.author.display_name}",
							colour=after.author.colour,
							timestamp=datetime.utcnow())
                fields = [("original:", before.content, False),
						("update:", after.content, False)]
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                await self.log_channel.send(embed=embed)

    @Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            embed = Embed(title="edit: message removed", 
                        description=f"by: {message.author.display_name}",
                        colour=message.author.colour,
                        timestamp=datetime.utcnow())
            fields = [("content", message.content, False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.log_channel.send(embed=embed)


# end ---
def setup(client):
    client.add_cog(logs(client))
