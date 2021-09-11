from discord import Embed
from discord.utils import get
# from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import Cog, command
from typing import Optional


def syntax(command):
    cmd_and_aliases = ' | '.join([str(command), *command.aliases])
    params = []

    for key, value in command.params.items():
        if key not in ('self', 'ctx'):
            params.append(f'[{key}]' if "NoneType" in str(
                value) else f'<{key}>')

    params = ' '.join([command.signature])

    return f'```{cmd_and_aliases} {params}```'

# class helpmenu(ListPageSource):
#     def __init__(self, ctx, entries):
#         self.ctx = ctx
#         super().__init__(entries, per_page=3)

#     async def write_page(self, menu, fields=[]):
#         offset = (menu.current_page*self.per_page) + 1
#         len_data = len(self.entries)

#         embed = Embed(title='help',
#                             description='dunce.bot: how can i help you?',
#                             colour=self.ctx.author.colour)
#         embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
#         embed.set_footer(text=f'{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands')

#         for name, value in fields:
#             embed.add_field(name=name, value=value, inline=False)

#         return embed

#     async def format_page(self, menu, entries):
#         fields = []

#         for entry in entries:
#             fields.append((entry.brief or 'no description', syntax(entry)))

#         return await self.write_page(menu, fields)


class help(Cog):
    def __init__(self, client):
        self.client = client
        # self.client.remove_command('help')  #remove default help command

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up('help')

    async def cmd_help(self, ctx, command):
        embed = Embed(title=f'help with `{command}`',
                            description=syntax(command),
                            colour=ctx.author.colour)
        embed.add_field(name='command description', value=command.help)
        await ctx.send(embed=embed)

    @command(name='halp', aliases=['hlp', '??', '?', '???', '????', '?????', '??????', '???????', '????????'])
    async def show_help(self, ctx, cmd: Optional[str]):
        """shows this message """
        if cmd is None:
            #     menu = MenuPages(source=helpmenu(ctx, list(self.client.commands)),
            #                         delete_message_after=True,
            #                         timeout=60.0)
            #     await menu.start(ctx)
            # await ctx.send('`try: ?help`')
            embed = Embed(title='help menu',
                            description=' try command: [ ?help ] ')
            await ctx.send(embed=embed)

        else:
            if (cmd := get(self.client.commands, name=cmd)):
                await self.cmd_help(ctx, cmd)

            else:
                await ctx.send(f'error: command does not exist')

# run cog ---


def setup(client):
    client.add_cog(help(client))
