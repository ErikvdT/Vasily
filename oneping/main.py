import os

import discord
from discord.ext import commands


#set globals
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
fetch_offline_members = True

#load all Cogs from ./cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Commands for un/loading Cogs through discord
@client.command(hidden = True)
@commands.is_owner()
async def load(ctx, arg1):
    client.load_extension(f'cogs.{format(arg1)}')
    await ctx.send(f'{arg1} loaded!')

@client.command(hidden = True)
@commands.is_owner()
async def unload(ctx, arg1):
    client.unload_extension(f'cogs.{format(arg1)}')
    await ctx.send(f'{arg1} unloaded!')

@client.command(hidden = True)
@commands.is_owner()
async def reload(ctx, arg1):
    client.reload_extension(f'cogs.{format(arg1)}')
    await ctx.send(f'{arg1} reloaded!')




#error handling

@client.event
async def on_command_error(ctx, execption):
    if isinstance(execption, commands.CheckFailure):
        await ctx.send(f"You don't have the required permissions to do this.")



#bot starting

@client.event
async def on_ready():
    print("ready")

client.run("")
