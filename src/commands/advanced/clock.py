import matplotlib.pyplot as plt
import os

import discord
from discord.ext import commands

from database import users, scrobbles
from utils import time

info = {
    "aliases": [],
    "description": "Displays your most frequent listening hours."
}

class Clock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def clock(self, ctx):
        
        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return
        
        _scrobbles = scrobbles.get_scrobbles(username)

        times = {
            "12 AM":0,
            "1 AM":0,
            "2 AM":0,
            "3 AM":0,
            "4 AM":0,
            "5 AM":0,
            "6 AM":0,
            "7 AM":0,
            "8 AM":0,
            "9 AM":0,
            "10 AM":0,
            "11 AM":0,
            "12 PM":0,
            "1 PM":0,
            "2 PM":0,
            "3 PM":0,
            "4 PM":0,
            "5 PM":0,
            "6 PM":0,
            "7 PM":0,
            "8 PM":0,
            "9 PM":0,
            "10 PM":0,
            "11 PM":0
        }

        for scrobble in _scrobbles:
            hour = time.get_hour(int(scrobble[2]))
            times[hour] += 1

        plt.clf()
        plt.bar(times.keys(), times.values())
        plt.xticks(rotation=90)
        plt.xlabel("Time")
        plt.ylabel("Scrobbles")

        file_name = f"data/{ctx.author.id}.png"
        plt.savefig(file_name)
        await ctx.send(file=discord.File(file_name))
        os.remove(file_name)

async def setup(bot):
    await bot.add_cog(Clock(bot))