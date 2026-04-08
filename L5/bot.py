import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"we heve logged in as {bot.user}")

@bot.command()
async def mem(ctx):
    with open("L5\images\mem1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTQ4ODk3ODc5NTc3OTMzMDA5MA.GD-Yag.eYyxTZ61EVtsDazI5iZgEMnxlmdmwmjg15CnTo")