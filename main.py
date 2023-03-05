import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
import yt_dlp
from yt_dlp import YoutubeDL
import json
from apikeys import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)

players= {}

def _init_(self,bot):
    self.bot = bot
    self.is_playing = False
    self.is_paused = False
    
    self.queue = []

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'beofre_options': '-reconnect 1 -reconnect_streamed 1 - reconnect_delay_max 5', 'options': '-vn'}

    self.vc = None

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

def search_yt(self, song):
    
    with YoutubeDL(self.YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % song, download=False)['entries'][0]
            info = (json.dumps(ydl.sanitize_info(info)))
        except Exception:
            return False
    return{'source': info['formats'][0]['url'], 'title':info['title']}

async def play_music(self, ctx):
    if len(self.queue) > 0:
        self.is_playing = True
        m_url = self.queue[0][0]['source']

        if self.vc == None or not self.vc.is_connected():
            self.vc = await self.queue[0][1].connect()
        
        if self.vc == None:
            await ctx.send("Could not connect to the voice channel call the join function")
        
        self.queue.pop(0)

        self.vc.play(discord,FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda r: self.play_music())
    else:
        self.is_playing = False

@bot.command(aliases = ['PLAY', 'Play', 'p' ], pass_context = True)
async def play(ctx, url):

    guild = ctx.message.guild
    voice_channel = guild.voice_client
    urls = [url]
    with YoutubeDL() as ydl:
        await play(ydl.download(urls), after=None)


    

bot.run(DISCORD_TOKEN)
