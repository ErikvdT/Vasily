import discord
from discord.ext import commands


async def parse0(zero_lvl_lst):
    operation = zero_lvl_lst[1]
    set1 = set(zero_lvl_lst[0])
    set2 = set(zero_lvl_lst[2])
    if operation == '+':
        return list(set1.union(set2))
    elif operation == '-':
        return list(set1.difference(set2))
    elif operation == '/':
        return list(set1.intersection(set2))

async def parse(input_lst):
    if len(input_lst) == 1:
        return input_lst[0]
    if len(input_lst) == 3:
        return await parse0(input_lst)
    else:
        return await parse([await parse0(input_lst[0:3])] + input_lst[3:])
