# discord.py imports
from discord import Intents, Embed, File
from discord.errors import HTTPException, Forbidden
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import (CommandNotFound, Context, BadArgument, MissingRequiredArgument)

# global imports ?
from datetime import datetime
from glob import glob

# asynchio imports
from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext.commands.errors import BadArgument

# database import
from ..db import db

PREFIX = '?'
OWNER_IDS = [876630793974345740]
COGS = [path.split('/')[-1][:-3] for path in glob('lib/cogs/*.py')]       # go through /cogs directory and return the name of any cogs -.py as array (split rules for removing it)
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)

class ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f'cogs: {cog} cog is ready')

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
# client initialization ---
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        # intents = Intents.default()                               # this is more customizable (i think?)
        # intents.members = True                                    # can use this instead of ACTIVATE INTENTS (to avoid presences?)

        db.autosave(self.scheduler)                                 # set db to autosave on init
        super().__init__(
            command_prefix=PREFIX, 
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
                await ctx.send(f'dunce.bot is taking a break')


# timed reminders ---
    async def rules_reminder(self):
        channel = self.get_channel(884116429421559859)              # welcome-spam channel id
        await channel.send(f'timed notification: rules reminder [weekly]')

# connect/disconnect messages ---
    async def on_connect(self):                                     
        print('\ndunce: big idiot is sentient\n\n')

    async def on_disconnect(self):
        print('\n\tdunce.bot is in the corner\n\n\n')

# error handling ---

    async def on_error(self, err, *args, **kwargs):
        if err == 'on_command_error':
            await args[0].send(f'on_command_error: check console')          # if error is a command error send message

        channel = self.get_channel(884131996194967572)              # send an error message to error-spam channel id
        await channel.send('on_error: check console')
        raise                                                       # raise error to the console

    async def on_command_error(self, ctx, exc):
        if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):          # if our exception == CommandNotFound
            pass    
            print(f'error: {ctx} command not found')

        elif isinstance(exc, BadArgument):
            pass

        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send(f'error: missing arguments')

        elif isinstance(exc.original, HTTPException):
            await ctx.send(f'error: unable to send message')

        elif isinstance(exc.original, Forbidden):
            await ctx.send(f'error: im not allowed')

        elif hasattr(exc, 'original'):
            raise exc.original
        
        else:
            raise exc

# on_ready notifiers ---

    async def on_ready(self):           
        if not self.ready:
            self.guild = self.get_guild(882994482579140739)         # server id
            self.stdout = self.get_channel(882994482579140742)      # spam channel id for [standard out] channel
        # scheduled tasks on_ready ---
            self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12))          # rules_reminder timed reminder start
            print(f'dunce: rules_reminder starting...')             # console: starting task
            self.scheduler.start()



# login message custom embed ---
#            embed = Embed(title='now online', 
#                            description='dunce is now online', 
#                            colour=0xff0000,
#                            timestamp=datetime.utcnow())            # enable embeds (0x prefix selects datatype i think?)
#            fields = [('name', 'value', True),
#                        ('another name field', 'another value field', True),
#                        ('third name non-inline', 'third value non-inline', False)]
#            for name, value, inline in fields:                                              # assign the value translation of fields
#                embed.add_field(name=name, value=value, inline=inline)
#            embed.set_author(name='server/organization [author]', icon_url=self.guild.icon_url)                  # footer icon
#            embed.set_footer(text='this footer here')                                       # footer text 
#            embed.set_thumbnail(url=self.guild.icon_url)                                    # :/https links or this to set thumbnail (small image in embed)
#            embed.set_image(url=self.guild.icon_url)                                        # ://https links or this to set (big image in embed)
#            await channel.send(embed=embed)                         # ON READY SEND EMBED TO CHANNEL
#
#            await channel.send(file=File('./data/images/ex_logo.jpg'))                      # send a file 
#
            
            while not self.cogs_ready.all_ready():
                await sleep(0.5)                                     # sleep is for incase cog takes too long to load

#            channel = self.get_channel(884116429421559859)          # welcome-spam channel id
#            await channel.send(f'dunce.bot is now : online')               # send login message
            self.ready = True
            print('dunce: im ready\n')                                # console: client is ready message
    
        else:
            print('dunce: reconnected\n')                             # console: client reconnected

# on_message response ---
    async def on_message(self, message):
        # if message.author.client and message.author != message.guild.me: # same thing but can take commands from other bots (NOT WORKING)
        #     await self.process_commands(message)
        if not message.author.bot:                                      # ignore messages from the bot itself only
            await self.process_commands(message)
# end ---
client = Bot()
