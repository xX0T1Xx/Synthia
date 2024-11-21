import asyncio
import math

from discord.ext import commands

from database import scrobbles, users
from api import lastfm

info = {
    "aliases": ["import", "i", "d"],
    "description": "Imports a user's scrobbles"
}

class Download(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.downloading = []

    @commands.command(aliases=info["aliases"])
    async def download(self, ctx):

        username = users.get_username(ctx.author.id)
        if username == None:
            await ctx.send("Please link your account first!")
            return

        if username in self.downloading:
            await ctx.send(f"{username}'s scrobbles are currently being imported!")
            return
        else:
            self.downloading.append(username)
        
        await ctx.send(f"Importing {username}'s scrobbles!")

        try:
            playcount1 = int(lastfm.getInfo(username)["user"]["playcount"])
            playcount2 = len(scrobbles.get_scrobbles(username))
            total = playcount1 - playcount2
            count = 0

            for page in range(1, math.ceil(total/200)+1):

                tracks = await asyncio.to_thread(lastfm.getRecentTracks, username, 200, page)
                _scrobbles = []

                for track in tracks["recenttracks"]["track"]:
                    if "@attr" in track: continue
                    
                    uts = track["date"]["uts"]
                    name = track["name"]
                    artist = track["artist"]["#text"]
                    album = track["album"]["#text"]

                    _scrobbles.append([username, uts, name, artist, album])
                
                await asyncio.to_thread(scrobbles.add_scrobbles, _scrobbles)

                count += len(_scrobbles)
                print(f"Added {len(_scrobbles)} tracks! ({count}/{total})")

        except:
            await ctx.send(f"Error importing {username}'s scrobbles!")

        finally:
            self.downloading.remove(username)
            await ctx.send(f"Finished importing {username}'s scrobbles!")

async def setup(bot):
    await bot.add_cog(Download(bot))