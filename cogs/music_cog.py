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

    def search_yt(self, song):

        YDL_OPTIONS = {"format":"bestaudio",
                        "extractaudio": True,
                        "noplaylist": True}

        #with YoutubeDL() 