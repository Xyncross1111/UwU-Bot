import discord
from discord.ext import commands

bot = commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#mute
    @bot.command(name='mute')
    @commands.has_role("BotLevel3")
    async def mute(self, ctx, member: discord.Member):
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
    async def unmute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted_role)

        embed = discord.Embed(title="Unmute",
                              description=f" Unmuted - {member.mention}",
                              colour=discord.Colour.blue())

        await ctx.send(embed=embed)

#purge

    @bot.command(alias=['p', 'purge'])
    @commands.has_role('BotLevel2')
    async def purge(self, ctx, no_=3):
        await ctx.channel.purge(limit=no_)

#kick

    @bot.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title='Member Kicked',
            description=f'{member.mention} has been kicked from {ctx.guild}',
            color=0x5865F2)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Executed by {ctx.author.name}')
        await ctx.send(embed=embed)

#ban

    @bot.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title='Member Banned',
            description=f'{member.mention} has been Banned from {ctx.guild}',
            color=0x5865F2)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Executed by {ctx.author.name}')
        await ctx.send(embed=embed)

    @bot.command(name='banlist')
    async def banlist(ctx):
        banned_list = await ctx.guild.bans()
        await ctx.send(banned_list)
#unban

    @bot.command(name='unban')
    async def unban(self, ctx, *, member):
        banned_list = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_list:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title='Member Unbanned',
                    description=
                    f'{member.mention} has been Unbanned from {ctx.guild}',
                    color=0x5865F2)
                embed.set_footer(icon_url=ctx.author.avatar_url,
                                 text=f'Executed by {ctx.author.name}')
                await ctx.send(embed=embed)
                return


#create a channel

    @bot.command(name='createchannel', help=':Creates a new channel')
    @commands.has_role('BotLevel1')
    async def createchannel(self, ctx, channel_name):

        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating new channel: {channel_name}')
            await guild.create_text_channel(channel_name)
            await ctx.send(f'{channel_name} has been created')

    @bot.command()
    async def whois(self, ctx, member: discord.Member):
        embed = discord.Embed(title=member.name,
                              description=member.mention,
                              color=discord.Color.red())
        embed.add_field(name='ID', value=member.id, inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

    @bot.command()
    async def av(self, ctx, member: discord.Member):
        embed = discord.Embed(color=discord.Color.Red())
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @bot.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.'
                           )


def setup(bot):
    bot.add_cog(Moderation(bot))
