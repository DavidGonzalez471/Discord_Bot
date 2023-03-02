import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
from apikeys import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)

players= {}
queue = []
joined = False

@bot.event
async def on_ready():
    print('Logged on as Discord Bot!')
    print("-------------------------")

#function for bot to say hello 
@bot.command()
async def hello(ctx):
    await ctx.send('Hello I am a Discord Bot')

#function for bot to leave server
@bot.command()
async def goodbye(ctx):
    exit()

#function for bot to join voice channel
@bot.command(pass_context = True)
async def join(ctx):
    if (ctx. author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send("Joining voice channel.")
        voice = await channel.connect()
        source = FFmpegPCMAudio('')
        player = voice.play(source)
        joined = True
    else:
        await ctx.send("You are not in a voice channel, Join one first.")

#function for bot to leave the voice channel.
@bot.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Leaving voice channel.")
        joined = False
    else:
        await ctx.send("I am not in a voice channel")

@bot.command(pass_context = True)
async def play(ctx, song):

    guild = ctx.message.guild
    voice_channel = guild.voice_client
    player = await voice_channel.create_ytdl_player(song)
    players[guild.id] = player
    player.start()


bot.run(DISCORD_TOKEN)
