import asyncio
import os

import discord
from discord.ext import commands

from database import tokens

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot started.")

@bot.command()
async def echo(ctx, *args):
    await ctx.send(' '.join(args))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error occured: {error}")

async def load_commands():
    for dir in os.listdir("./commands"):
        for file in os.listdir(f"./commands/{dir}"):
            await bot.load_extension(f"commands.{dir}.{file[:-3]}")

async def main():
    await load_commands()
    await bot.start(tokens.Discord())

if __name__ == "__main__":
    asyncio.run(main())