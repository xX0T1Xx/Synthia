import matplotlib.pyplot as plt
import os

import discord
from discord.ext import commands

from api import lastfm
from database import scrobbles, users

info = {
    "aliases": ["sot"],
    "description": "Graphs your scrobbles over time."
}

class ScrobblesOverTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def scrobblesovertime(self, ctx):

        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return

        info = lastfm.getInfo(username)
        _scrobbles = sorted(scrobbles.get_scrobbles(username), key=lambda x: int(x[2]))

        x = [int(info["user"]["registered"]["unixtime"])]
        y = [0]
        count = 0

        for scrobble in _scrobbles:
            x.append(int(scrobble[2]))
            y.append(count)
            count += 1

        plt.clf()
        plt.plot(x, y)
        plt.xlabel("Time")
        plt.ylabel("Scrobbles")
        plt.title("Scrobbles Over Time")

        file_name = f"data/{ctx.author.id}.png"
        plt.savefig(file_name)
        await ctx.send(file=discord.File(file_name))
        os.remove(file_name)

async def setup(bot):
    await bot.add_cog(ScrobblesOverTime(bot))