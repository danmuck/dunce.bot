from discord.ext import commands
from discord.ext.commands import Cog 

# define cog object ---
class fun(Cog):

# cog initialization ---
    def __init__(self, bot):
        self.bot = bot 

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up('fun')

        await self.bot.stdout.send(f'cogs: fun cog ready')                  # spam to channel on ready


    @commands.command(name = "yeeter", aliases=["ytr"])
    async def  yeeter(self, ctx, amount=250):
        await ctx.channel.purge(limit=amount)


# cog setup ---
def setup(bot):
    bot.add_cog(fun(bot))