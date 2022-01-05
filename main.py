import os
import discord
import random


from discord.ext import commands




bot = commands.Bot(command_prefix="!")

#load extensions


@bot.command(name='load')
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


#unload


@bot.command(name='unload')
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


#ping
@bot.command(name="ping")
async def ping(ctx):
    await ctx.reply(
        f"*Pong!*  The latency is `{round(bot.latency * 1000)}ms`  \nAll's Good"
    )


@bot.command(aliases=['hello', 'helu'])
async def Hello(ctx):
    await ctx.reply(f"hello, {ctx.author.mention}")


@bot.command(name='working', help='tells itf the bot is working')
async def working(ctx):
    await ctx.send("Yes")


@bot.command(name='info', help=':tells info')
async def info(ctx):
    await ctx.send("Coder - Xyncross#0001 \nCreated 12/28/21")


@bot.command()
async def owner(ctx):
    embed = discord.Embed(
        title="OWNER",
        description="Coder - Xyncross#0001 \nCreated 12/28/21",
        color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command()
async def xyn(ctx):
    embed = discord.embed(color=discord.Color.red())
    embed.set_image(
        url='https://media.tenor.co/videos/9537cc5cc9d4e62a9caa804f988b9279/mp4'
    )
    await ctx.send(embed=embed)  



bot.run('OTIyMTExMTY4NjQwODY4NDAy.Yb8s8g.wYjkroXMRuyW1QiIBZRBapHHafM')
