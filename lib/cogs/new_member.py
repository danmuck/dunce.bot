from discord import Forbidden
from discord.ext.commands import Cog
from ..db import db


class new_member(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('new_member')

    @Cog.listener()
    async def on_member_join(self, member):
        print(f'\n\talert: {member} has entered the chat\n')
        db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
        print(f'db: adding user {member}|{member.id} to database...')
        db.commit()
        # welcome-spam channel id
        await self.client.get_channel(884853014228267038).send(f'welcome to **{member.guild.name}** {str(member)[-5]}')
        try:
            # sends dm with welcome-spam channel id
            await member.send(f'welcome to **{member.guild.name}**\n\tplease stop by <#878370102549041212> and check pins')
        except Forbidden:
            pass
        # default-role ids [outsider]
        await member.add_roles(*(member.guild.get_role(id_) for id_ in (884533782051426304, 884860921829281913)))

    @Cog.listener()
    async def on_member_remove(self, member):
        print(f'\n\talert: {member} has left the chat\n')
        db.execute("DELETE FROM exp WHERE UserID = ?", member.id)
        print(f'db: removing user {member.display_name}|{member.id} from database...')
        db.commit()
        # welcome-spam channel id
        await self.client.get_channel(884853014228267038).send(f'```{member.display_name} has left {member.guild.name}... shame on them```')


def setup(client):
    pass
    client.add_cog(new_member(client))
