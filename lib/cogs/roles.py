from discord.ext.commands import Cog, command

class roles(Cog):
    def __init__(self, client):
        self.PREFIX = '?'
        self.client = client

    @command(hidden=True)
    async def pings(self, ctx):
        await ctx.send('Pong!')

    @command(name = "role", aliases=["roles"])
    async def role(self, ctx):
        await ctx.send('``` Please select a preferred role by typing a command:\n \n?ccc \n?mod \n?admin *hardware | software | networking | webdev*  \n?associate *who do you know from ccc* ```')
        print('\nNew Member Alert!\n')

    @command(name = "ccc", aliases=["compsci" , "student"], hidden=True)
    async def ccc(self, ctx):
        await ctx.send(f'``` I am a CCC student  ```<@&881287992382197850>')

    @command(name = "joe", aliases=["dr.logic"], hidden=True)
    async def joe(self, ctx):
        await ctx.send(f'``` error: *does not compute*```')

    @command(name = 'mod', aliases = [ 'moderator' , 'mods' ], hidden=True)
    async def mod(self, ctx):
        await ctx.send(f'``` **Keep sanity in the public channels primarily** Please communicate with other admins before pushing structural changes. >> mod ```<@&881287992382197850> ')

    @command(name = "admin", aliases=["administrator"], hidden=True)
    async def admin(self, ctx, *, spec='im a god'):
        await ctx.send(f'``` **This is a contributor role and it is expected that you understand this.** Please communicate with other admins before pushing structural changes. >> admin {spec}```<@&881287992382197850>')

    @command(name = "associate", aliases=["ass" , "as"], hidden=True)
    async def associate(self, ctx, *, friends='friends at ccc?'):
        await ctx.send(f'``` I would like to hang out with my CCC friends. I know {friends} ```<@&881287992382197850> ')

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('roles')
    # @Cog.listener()
    # async def on_ready(self):
    #     print('cogs: [roles] online')
# end #
def setup(client):
    client.add_cog(roles(client))

