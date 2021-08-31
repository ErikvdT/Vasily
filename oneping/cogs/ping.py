from json import load

import discord
from discord.ext import commands

from lib.parse import parse


async def get_member(ctx, member_role):
    # convert given string to list of member objects
    try:
        # first assume input is a role
        role = await discord.ext.commands.RoleConverter().convert(ctx, member_role)
        member_lst = role.members
    except:
        try:
            # else search for user
            member = await discord.ext.commands.MemberConverter().convert(ctx, member_role)
            member_lst = [member]
        except:
            await ctx.send(f"Could not find {member_role}")
            return

    return member_lst

class OnePing(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx, *args):
        """
        Ping any number of roles or user.
        
        Usage: combine roles or usernames with any operator followed by an optional message
        
        +: add members of the two elements
        -: subtract members from first element
        /: get the intersection of the two elements
        
        Example: !ping role - user message"""

        with open("config.json", 'r') as config_file:
            configs = load(config_file)
        msg = ''
        eval_lst = []
        operator = False
        word = False
        # check syntax for alternating word and operator
        # and create list of items to evaluate
        # words without operator separation are interpreted as message to send
        for arg in args:
            if arg in {'+', '-', '/'} and not operator:
                eval_lst += arg
                operator = True
                word = False
            elif arg in {'+', '-', '/'} and operator:
                ctx.send("Invalid syntax. Use !help for more info.")
                return
            elif word:
                msg += f" {arg}"
                word = True
            else:
                # nest member lists in evaluation list
                eval_lst.append(await get_member(ctx, arg))
                word = True

        # get list of members to ping
        member_lst = await parse(eval_lst)
        tmp_role = await ctx.guild.create_role(name = configs["tmp_role"], mentionable = True, reason = f"Ping cmd from Vasily invoked by {ctx.message.author}")
        msg = tmp_role.mention + msg + f"\n- from {ctx.message.author.nick}"

        for member in member_lst:
            await member.add_roles(tmp_role, reason = f"Ping cmd from Vasily invoked by {ctx.message.author}")

        # delete invoking message
        await ctx.message.delete()
        await ctx.send(msg)
        await tmp_role.delete(reason = f"Ping cmd from Vasily invoked by {ctx.message.author}")
        return

def setup(client):
    client.add_cog(OnePing(client))
