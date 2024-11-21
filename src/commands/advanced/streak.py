import discord
from discord.ext import commands

from database import scrobbles, users

info = {
    "aliases": [],
    "description": "Displays your top 10 longest looping streaks."
}

class Streak(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def streak(self, ctx):
        
        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return

        _scrobbles = sorted(scrobbles.get_scrobbles(username), key=lambda x: int(x[2]))

        # element: [[scrobble1, scrobble2, ...], count]
        runs = [[[_scrobbles[0]],1]]
        for scrobble in _scrobbles[1:]:
            if scrobble[3] == runs[len(runs)-1][0][0][3]:
                runs[len(runs)-1][0].append(scrobble)
                runs[len(runs)-1][1] += 1
            else:
                runs.append([[scrobble],1])
        runs.sort(key=lambda x: x[1], reverse=True)

        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        for i in range(10):
            run = runs[i]
            track = run[0][0][3]
            artist = run[0][0][4]
            count = run[1]
            start = run[0][0][2]
            end  = run[0][len(run[0])-1][2]
            
            embed.add_field(name=f"{artist} - {track} - {count} times", value=f"<t:{start}> - <t:{end}>", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Streak(bot))