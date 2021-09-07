import discord, random, os
# discord.py imports
from discord import Intents, Embed, File
from discord.errors import HTTPException, Forbidden
from discord.ext import tasks
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import (CommandNotFound, Context, BadArgument, MissingRequiredArgument, CommandOnCooldown, when_mentioned_or)

# global imports ?
from datetime import datetime
from glob import glob

# asynchio imports
from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext.commands.errors import BadArgument, MissingPermissions
from itertools import cycle

# database import
from ..db import db

# logging

import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#PREFIX = '?'
OWNER_IDS = [876630793974345740]    # i am owner
COGS = [path.split('/')[-1][:-3] for path in glob('lib/cogs/*.py')]       # go through /cogs directory and return the name of any cogs -.py as array (split rules for removing it)
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument, MissingPermissions)
STATUS = (['god' , 'trapqueen' , 'buddha' , 'zeus' , 'qanon chatroom' , 'doja cat' , 'creator' , 'yourself' , 'pretend' , 'bush did 9/11 sim'])

class ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f'cogs: {cog} cog is ready')

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

# get prefix ---
def get_prefix(client, message):
    prefix = db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", message.guild.id)
    if prefix == None:
        print(f'db: guild added to database: command prefix set to default: ?')
        db.execute('INSERT INTO guilds (GuildID, Prefix) VALUES (?, "?")', message.guild.id)
        db.commit()
        prefix = db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", message.guild.id)
        return when_mentioned_or(prefix)(client, message)                   # set up multiserver bot
    else:
        return when_mentioned_or(prefix)(client, message)           

class Bot(BotBase):
# client initialization ---
    def __init__(self):
        self.PREFIX = get_prefix
        self.ready = False
        self.cogs_ready = ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        # intents = Intents.default()                               # this is more customizable (i think?)
        # intents.members = True                                    # can use this instead of ACTIVATE INTENTS (to avoid presences?)

        db.autosave(self.scheduler)                                 # set database to autosave on init
        super().__init__(
            command_prefix=get_prefix, 
            owner_ids=OWNER_IDS,
            intents=Intents.all(),                                  # ACTIVATE INTENTS
            )

# load cogs ---
    def setup(self):                                                
        for cog in COGS:                                            # note: [cog] set as cursor (constant)
            self.load_extension(f"lib.cogs.{cog}")      
            print(f'cogs: {cog} cog loading')     
        
        print(f'\n\tcogs: loading complete')                              # console: cogs loaded / complete status


# run client with token ---        
    def run(self, version):                                         
        self.VERSION = version

        print(f'*** dunce.bot ***\n** by: danmuck **\n\ndunce: starting my initial setup...\n')                                  # console: client setting up
        self.setup()
        
        with open('./lib/client/token.0', 'r', encoding='utf-8') as tf:
            self.TOKEN = tf.read()

        print('\n\ndunce: hello friend :)\ndunce: checking my token...')
        super().run(self.TOKEN, reconnect=True)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=Context)

        if ctx.command is not None and ctx.guild is not None:
            if self.ready:
                await self.invoke(ctx)

            else:
                await ctx.send(f'```dunce.bot is taking a break```')
# connect/disconnect messages ---
    async def on_connect(self):                                     
        print('\ndunce: big idiot is sentient\n\n')

    async def on_disconnect(self):
        print('\n\tdunce.bot is in the corner\n\n\n')
# timed reminders ---
    async def rules_reminder(self):
        channel = self.get_channel(884853014228267038)              # welcome-spam channel id
        await channel.send(f'```timed notification: rules reminder [weekly] UPDATE ME```')


# error handling ---

    async def on_error(self, err, *args, **kwargs):
        if err == 'on_command_error':
            await args[0].send(f'```on_command_error: check console```')          # if error is a command error send message

        channel = self.get_channel(881174439880958003)              # send an error message to error-spam channel id
        await channel.send('```on_error: check console```')
        raise                                                       # raise error to the console

    async def on_command_error(self, ctx, exc):
        if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):          # if our exception == CommandNotFound
            print(f'error: {ctx} command not found')
            pass    

        elif isinstance(exc, MissingPermissions):
            pass

        elif isinstance(exc, BadArgument):
            pass

        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send(f'```error: missing arguments```')

        elif isinstance(exc, CommandOnCooldown):
            await ctx.send(f'```error: {str(exc.cooldown.type).split(".")[-1]} cooldown [try again in {exc.retry_after:,.2f} sec]```')    # {exc.retry_after://60+1,.2f} return minutes (un-comfirmed)

        elif hasattr(exc, 'original'):
            if isinstance(exc.original, HTTPException):
                await ctx.send(f'```error: unable to send message```')

            elif isinstance(exc.original, Forbidden):

                await ctx.send(f'```error: im not allowed```')
            else:
                raise exc.original
        
        else:
            raise exc

# on_ready notifiers ---
    async def on_ready(self):           
        if not self.ready:
            await client.change_presence(status=discord.Status.idle, activity=discord.Game('YOURSELF'))
            self.guild = self.get_guild(878370102091853824)         # server id
            self.stdout = self.get_channel(881226606490841088)      # spam channel id for [standard out] channel
    # scheduled tasks on_ready ---
            change_status.start()
            print(f'tasks: change_status starting...')
            clear_test.start()
            print(f'tasks: clear_test starting...')
            self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12))          # rules_reminder timed reminder start
            print(f'tasks: rules_reminder starting...')             # console: starting task
            self.scheduler.start()
            
            while not self.cogs_ready.all_ready():
                await sleep(0.5)                                     # sleep is for incase cog takes too long to load

#            channel = self.get_channel(884116429421559859)          # welcome-spam channel id
#            await channel.send(f'dunce.bot is now : online')               # send login message
            self.ready = True
            print('dunce: im ready\n')                                # console: client is ready message
    
        else:
            print('dunce: reconnected\n')                             # console: client reconnected
# tasks ---
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(random.choice(STATUS)))
@tasks.loop(minutes=15)
async def clear_test():
    await client.get_channel(883778568004456458).purge(limit=250) #text channel id
    await client.get_channel(883778568004456458).send(f'its my spam, i do what i want with it') 

# end ---
# on_message response ---
    async def on_message(self, message):
        # if message.author.client and message.author != message.guild.me: # same thing but can take commands from other bots (NOT WORKING)
        #     await self.process_commands(message)
        if not message.author.bot:                                      # ignore messages from the bot itself only
            await self.process_commands(message)
client = Bot()












# login message custom embed template ---
        #    embed = Embed(title='now online', 
        #                    description='dunce.bot is now online', 
        #                    colour=0xff0000,
        #                    timestamp=datetime.utcnow())            
        #    fields = [('name', 'value', True),
        #                ('another name field', 'another value field', True),
        #                ('third name non-inline', 'third value non-inline', False)]
        #    for name, value, inline in fields:                                              # assign the value translation of fields
        #        embed.add_field(name=name, value=value, inline=inline)
        #    embed.set_author(name='server/organization [author]', icon_url=self.guild.icon_url)                  # footer icon
        #    embed.set_footer(text='this footer here')                                       # footer text 
        #    embed.set_thumbnail(url=self.guild.icon_url)                                    # :/https links or this to set thumbnail (small image in embed)
        #    embed.set_image(url=self.guild.icon_url)                                        # ://https links or this to set (big image in embed)
        #    await channel.send(embed=embed)                         # ON READY SEND EMBED TO CHANNEL

        #    await channel.send(file=File('./data/images/ex_logo.jpg'))                      # send a file 

