from discord.ext.commands import Cog, CheckFailure, command, has_permissions
from datetime import datetime, timedelta
from random import randint
from ..db import db


class exp(Cog):
    def __init__(self, client):
        self.client = client

    async def process_xp(self, message):
        xp, lvl, xplock = db.record("SELECT XP, Level, XPLock FROM exp WHERE UserID = ?", message.author.id)
        print(xp, lvl, xplock)

        if datetime.utcnow() > datetime.fromisoformat(xplock):
            await self.add_xp(message, xp, lvl)

    async def add_xp(self, message, xp, lvl):
        xp_add = randint(4, 20)
        new_lvl = int(((xp+xp_add)//42)** 0.55)
        print(f'{xp_add=} {new_lvl=}')

        db.execute("UPDATE exp SET XP = XP + ?, Level = ?, XPLock = ? WHERE UserID = ?", 
                            xp_add, new_lvl, (datetime.utcnow()+timedelta(seconds=45)).isoformat(), message.author.id)

        if new_lvl > lvl:
                await message.channel.send(f'congrats: {message.author.display_name} level up to {new_lvl:,}')

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('exp')

    @Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_xp(message)


# end ---
def setup(client):
    client.add_cog(exp(client))