import discord
import random
from discord.ext import commands

bot = commands

nom_gif = [
    'https://cdn.discordapp.com/attachments/927483664630169630/928405814950121543/anime-ear-ear-bite.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405815285657720/anime-nom.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405815742849054/jingaisan-no-yome-kanenogi.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405816099373066/chuuu.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405816380358656/nom-nom-nom.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405816967589888/nom-love.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405817185681500/bite-anime.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405817428938752/anime-bite.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928405817676398644/wholesome-nom-nom-nom-nom.gif',
]

cuddle_gif = [
    'https://media.discordapp.net/attachments/927483664630169630/928392998314713098/anime-lap-pillow.gif',
    'https://tenor.com/view/anime-lap-pillow-anime-lap-pillow-pillow-comfy-gif-22934085'
    'https://media.discordapp.net/attachments/927483664630169630/928392997094166628/cuddles-anime.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928392997094166628/cuddles-anime.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928392996683141120/anime-snuggle.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928392996175642694/anime-love.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928392995718434836/sao-sword-art-online.gif'
]

kiss_gif = [
    'https://media.discordapp.net/attachments/927483664630169630/928397545279983707/eden-of-the-east-akira-takizawa.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928397544931860511/anime-kissing.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928397544386621510/cute-kawai.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928397544051052624/anime-kiss.gif5',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398319569494106/kiss-anime_1.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398320215425084/besos-beso.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398320706125834/anime-cute.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398321209458748/anime-kiss_1.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398321846976634/kuzu-no-honkai-kissing.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398322199322644/girl-anime.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928398322627133500/kiss-anime.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928398323193352242/anime-ano.gif'
]

lap_pillow = [
    'https://cdn.discordapp.com/attachments/927483664630169630/928399867506737152/izayoi-sonosuke_1.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928399867875823616/anime-lap-pillow_1.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928399868484022282/lap-sleep.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928399868907626556/lap-pillow.gif',
    'https://media.discordapp.net/attachments/927483664630169630/928399869234790431/nogamenolife-shiro.gif',
    'https://tenor.com/view/izayoi-sonosuke-sonosukeizayoi-danganronpa3-danganronpa-gif-5947990',
]

hug_gif = [
    'https://cdn.discordapp.com/attachments/927483664630169630/928407075233595442/hugs-and-love.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407075510423652/horimiya-izumi-miyamura.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407075745320980/anime-hug.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407076168933407/hug-anime.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407076424777789/cuddle-hug.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407649144434778/anime-hug-sweet.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407648687259648/hug-anime_1.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407648402022440/chuunibyou-anime.gif',
    'https://cdn.discordapp.com/attachments/927483664630169630/928407647965810718/mp4.mp4'
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
        embed = discord.Embed(
            title="NOM",
            description=f'{ctx.author.mention} just nommed {member.mention}',
            color=discord.Color.red())
        response = random.choice(nom_gif)
        embed.set_image(url=response)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

#hug

    @bot.command(name='hug', help='give someone a much deserved hug')
    async def hug(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title="Hug",
            description=f'{ctx.author.mention} just hugged {member.mention}<3',
            color=discord.Color.red())
        response = random.choice(hug_gif)
        embed.set_image(url=response)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

#cuddle

    @bot.command(name='cuddle')
    async def cuddle(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title="CUddle",
            description=f'{ctx.author.mention} just cuddled {member.mention}<3',
            color=discord.Color.red())
        response = random.choice(cuddle_gif)
        embed.set_image(url=response)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

#kiss

    @bot.command(name='kiss')
    async def kiss(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title="KISS",
            description=f'{ctx.author.mention} just kissed {member.mention}<3',
            color=discord.Color.red())
        response = random.choice(kiss_gif)
        embed.set_image(url=response)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)


#lap pillow

    @bot.command(name='lap')
    async def lap(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title="UwU",
            description=
            f"{member.mention} just slept {ctx.author.mention}'s lap <3",
            color=discord.Color.red())
        response = random.choice(lap_pillow)
        embed.set_image(url=response)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(action(bot))
