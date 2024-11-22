import random

import discord
from discord.ext import commands

from database import users, scrobbles, globals

info = {
    "aliases": ["r"],
    "description:": "Provides a random song you've scrobbled."
}

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def random(self, ctx):

        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return
        
        _scrobbles = sorted(scrobbles.get_scrobbles(username), key=lambda x: int(x[2]))

        # {"artist - name": [last_utc, count], ...}
        tracks = {}
        for scrobble in _scrobbles:
            track = f"{scrobble[4]} - {scrobble[3]}"
            time = scrobble[2]
            if not track in tracks:
                tracks[track] = [time, 1]
            else:
                tracks[track][0] = time
                tracks[track][1] += 1

        rt = list(tracks.items())[random.randint(0, len(tracks.items()))]
        
        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name=f"{rt[0]} ({rt[1][1]} Scrobbles)", value=f"Last scrobbled on <t:{rt[1][0]}>")
        await ctx.send(embed=embed)

        globals.set_global("last_track", rt[0])


async def setup(bot):
    await bot.add_cog(Random(bot))