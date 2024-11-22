import discord
from discord.ext import commands

from database import users, globals
from api import lastfm

info = {
    "aliases": [],
    "description": "Displays the current song you're listening to."
}

class Fm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fm(self, ctx):
        
        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return
        
        track = lastfm.getRecentTracks(username)["recenttracks"]["track"][0]
        name = track["name"]
        artist = track["artist"]["#text"]
        album = track["album"]["#text"]
        image = track["image"][3]["#text"]
        nowplaying = "@attr" in track

        embed = discord.Embed()
        embed.add_field(name=f"{name}", value=f"{artist}" + (f" - {album}" if album else ""), inline=False)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.set_thumbnail(url=image)
        embed.set_footer(text=("Now Playing" if nowplaying else "Last Track"))
        await ctx.send(embed=embed)

        globals.set_global("last_track", f"{artist} - {name}")


async def setup(bot):
    await bot.add_cog(Fm(bot))