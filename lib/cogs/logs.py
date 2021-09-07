from discord import Forbidden, Embed
from datetime import datetime
from discord.ext.commands import Cog



class logs(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.log_channel = self.client.get_channel(884548573730074624)
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

    @Cog.listener()
    async def on_message_edit(self, before, after):
        pass

        if not after.author.client:
            pass

    @Cog.listener()
    async def on_message_delete(self, before, after):
        pass
        if not after.author.client:

            pass


# end ---
def setup(client):
    client.add_cog(logs(client))
