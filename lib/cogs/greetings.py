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
        print(f'db: adding user {member.id} to database...')
        db.commit()
        await self.client.get_channel(884116429421559859).send(f'welcome to **{member.guild.name}** {member.mention}')      # welcome-spam channel id
        try:
            await member.send(f'welcome to **{member.guild.name}**\n\tplease stop by <#884116429421559859> and check pins') # sends dm with welcome-spam channel id
        except Forbidden:
            pass
        await member.add_roles(*(member.guild.get_role(id_) for id_ in (884515444688584734, 884515686804774953)))       # default-role ids


    @Cog.listener()
    async def on_member_remove(self, member):
        db.execute("DELETE FROM exp WHERE UserID = ?", member.id)
        print(f'db: removing user {member.id} from database...')
        db.commit()
        await self.client.get_channel(884116429421559859).send(f'```{member.display_name} has left {member.guild.name}... shame on them```')      # welcome-spam channel id



def setup(client):
    pass
    client.add_cog(greetings(client))