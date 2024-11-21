import os

import discord
from discord.ext import commands

info = {
    "aliases": ["h"],
    "description": "Displays information about every command."
}

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def help(self, ctx, command=None):
        
        embed = discord.Embed(title="Help")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        if command == None:
            for category in os.listdir("./commands"):
                commands = [command[:-3] for command in os.listdir(f"./commands/{category}")]
                embed.add_field(name=category, value=", ".join(commands), inline=False)
            await ctx.send(embed=embed)
            return
        else:
            for category in os.listdir("./commands"):
                for cmd in os.listdir(f"./commands/{category}"):
                    if cmd[:-3] == command:
                        vars = {}
                        with open(f"./commands/{category}/{cmd}") as file:
                            exec(file.read(), vars)
                        embed.add_field(name="Aliases", value=", ".join(vars["info"]["aliases"]), inline=False)
                        embed.add_field(name="Description", value=vars["info"]["description"], inline=False)
                        await ctx.send(embed=embed)
                        return
            embed.add_field(name="Error", value="Command not found!", inline=False)
            await ctx.send(embed=embed)
            return

                            

async def setup(bot):
    await bot.add_cog(Help(bot))