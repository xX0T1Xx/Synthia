import discord
from discord.ext import commands

from database import users
from api import lastfm

info = {
    "aliases": ["s"],
    "description": "Provides general stats about your LastFM profile"
}

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def stats(self, ctx):

        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return

        embed = discord.Embed(title="Statistics")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        information = lastfm.getInfo(username)["user"]
        
        general_info = ""
        general_info += f"{information['name']}\n"
        general_info += f"{information['country']}\n"
        general_info += f"Registered <t:{information['registered']['unixtime']}:D>\n"

        stats_info = ""
        stats_info += f"Playcount: **{int(information['playcount']):,}**\n"
        stats_info += f"Artists: **{int(information['artist_count']):,}**\n"
        stats_info += f"Tracks: **{int(information['track_count']):,}**\n"
        stats_info += f"Albums: **{int(information['album_count']):,}**\n"

        embed.add_field(name="General", value=general_info)
        embed.add_field(name="Statistics", value=stats_info)
        embed.set_thumbnail(url=information["image"][3]["#text"])

        await ctx.send(embed=embed)




async def setup(bot):
    await bot.add_cog(Stats(bot))