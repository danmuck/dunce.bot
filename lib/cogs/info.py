from discord.ext.commands import Cog
from discord.ext.commands import command

class info(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('info')

    


# end ---
def setup(client):
    client.add_cog(info(client))