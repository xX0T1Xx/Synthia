import discord
from discord.ext import commands

from database import users, scrobbles

info = {
    "aliases": ["m"],
    "description": "Provides the date you achieved a given scrobble count"
}

class Milestone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def milestone(self, ctx, count):
        
        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return

        _scrobbles = sorted(scrobbles.get_scrobbles(username), key=lambda x:int(x[2]))
        _count = int(count.replace(",", ""))

        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        if _count > len(_scrobbles):
            embed.add_field(name="Error", value=f"You have less than {_count} scrobbles!")
            await ctx.send(embed=embed)
            return

        else:
            embed.add_field(name=f"Achieved {_count} scrobbles on:", value=f"<t:{_scrobbles[_count-1][2]}>")
            await ctx.send(embed=embed)
            return
        

async def setup(bot):
    await bot.add_cog(Milestone(bot))