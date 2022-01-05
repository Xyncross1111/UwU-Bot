#use  as reference DO NOT CHANGE

import discord
from discord.ext import commands

bot = commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

    @commands.command()
    async def piing(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def test(ctx, arg1, arg2):
        await ctx.send('You passed {} and {}'.format(arg1, arg2))


def setup(bot):
    bot.add_cog(Example(bot))
