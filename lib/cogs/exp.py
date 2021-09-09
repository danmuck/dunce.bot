from discord.ext.commands import Cog, CheckFailure, command, has_permissions
from datetime import datetime, timedelta
from random import randint
from ..db import db


class exp(Cog):
    def __init__(self, client):
        self.client = client

    async def process_xp(self, message):
        xp, lvl, xplock = db.record("SELECT XP, Level, XPLock FROM exp WHERE UserID = ?", message.author.id)
        print(f'\nNEW MESSAGE: [ @{message.author.display_name} in #{message.channel.name} ] | lvl = {lvl} xp = {xp} | LOCK EXPIRES = {xplock}\n')
        print(f'"{str(message.content)}"\n')

        if datetime.utcnow() > datetime.fromisoformat(xplock):
            await self.add_xp(message, xp, lvl)

    async def add_xp(self, message, xp, lvl):
        xp_add = randint(4, 20)
        new_lvl = int(((xp+xp_add)//42)** 0.55)
        print(f'+{xp_add}xp to user {message.author.display_name}: new level is {new_lvl}\n')

        db.execute("UPDATE exp SET XP = XP + ?, Level = ?, XPLock = ? WHERE UserID = ?", 
                    xp_add, new_lvl, (datetime.utcnow()+timedelta(seconds=60)).isoformat(sep=' ', timespec='seconds'), message.author.id)

        if new_lvl > lvl:
                await self.logs_channel.send(f'```congrats {message.author.display_name} \nnew level = {new_lvl:,}```')

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.logs_channel = self.client.get_channel(884851550206435410)
            self.client.cogs_ready.ready_up('exp')

    @Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_xp(message)


# end ---
def setup(client):
    client.add_cog(exp(client))