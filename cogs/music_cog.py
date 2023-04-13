#building a music cog to organize the code more, not working yet.
#CommandNotFound on cogs

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import yt_dlp
from yt_dlp import YoutubeDL
 

class music_bot(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

        self.is_playing
        self.is_paused

        self.queue = []
        self.vc = None
        

   @commands.command(name= "play", aliases = ['PLAY', 'Play', 'p' ], pass_context = True)
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

   @commands.command(name = 'play_next', aliases = ['playnext', 'pn', 'PLAYNEXT', ' queue', 'play next'], pass_context = True)
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
