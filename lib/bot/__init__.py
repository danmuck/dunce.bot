from discord import Intents, Embed, File
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

# database import
from ..db import db

PREFIX = '?'
OWNER_IDS = [876630793974345740]

class Bot(BotBase):
# bot initialization ---
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
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
        
    def run(self, version):
        self.VERSION = version
        
        with open('./lib/bot/token.0', 'r', encoding='utf-8') as tf:
            self.TOKEN = tf.read()

        print('dunce: hello friend :)\ndunce: running bot...')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('\n\tdunce: big idiot connected\n\n')

    async def on_disconnect(self):
        print('\n\tdunce: dunce is in the corner\n\n\n')

# error handling ---

    async def on_error(self, err, *args, **kwargs):
        if err == 'on_command_error':
            await args[0].send(f'on_error == on_command_error: check console')          # if error is a command error send message

        channel = self.get_channel(884131996194967572)              # send an error message to error-spam
        await channel.send('on_error: check console')

        raise                                                       # raise error to the command prompt

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):                        # if our exception == CommandNotFound
            pass    # await.ctx.send(f'command not found')          # can use this to notify (frowned upon)

        elif hasattr(exc, 'original'):
            raise exc.original
        
        else:
            raise exc

# on_ready notifiers ---

    async def on_ready(self):           
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(882994482579140739)         # server id
            self.scheduler.start()

            channel = self.get_channel(884116429421559859)          # welcome channel id
            await channel.send(f'dunce is here bois')               # send login message

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
            print('dunce: im ready\n')                                # bot is ready message
    
        else:
            print('dunce: reconnected\n')                             # bot reconnected

    async def on_message(self, message):
        pass

bot = Bot()
