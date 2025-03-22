import discord
from discord.ext import commands
from text import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def contexto(ctx):
    await ctx.send(f'👀 muy void 👀')



@bot.command()
async def void(ctx, count_heh = 5):
    await ctx.send(voidmem)

@bot.command()
async def machete(ctx, count_heh = 5):
    await ctx.send("empezemos por las piernas")

bot.run("token")
