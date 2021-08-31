import discord
from discord.ext import commands


class Manage(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands for un/loading Cogs through discord
    @commands.command(hidden = True)
    @commands.is_owner()
    async def load(self, ctx, arg1):
        self.client.load_extension(f'cogs.{format(arg1)}')
        await ctx.send(f'{arg1} loaded!')

    @commands.command(hidden = True)
    @commands.is_owner()
    async def unload(self, ctx, arg1):
        self.client.unload_extension(f'cogs.{format(arg1)}')
        await ctx.send(f'{arg1} unloaded!')

    @commands.command(hidden = True)
    @commands.is_owner()
    async def reload(self, ctx, arg1):
        self.client.reload_extension(f'cogs.{format(arg1)}')
        await ctx.send(f'{arg1} reloaded!')

def setup(client):
    client.add_cog(Manage(client))
