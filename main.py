import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import yt_dlp
from yt_dlp import YoutubeDL


DISCORD_TOKEN = 'MTA3ODM5OTI5NDg3NDMzMzI3NA.GudrPB.4a43mqI9WF8FjFbA2nVo0VQ_9WfOuZCVkHxYa4'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)

YDL_OPTIONS = {"format":"m4a/bestaudio/best",
               "extractaudio": True,
                "noplaylist": True}

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                   'options': '-vn'}

async def __init__(self, bot):

    self.bot = bot

    self.is_playing
    self.is_paused

    self.queue = []
    self.vc = None

@bot.event
async def on_ready():
    print("Ready")
    print("--------------")

@bot.command(name='hello')
async def hello(ctx):
    member = ctx.author
    await ctx.send(f"Hello, {member.name} I am a discord bot")

@bot.command(name='join', pass_context=True)
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except:
        await ctx.send("Please join a voice channel")

@bot.command(name='leave', pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.disconnect()
        await ctx.send("Leaving voice channel")
    else:
        await ctx.send("I am not in a voice channel.")



def search_yt(self, song):
    
    with YoutubeDL(self.YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % song, download=False)['entries'][0]
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

        self.vc.play(FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda r: self.play_music())
    else:
        self.is_playing = False

@bot.command(name= "play", aliases = ['PLAY', 'Play', 'p' ], pass_context = True)
async def play(self, ctx, *args, pass_context = True):
    query = "".join(args)

    channel = ctx.author.voice.channel
    if channel is None:
        await ctx.send("Connect to a voice channel")
    elif self.is_paused:
        self.vc.resume()
    else:
        song = self.search_yt(query)
        if type(song) == type(True):
            await ctx.send("Couldn't get the song")
        else:
            await ctx.send("Song added to queue")
            self.queue.append([song, channel])
            if self.is_playing == False:
                await self.play(ctx, after= None)

@bot.command(name = 'play_next', aliases = ['playnext', 'pn', 'PLAYNEXT', ' queue', 'play next'], pass_context = True)
async def play_next(self, ctx, *args, pass_context = True):
    query = "".join(args)

    channel = ctx.author.voice.channel
    if channel is None:
        await ctx.send("Connect to a voice channel")
    if self.is_playing == False:
        await ctx.send("No song playing, play a song.")
    else:
        song = self.search_yt(query)
        if type(song) == type(True):
            await ctx.send("Couldn't get the song")
        else:
            await ctx.send("Song added to the queue")
            self.music_queue.append([song, channel])





        

bot.run(())