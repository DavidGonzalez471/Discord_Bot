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


    @commands.command(name='hello')
    async def hello(self, ctx):
        member = ctx.author
        await ctx.send(f"Hello, {member.name} I am a discord bot")

    def search_yt(self, song):

        YDL_OPTIONS = {"format":"bestaudio", "noplaylist": "True"}

        #with YoutubeDL() 
