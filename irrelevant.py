import discord
from discord.ext import commands

bot = commands
class Irrelevant(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
#server name (irrelevant? lmao)
  @bot.command(name='server')
  async def server(ctx):
      await ctx.send(ctx.guild)


def setup(bot):
  bot.add_cog(Irrelevant(bot))