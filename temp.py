#original code before switching to cogs


import os
import discord
import random

from replit import db
from dotenv import load_dotenv
from discord.ext import commands
from dontdie import dontdie

load_dotenv()

bot = commands.Bot(command_prefix="!")


def add_link(new_link):
    if "giflinks" in db.keys():
        giflinks = db["giflinks"]
        giflinks.append(new_link)
        db["giflinks"] = giflinks


def delete_link(index):
    giflinks = ["giflinks"]
    if len(giflinks) > index:
        del giflinks[index]
        db["giflinks"] = giflinks

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
    await ctx.send(
        f"*Pong!*  The latency is `{round(bot.latency * 1000)}ms`  \nAll's Good"
    )

#imp
#redo
@bot.event
async def on_member_join(member):
    print("{member}has joined the server")


#server name (irrelevant? lmao)
@bot.command(name='server')
async def server(ctx):
    await ctx.send(ctx.guild)


@bot.command(name='test')
async def test(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))


@bot.command(aliases=['hello', 'helu'])
async def Hello(ctx):
    await ctx.send(f"hello, {ctx.author.mention}")


@bot.command(name='pickup', help='Sends a random pickup line')
async def pickup(ctx):
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

    response = random.choice(pickup_lines)
    await ctx.send(response)


@bot.command(name='working', help='tells itf the bot is working')
async def working(ctx):
    await ctx.send("Yes")


@bot.command(name='info', help=':tells info')
async def info(ctx):
    await ctx.send("Coder - Xyncross#0001 \nCreated 12/28/21")


@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title="Sample Embed",
        url="https://realdrewdata.medium.com/",
        description=
        "This is an embed that will show how to build an embed and the different components",
        color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command(name='whois1', help='gets information about the user')
async def whois1(ctx, member: discord.Member):
    embed = discord.Embed(title=ctx.member.name,
                          description=ctx.member.mention)
    embed.add_field(name="ID", value=ctx.member.id, inline=True)
    await ctx.send(embed=embed)


@bot.command(name='whois', help='gets information about the user')
async def whois(ctx, member: discord.Member):
    await ctx.send("User:{}".format(member.mention) +
                   "\nThe user is `{}`".format(member.name) +
                   "\nThe user's ID is `{}`".format(member.id))


#@bot.command()
async def xyn(ctx):
    embed = discord.embed(url="https://tenor.com/view/wink-anime-gif-7784168")
    await ctx.send(embed=embed)  #


gen_gifs = [
    'https://tenor.com/view/rias-gremory-gif-19135269',
    'https://tenor.com/view/wink-anime-gif-7784168',
    'https://tenor.com/view/blush-rias-gremory-highschool-dxd-anime-cute-gif-17791241',
    'https://tenor.com/view/riasgremory-funnyface-highschooldxd-wink-gif-8958138',
    'https://tenor.com/view/rias-gremory-high-school-dxd-gremory-rias-anime-gif-18954869',
    'https://tenor.com/view/rias-gremory-high-school-dxd-gremory-rias-gif-18954866',
    'https://tenor.com/view/rias-rias-gremory-gif-18947895',
    'https://tenor.com/view/rias-gremory-gif-19135277', ''
]


@bot.command(name='gen', help=':why does this work but the other not ugh')
async def gen(ctx):
    response = random.choice(gen_gifs)
    await ctx.send(response)


@bot.command(name='ayuyu', help=':OOoOoOOooOoooOOOo')
async def ayuyu(ctx):
    await ctx.send("https://tenor.com/view/ayuyu-gif-23227373")


@bot.command(name='woof', help=':barks for yoou *woof*')
async def woof(ctx):
    await ctx.send(
        "*WOOF WOOF GRRRRRRRRRRRR BARK BARK BARK WOOF RUFF RUFF GRRRR WOOF WOOF BARK BARK BARK BARK RUFF RUFF GRRRRRRR BARK RUFF WOOF BARK BARK BARK BARK RUFF RUFF WOOF BARK GRRRRR BARK BARK RUFF RUFF WOOF WOOF WOOF BARK WOOF*"
    )


@bot.command(name='nyaa', help=':nyaa nyaaa')
async def nyaa(ctx):
    await ctx.send(
        '*ya nya nya nya~! :3 kyakun-nya-nya, and a pyon-pyon-purrr-nyaa skyaaaaaaa~~~ nya-nya-meow-meow-purr-purr pyan, pyan!!!!*'
    )


@bot.command(name='pereb', help=':them fine legs')
async def pereb(ctx):
    await ctx.send(
        'https://tenor.com/view/spider-zhongli-spiderzhongli-gif-21689465')


@bot.command(name='slap', help=':you deserve a slap')
async def slap(ctx):
    await ctx.send(
        'https://tenor.com/view/slap-face-slap-smack-yo-slap-waifu-gif-20089821'
    )


@bot.command(name='monomi', help=':Why ask?')
async def monomi(ctx):
    await ctx.send('https://imgur.com/gallery/bAFuNdh')


@bot.command(name='alli', help=':Im sleepy')
async def alli(ctx):
    await ctx.send(
        'https://tenor.com/view/ganyu-genshin-impact-cute-gif-24203853')


@bot.command(name='shock', help=':Truly very shocking!')
async def shock(ctx):
    await ctx.send(
        'https://giphy.com/gifs/funimation-shock-danganronpa-monomi-aiGz8Pczmju2A'
    )


@bot.command(name='gn', help=':have a nice sleep')
async def gn(ctx):
    await ctx.send(
        "You've worked hard today \nYou can Rest Now \nGoodnight and Sleep well"
    )


@bot.command(name='alli2', help='SO CUTE OMFG')
async def alli2(ctx):
    await ctx.send(
        "https://tenor.com/view/shy-bye-rabbit-bunny-fluff-gif-5340278")


#action commands

hug_gif = [
    'https://tenor.com/view/cuddle-hug-anime-bunny-costumes-happy-gif-17956092',
    'https://tenor.com/view/hug-anime-clingy-gif-7552075',
    'https://tenor.com/view/anime-hug-sweet-love-gif-14246498',
    'https://tenor.com/view/horimiya-izumi-miyamura-hori-kyoko-couple-hug-gif-14539121',
    'https://tenor.com/view/hugs-and-love-gif-19327081',
    'https://tenor.com/view/anime-hug-sweet-anime-gif-13857539',
    'https://tenor.com/view/hug-anime-cartoon-japanese-fall-gif-7552093',
    'https://tenor.com/view/chuunibyou-anime-couple-anime-couple-cute-gif-13576064',
    'https://media.tenor.co/videos/6d50cb0b25b712d0859088e3fb95d35e/mp4'
]


@bot.command(name='hug', help='give someone a much deserved hug')
async def hug(ctx, arg):
    await ctx.send('{} just hugged {}'.format(ctx.author.mention, arg))
    response = random.choice(hug_gif)
    await ctx.send(response)


#nom
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


@bot.command(name='nom')
async def nom(ctx, arg):
    await ctx.send('{} just nommed {}'.format(ctx.author.mention, arg))
    response = random.choice(nom_gif)
    await ctx.send(response)


#cuddle

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


@bot.command(name='cuddle')
async def cuddle(ctx, arg):
    await ctx.send('{} just cuddled {} UwU'.format(ctx.author.mention, arg))
    response = random.choice(cuddle_gif)
    await ctx.send(response)


#kiss

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


@bot.command(name='kiss')
async def kiss(ctx, arg):
    await ctx.send('{} just kissed {} <3'.format(ctx.author.mention, arg))
    response = random.choice(kiss_gif)
    await ctx.send(response)


#lap pillow

lap_pillow = [
    'https://tenor.com/view/anime-lap-pillow-pillow-anime-love-emilia-gif-21896027',
    'https://tenor.com/view/nogamenolife-shiro-headrub-sleepy-tired-gif-6238142',
    'https://tenor.com/view/lap-pillow-gif-19164779',
    'https://tenor.com/view/lap-sleep-on-gif-19033450',
    'https://tenor.com/view/anime-lap-pillow-anime-lap-pillow-pillow-comfy-gif-22934085',
    'https://tenor.com/view/izayoi-sonosuke-sonosukeizayoi-danganronpa3-danganronpa-gif-5947990',
]


@bot.command(name='lap')
async def lap(ctx, arg):
    await ctx.send("{} just slept on {}'s lap <3".format(
        arg, ctx.author.mention))
    response = random.choice(lap_pillow)
    await ctx.send(response)


#die roll


@bot.command(name='dieroll', help=':roles a die')
async def dieroll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [str(random.choice(range(1, +number_of_sides, 1)))]
    await ctx.send(','.join(dice))


#arithemetic


@bot.command(name='add', help=':adds two numbers')
async def add(ctx, first_number: int, second_number: int):
    sum = first_number + second_number
    await ctx.send(sum)


@bot.command(name='subtract', help=':subtracts two numbers')
async def subtract(ctx, first_number: int, second_number: int):
    remainder = first_number - second_number
    await ctx.send(remainder)


@bot.command(name='multiply', help=':mupltiplies two numbers')
async def multiply(ctx, first_number: int, second_number: int):
    product = first_number * second_number
    await ctx.send(product)


@bot.command(name='divide', help=':divides two numbers')
async def divide(ctx, first_number: int, second_number: int):
    quotient = first_number / second_number
    await ctx.send(quotient)


#direct calc function


@bot.command(name='calc', help='do any arithemetic calculation')
async def calc(ctx, first_number: int, operation: str, second_number: int):
    if operation == ("+"):
        await ctx.send(str(first_number + second_number))

    elif operation == ("-", ):
        await ctx.send(str(first_number - second_number))

    elif operation == ("*"):
        await ctx.send(str(first_number * second_number))

    elif operation == ("x"):
        await ctx.send(str(first_number * second_number))

    elif operation == ("/"):
        await ctx.send(str(first_number / second_number))

    else:
        await ctx.send(
            "Enter Values in correct format\n`First value + Operation + Second value`"
        )


# primogem calculator


@bot.command(name='primos', help=':Calculates Fates from given primogems')
async def primos(ctx, primo: int):

    fates = primo / 160
    await ctx.send("You have " + str(int(fates)) + " wishes")

    if str(int(fates)) == ("0"):
        await ctx.send("you broke asf lol")


#pity calculator


@bot.command(name='pity')
async def pity(ctx, wish_count: int, primos: int = 0):
    pity_counter = wish_count + primos / 160

    await ctx.send("You will have " + str(int(pity_counter)) +
                   " wishes done on pity counter.")

    embed = discord.Embed(title='Pity Calculator',
                          description='You will have made ' +
                          str(int(pity_counter)) + " wishes.",
                          color=discord.Color.purple())

    await ctx.send(embed=embed)

    if str(int(pity_counter)) == ("0"):

        embed = discord.Embed(title='Pity Calulator',
                              description="O pulls LMAOO\nYou broke af lol",
                              color=discord.Color.black())
        await ctx.send(embed=embed)


#mute


@bot.command(name='mute')
@commands.has_role("BotLevel3")
async def mute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")

        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role,
                                          speak=False,
                                          send_messages=False,
                                          read_message=False)

    await member.add_roles(muted_role)

    embed = discord.Embed(title="Mute",
                          description=f" Muted - {member.mention}",
                          colour=discord.Colour.red())

    await ctx.send(embed=embed)
    await ctx.member.send('You have been muted')


#unmute


@bot.command(name='unmute')
@commands.has_role("BotLevel3")
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role)

    embed = discord.Embed(title="Unmute",
                          description=f" Unmuted - {member.mention}",
                          colour=discord.Colour.blue())

    await ctx.send(embed=embed)


#purge


@bot.command(alias=['p', 'purge'])
@commands.has_role('BotLevel2')
async def purge(ctx, no_=3):
    await ctx.channel.purge(limit=no_)


#kick


@bot.command(name='kick')
@commands.has_role('BotLevel3')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server')


#ban


@bot.command(name='ban')
@commands.has_role('BotLevel3')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server')


@bot.command(name='banlist')
async def banlist(ctx):
    banned_list = await ctx.guild.bans()
    await ctx.send(banned_list)


@bot.command(name='unban')
async def unban(ctx, *, member):
    banned_list = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_list:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been unbanned from the server')
            return


#create a channel


@bot.command(name='createchannel', help=':Creates a new channel')
@commands.has_role('BotLevel1')
async def createchannel(ctx, channel_name):

    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        await ctx.send(f'{channel_name} has been created')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


dontdie()

bot.run(os.environ['TOKEN'])
