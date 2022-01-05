import discord
from discord.ext import commands
import random

#arithemetic

bot = commands


class Arithmetic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#die roll

    @bot.command(name='dieroll', help=':roles a die')
    async def dieroll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [str(random.choice(range(1, +number_of_sides, 1)))]
        await ctx.send(','.join(dice))

#arithemetic

    @bot.command(name='add', help=':adds two numbers')
    async def add(self, ctx, first_number: int, second_number: int):
        sum = first_number + second_number
        await ctx.send(sum)

    @bot.command(name='subtract', help=':subtracts two numbers')
    async def subtract(self, ctx, first_number: int, second_number: int):
        remainder = first_number - second_number
        await ctx.send(remainder)

    @bot.command(name='multiply', help=':mupltiplies two numbers')
    async def multiply(self, ctx, first_number: int, second_number: int):
        product = first_number * second_number
        await ctx.send(product)

    @bot.command(name='divide', help=':divides two numbers')
    async def divide(self, ctx, first_number: int, second_number: int):
        quotient = first_number / second_number
        await ctx.send(quotient)

#direct calc function

    @bot.command(name='calc', help='do any arithemetic calculation')
    async def calc(self, ctx, first_number: int, operation: str,
                   second_number: int):
        if operation == ("+"):
            #embed = discord.Embed(title='Calculation', description=)  #add fields
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
    async def primos(self, ctx, primo: int):

        fates = primo / 160
        await ctx.send("You have " + str(int(fates)) + " wishes")
        if str(int(fates)) == ("0"):
            await ctx.send("you broke asf lol")


#pity calculator

    @bot.command(name='pity')
    async def pity(self, ctx, wish_count: int, primos: int = 0):
        pity_counter = wish_count + primos / 160

        embed = discord.Embed(title='Pity Calculator',
                              description='You will have made ' +
                              str(int(pity_counter)) + " wishes.",
                              color=discord.Color.purple())

        await ctx.send(embed=embed)

        if str(int(pity_counter)) == ("0"):
            embed = discord.Embed(
                title='Pity Calulator',
                description="O pulls LMAOO\nYou broke af lol",
                color=discord.Color.red())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Arithmetic(bot))
