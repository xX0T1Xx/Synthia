from discord.ext import commands

from database import users

info = {
    "aliases": ["l"],
    "description": "Links your discord account to your lastfm account."
}

class Link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=info["aliases"])
    async def link(self, ctx, username):
        users.create_user(ctx.author.id)
        users.set_username(ctx.author.id, username)
        await ctx.send(f"Linked <@{ctx.author.id}> to {username}!")

async def setup(bot):
    await bot.add_cog(Link(bot))