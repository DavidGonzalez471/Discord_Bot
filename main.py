import discord
from discord.ext import commands
from apikeys import *

intent = discord.Intents.all()
bot = commands.Bot(command_prefix = '', intents=intent)

@bot.event
async def on_ready():
    print('Logged on as Discord Bot!')
    print("-------------------------")

@bot.command()
async def hello(ctx, arg):
    await ctx.send('Hello I am a Discord Bot')
    await ctx.send(arg)

bot.run(DISCORD_TOKEN)