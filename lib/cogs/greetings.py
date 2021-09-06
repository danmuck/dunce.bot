from discord import Forbidden
from discord.ext.commands import Cog, command
from ..db import db 

class greetings(Cog):
    def __init__(self, client):
        self.client = client



    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('greetings')

    @Cog.listener()
    async def on_member_join(self, member):
        db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
        await self.client.get_channel(884116429421559859).send(f'welcome to **{member.guild.name}** {member.mention}')
        try:
            await member.send(f'welcome to **{member.guild.name}**\n\tplease stop by welcome and check pins') # sends dm
            # await member.add_roles(884514547891834901)    # adds role by id
            # await member.edit(roles=[*member.roles, *[member.guild.get_role(id_) for id_ in (884515444688584734, 884515686804774953)]])   # another way to do it [faster but funky to read?]
        except Forbidden:
            pass
        await member.add_roles(*(member.guild.get_role(id_) for id_ in (884515444688584734, 884515686804774953)))


    @Cog.listener()
    async def on_member_leave(self, member):
        pass


def setup(client):
    pass
    client.add_cog(greetings(client))