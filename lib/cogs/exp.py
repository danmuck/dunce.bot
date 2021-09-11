from discord.ext.commands import Cog, CheckFailure, command, has_permissions
from datetime import datetime, timedelta
from random import randint
from typing import Optional
from discord import Member
from ..db import db


class exp(Cog):
    def __init__(self, client):
        self.client = client

    async def process_xp(self, message):
        xp, lvl, xplock = db.record("SELECT XP, Level, XPLock FROM exp WHERE UserID = ?", message.author.id)
        print(f'\n\n\nNEW MESSAGE: [ @{message.author.display_name} in #{message.channel.name} ] | lvl = {lvl} xp = {xp} | LOCK EXPIRES = {xplock}\n')
        print(f'"{str(message.content)}"\n')

        if datetime.utcnow() > datetime.fromisoformat(xplock):
            await self.add_xp(message, xp, lvl)
            

    async def add_xp(self, message, xp, lvl):
        xp_add = randint(4, 20)
        new_lvl = int(((xp+xp_add)//42)** 0.55)
        print(f'+{xp_add}xp to user {message.author.display_name}: new level is {new_lvl}\n')

        db.execute("UPDATE exp SET XP = XP + ?, Level = ?, XPLock = ?, UserName = ? WHERE UserID = ?", 
                    xp_add, new_lvl, (datetime.utcnow()+timedelta(seconds=60)).isoformat(sep=' ', timespec='seconds'), message.author.display_name, message.author.id)

        if new_lvl > lvl:
                await self.logs_channel.send(f'``` congrats {message.author.display_name} \nnew level = {new_lvl:,} ```')

    @command(name = 'check_level', aliases=['lvl'])
    async def  check_level(self, ctx, member: Optional[Member]):
        member = member or ctx.author
        xp, lvl = db.record("SELECT XP, Level FROM exp WHERE UserID = ?", member.id) or (None, None)
        if lvl is not None:
            await ctx.send(f'``` {member.display_name} is level {lvl} with {xp}xp ```')
        else:
            await ctx.send(f'``` prolly a bot ```')

    @command(name = 'check_rank', aliases=['rank'])
    async def  check_rank(self, ctx, member: Optional[Member]):
        member = member or ctx.author
        ids = db.column("SELECT UserID FROM exp ORDER BY XP DESC")
        try:
            await ctx.send(f'``` {member.display_name} is rank #{ids.index(member.id)+1} out of {len(ids)} users ```')
        except ValueError:
            await ctx.send(f'``` prolly a bot ```')
            
# leaderboard needs work but it is okay for now since no one will use it
    @command(name = 'leaderboard', aliases=['lb'])
    async def  leaderboard(self, ctx):
        records = db.records("SELECT UserName FROM exp ORDER BY XP DESC")
        record = ([record[0] for record in records])
        for record in records:
            if not None:
                await ctx.send(f"``` {str(record)[2:-3]} has {str(db.records('SELECT XP FROM exp WHERE UserName = ?', str(record)[2:-3]))[2:-3]}xp ```")

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