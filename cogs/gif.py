import discord
from discord.ext import commands
import random

bot = commands


pickup_lines = [
    'I hope you know CPR, because you just took my breath away!',
    'I hope you know CPR, because you just took my breath away!',
    'Are you a   parking ticket? ‘Cause you’ve got ‘fine’ written all over you.',
    'If you were a vegetable, you’d be a ‘cute-cumber.’',
    'Do you happen to have a Band-Aid? ‘Cause I scraped my knees falling for you.',
    'Are you as beautiful on the inside as you are on the outside?',
    'If being sexy was a crime, you’d be guilty as charged.',
    'Do you have a map? I just got lost in your eyes.',
    'Do you know what the Little Mermaid and I have in common? We both want to be part of your world.',
    'If you were a song, you’d be the best track on the album.',
    'On a scale of 1 to America, how free are you tonight?',
    'You know, I always thought that Disneyland was the ‘happiest place on Earth,’ but that was before I got a chance to stand here next to you.',
    'Want to go outside and get some fresh air with me? You just took my breath away.',
    'If you were a taser, you’d be set to ‘stun.’',
    'If you were a Transformer, you’d be ‘Optimus Fine.’',
    'Is your name Google? Because you have everything I’m searching for.',
    'Do you ever get tired from running through my thoughts all night?',
    'You know, they say that love is when you don’t want to sleep because reality is better than your dreams. And after seeing you, I don’t think I ever want to sleep again.',
    'I’m not usually religious, but when I saw you, I knew you were the answer to my prayers.',
    '(Hold out your hand) Hey, I’m going for a walk. Would you mind holding this for me?',
    'Do you believe in love at first sight, or should I try walking by again?',
    'I’m really glad I just bought life insurance, because when I saw you, my heart stopped.',
    'I’m not photographer, but I can definitely picture us together.',
    'Would you mind giving me a pinch? You’re so cute, I must be dreaming.',
    'Wow, when God made you, he was seriously showing off.',
    'Excuse me, do you have the time? I just want to remember the exact minute I got a crush on you.',
    'Kiss me if I’m wrong but, dinosaurs still exist, right?',
    'If I were a cat, I’d spend all nine of my lives with you.'
    'You know, I had a pickup line ready to go, but you’re so hot it just left my mind.',
    'When I text you goodnight later, what phone number should I use?',
    'I saw you walking by and I had to come say hello. I love your style. My name’s (your name).',
    'I’m not currently an organ donor, but I’d be happy to give you my heart.',
    'I was going to say something really sweet about you, but when I saw you, I became speechless.',
    'You know, I believe that honesty is the best policy, so to be perfectly honest, you’re the sexiest man I’ve ever seen.',
    'I’d say, ‘God bless you,’ but it looks like he already did.',
    'You must be a hell of a thief, because you managed to steal my heart from across the room.',
    'There must be something wrong with my eyes—I can’t seem to take them off of you.',
    'If you let me borrow a kiss, I promise I’ll give it right back.'
]

pickup_starter = [
    "You're amazing", "Hello Beautiful", "You're breathtaking", "Hey Cutie"
]


class Gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



#woof

    @bot.command(name='woof', help=':barks for yoou *woof*')
    async def woof(self, ctx):
        await ctx.send(
            "*WOOF WOOF GRRRRRRRRRRRR BARK BARK BARK WOOF RUFF RUFF GRRRR WOOF WOOF BARK BARK BARK BARK RUFF RUFF GRRRRRRR BARK RUFF WOOF BARK BARK BARK BARK RUFF RUFF WOOF BARK GRRRRR BARK BARK RUFF RUFF WOOF WOOF WOOF BARK WOOF*"
        )

#nyaa

    @bot.command(name='nyaa', help=':nyaa nyaaa')
    async def nyaa(self, ctx):
        await ctx.send(
            '*ya nya nya nya~! :3 kyakun-nya-nya, and a pyon-pyon-purrr-nyaa skyaaaaaaa~~~ nya-nya-meow-meow-purr-purr pyan, pyan!!!!*'
        )

#slap

    @bot.command(name='slap', help=':you deserve a slap')
    async def slap(self, ctx):
        await ctx.send(
            'https://tenor.com/view/slap-face-slap-smack-yo-slap-waifu-gif-20089821'
        )


#zhong cop

    @bot.command(name='cop')
    async def cop(self, ctx):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(
            url=
            'https://cdn.discordapp.com/attachments/926976896242188310/928324143986909254/SmartSelect_20220103-010703_TikTok.png'
        )
        await ctx.send(embed=embed)

    @bot.command(name='shock', help=':Truly very shocking!')
    async def shock(self, ctx):
        await ctx.send(
            'https://giphy.com/gifs/funimation-shock-danganronpa-monomi-aiGz8Pczmju2A'
        )

    @bot.command(name='gn', help=':have a nice sleep')
    async def gn(self, ctx):
        await ctx.send(
            "You've worked hard today \nYou can Rest Now \nGoodnight and Sleep well"
        )

    @bot.command(name='pickup', help='Sends a random pickup line')
    async def pickup(self, ctx):
        response1 = random.choice(pickup_lines)
        response2 = random.choice(pickup_starter)
        embed = discord.Embed(title=response2,
                              description=response1,
                              color=discord.Color.red())
        await ctx.send(embed=embed)
        await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(Gif(bot))
