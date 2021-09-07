from discord import Forbidden
from discord.ext.commands import Cog
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
        # welcome-spam channel id
        await self.client.get_channel(884853014228267038).send(f'welcome to **{member.guild.name}** {member}')
        try:
            # sends dm with welcome-spam channel id
            await member.send(f'welcome to **{member.guild.name}**\n\tplease stop by <#878370102549041212> and check pins')
        except Forbidden:
            pass
        # default-role ids [outsider]
        await member.add_roles(*(member.guild.get_role(id_) for id_ in (884533782051426304, 884860921829281913)))

    @Cog.listener()
    async def on_member_remove(self, member):
        db.execute("DELETE FROM exp WHERE UserID = ?", member.id)
        print(f'db: removing user {member.id} from database...')
        db.commit()
        # welcome-spam channel id
        await self.client.get_channel(884853014228267038).send(f'```{member.display_name} has left {member.guild.name}... shame on them```')


def setup(client):
    pass
    client.add_cog(greetings(client))
