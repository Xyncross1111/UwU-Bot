import discord
import random
from discord.ext import commands

bot = commands

nom_gif = [
        'https://tenor.com/view/wholesome-nom-nom-nom-nom-anime-scared-gif-16372716',
        'https://tenor.com/view/anime-bite-gif-23254686',
        'https://tenor.com/view/bite-anime-cute-gif-8259627',
        'https://tenor.com/view/nom-love-gif-13291182',
        'https://tenor.com/view/nom-nom-nom-gif-19008702',
        'https://tenor.com/view/chuuu-gif-9938336',
        'https://tenor.com/view/jingaisan-no-yome-kanenogi-anime-nom-me-when-your-bussy-gif-23328719',
        'https://tenor.com/view/anime-nom-neko-kawaii-anime-blush-gif-15735907',
        'https://tenor.com/view/anime-ear-ear-bite-anime-nom-anime-couple-gif-16088514',
    ]

cuddle_gif = [
    'https://tenor.com/view/cuddle-anime-hug-comfort-sweet-gif-16498143',
    'https://tenor.com/view/anime-lap-pillow-anime-lap-pillow-pillow-comfy-gif-22934085'
    'https://tenor.com/view/cute-cuddle-sleeping-love-gif-5858494',
    'https://tenor.com/view/cuddles-anime-gif-11733535',
    'https://tenor.com/view/anime-snuggle-cuddle-oreshura-eita-gif-16361738',
    'https://tenor.com/view/anime-love-cuddle-cute-couple-gif-14518537',
    'https://tenor.com/view/sao-sword-art-online-love-kirito-asuna-gif-16542536',
    ''
]

kiss_gif = [
    'https://tenor.com/view/eden-of-the-east-akira-takizawa-anime-kiss-blushing-gif-17092948',
    'https://tenor.com/view/anime-kissing-kiss-love-gif-10356314',
    'https://tenor.com/view/cute-kawai-kiss-anime-gif-16371489',
    'https://tenor.com/view/anime-kiss-love-sweet-gif-5095865',
    'https://tenor.com/view/anime-ano-natsu-de-matteru-gif-9670722',
    'https://tenor.com/view/kiss-anime-love-couple-intimate-gif-17193768',
    'https://tenor.com/view/girl-anime-kiss-anime-i-love-you-girl-kiss-gif-14375355',
    'https://tenor.com/view/kuzu-no-honkai-kissing-anime-affection-hanabi-yasuraoka-gif-11831573',
    'https://tenor.com/view/anime-kiss-gif-20779050',
    'https://tenor.com/view/anime-cute-kiss-in-love-gif-12192867',
    'https://tenor.com/view/besos-beso-besito-besitos-besote-gif-16585116',
    'https://tenor.com/view/kiss-anime-anime-kiss-animegirl-animeboy-gif-13387677'
]

lap_pillow = [
    'https://tenor.com/view/anime-lap-pillow-pillow-anime-love-emilia-gif-21896027',
    'https://tenor.com/view/nogamenolife-shiro-headrub-sleepy-tired-gif-6238142',
    'https://tenor.com/view/lap-pillow-gif-19164779',
    'https://tenor.com/view/lap-sleep-on-gif-19033450',
    'https://tenor.com/view/anime-lap-pillow-anime-lap-pillow-pillow-comfy-gif-22934085',
    'https://tenor.com/view/izayoi-sonosuke-sonosukeizayoi-danganronpa3-danganronpa-gif-5947990',
]

class action(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

#ping
  @bot.command(name="pinga")
  async def pinga(self, ctx):
      await ctx.reply(
        f"*Pong!*  The latency is `{round(self.bot.latency * 1000)}ms`  \nAll's Good"
    )

#nom

  @bot.command(name='nom')
  async def nom(self, ctx, member: discord.Member):
    await ctx.send('{} just nommed {}'.format(ctx.author.mention, member.mention))
    response = random.choice(nom_gif)
    await ctx.send(response)
  
  @bot.command()
  async def nom1(self, ctx, member: discord.Member):
    embed = discord.Embed(color = discord.Color.red())
    embed.set_image(url = random.choice(nom_gif))
    await ctx.send(embed=embed)


#cuddle

  @bot.command(name='cuddle')
  async def cuddle(self, ctx, member: discord.Member):
    await ctx.send('{} just cuddled {} UwU'.format(ctx.author.mention, member.mention))
    response = random.choice(cuddle_gif)
    await ctx.send(response)


#kiss

  @bot.command(name='kiss')
  async def kiss(self, ctx, member: discord.Member):
    await ctx.send('{} just kissed {} <3'.format(ctx.author.mention, member.mention))
    response = random.choice(kiss_gif)
    await ctx.send(response)


#lap pillow

  @bot.command(name='lap')
  async def lap(self, ctx, member: discord.Member):
    await ctx.send("{} just slept on {}'s lap <3".format(
        member.mention, ctx.author.mention))
    response = random.choice(lap_pillow)
    await ctx.send(response)

def setup(bot):
  bot.add_cog(action(bot))