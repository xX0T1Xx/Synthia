import discord
from discord.ext import commands

from database import users, globals, scrobbles
from api import lastfm

info = {
    "aliases": ["t"],
    "description": "Provides your statistics about a song."
}

class Track(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def track(self, ctx, *, args=None):
        
        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return
        
        t = ""
        if args == None:
            latest_track = lastfm.getRecentTracks(username)["recenttracks"]["track"][0]
            t = f"{latest_track['artist']['#text']} - {latest_track['name']}"
        elif args == "^":
            t = globals.get_global("last_track")
        else:
            t = args

        _scrobbles = sorted(scrobbles.get_scrobbles(username), key=lambda x: int(x[2]))

        count = 0
        last = "0"
        for scrobble in _scrobbles:
            if f"{scrobble[4]} - {scrobble[3]}" == t:
                count += 1
                last = scrobble[2]

        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name=f"{t} - {count} scrobbles", value=f"Last scrobbled <t:{last}:R>")
        await ctx.send(embed=embed)

        globals.set_global("last_track", t)


async def setup(bot):
    await bot.add_cog(Track(bot))