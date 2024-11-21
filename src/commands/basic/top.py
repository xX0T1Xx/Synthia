import discord
from discord.ext import commands

from api import lastfm
from database import users

info = {
    "aliases": ["t"],
    "description": "Displays your top 10 scrobbled songs."
}

class Top(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def top(self, ctx, period="overall"):

        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return
        
        tracks = lastfm.getTopTracks(username, period)

        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        value = ""
        for i in range(10):
            track = tracks["toptracks"]["track"][i]
            artist = track["artist"]["name"]
            name = track["name"]
            playcount = int(track["playcount"])
            value += f"**{i+1}.** {artist} - {name} ({playcount:,} Scrobbles)\n"

        embed.add_field(name=f"**Top 10 Tracks**", value=value, inline=False)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Top(bot))