from os import listdir
from json import load

import discord
from discord.ext import commands

with open("config.json", 'r') as config_file:
    configs = load(config_file)

#set globals
intents = discord.Intents.all()
client = commands.Bot(command_prefix = configs["prefix"], intents=intents)
fetch_offline_members = True

#load all Cogs from ./cogs
for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#error handling

@client.event
async def on_command_error(ctx, execption):
    if isinstance(execption, commands.CheckFailure):
        await ctx.send(f"You don't have the required permissions to do this.")


#bot starting

@client.event
async def on_ready():
    print("ready")

client.run(configs["token"])
