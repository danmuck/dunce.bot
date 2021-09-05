from discord.ext.commands import Cog 

# define cog object ---
class fun(Cog):

# cog initialization ---
    def __init__(self, bot):
        self.bot = bot 

    @Cog.listener
    async def on_ready(self):
        self.bot.stdout.send(f'cogs: fun cog ready')


# cog setup ---
def setup(bot):
    bot.add_cog(fun(bot))