import discord
from discord.ext import commands

from database import users, scrobbles
from utils import time

info = {
    "aliases": ["g", "break"],
    "description": "Displays your longest listening gaps."
}

class Gap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def gap(self, ctx):
        
        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return
        
        _scrobbles = sorted(scrobbles.get_scrobbles(username), key=lambda x: int(x[2]))

        # [(scrobble1 time, scrobble2 time), (), ...]
        gaps = []
        for i in range(len(_scrobbles)-1):
            gaps.append((int(_scrobbles[i][2]), int(_scrobbles[i+1][2])))
        gaps.sort(key=lambda x: x[1]-x[0], reverse=True)

        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        for i in range(10):
            embed.add_field(
                name = time.timestamp(gaps[i][1]-gaps[i][0]),
                value = f"<t:{gaps[i][0]}> - <t:{gaps[i][1]}>",
                inline = False
            )
        
        await ctx.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(Gap(bot))