from discord.ext.commands import Cog, command
from datetime import datetime, timedelta
from random import randint
from typing import Optional
from discord import Member
from ..db import db
import re

class exp(Cog):
    def __init__(self, client):
        self.client = client
        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    async def process_xp(self, message):
        xp, lvl, xplock = db.record("SELECT XP, Level, XPLock FROM exp WHERE UserID = ?", message.author.id)
        if datetime.utcnow() > datetime.fromisoformat(xplock):
            await self.add_xp(message, xp, lvl)

        if not message.author.bot:
            message_cont = re.sub(self.url_regex, '[link]', str(message.content), flags=re.MULTILINE)
            print(f'\nNEW MESSAGE: [ @{message.author.display_name} in #{message.channel.name} ] | lvl = {lvl} xp = {xp} | LOCK EXPIRES: {str(xplock)[11:]}\n')
            print(f'"{message_cont}"\n\n\n')
            # db.commit()

    async def add_xp(self, message, xp, lvl):
        xp_add = randint(4, 20)
        new_lvl = int(((xp+xp_add)//69)** 0.45)

        db.execute("UPDATE exp SET XP = XP + ?, Level = ?, XPLock = ?, UserName = ? WHERE UserID = ?", 
                    xp_add, new_lvl, (datetime.utcnow()+timedelta(seconds=60)).isoformat(sep=' ', timespec='seconds'), message.author.display_name, message.author.id)
        print(f'''
                    {int(((2000000)//69)** 0.45) }
                    
        
        ''')
        if new_lvl > lvl:
                print(f'+{xp_add}xp to user {message.author.display_name}: [ lvl {new_lvl} ] LEVEL UP!\n')
                await self.logs_channel.send(f'```congrats {message.author.display_name} \n\nnew level: [ {new_lvl:,} ]```')
        else:
            if not message.author.bot: 
                print(f'+{xp_add}xp to user {message.author.display_name}: [ lvl {new_lvl} ]')
                # pass
        db.commit()
        

    # @command(name = 'check_level', aliases=['lvl'])
    # async def  check_level(self, ctx, member: Optional[Member]):
    #     member = member or ctx.author
    #     xp, lvl = db.record("SELECT XP, Level FROM exp WHERE UserID = ?", member.id)
    #     await ctx.send(f'{member.display_name} is level {lvl} with {xp}xp')

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
        # names = db.records("SELECT UserName FROM exp ORDER BY XP DESC")
        record = ([record[0] for record in records[0:9]])
        # name = ([name[0] for name in names])
        x = 0
        for record in records:
            x = x + 1
            if str(record)[2].startswith('?'):
                pass
            else:
                await ctx.send(f"```{x}. {str(record)[2:-3]} has {str(db.records('SELECT XP FROM exp WHERE UserName = ?', str(record)[2:-3]))[2:-3]}xp ```")

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.logs_channel = self.client.get_channel(884548573730074624)
            self.client.cogs_ready.ready_up('exp')

    @Cog.listener()
    async def on_message(self, message):
        # if not message.author.bot:
        await self.process_xp(message)


# end ---
def setup(client):
    client.add_cog(exp(client))