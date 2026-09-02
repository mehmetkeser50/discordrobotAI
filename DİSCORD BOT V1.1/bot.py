import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# --- İLK KOMUT: RESİM GÖNDERİR (!mem) ---
@bot.command()
async def mem(ctx):
    try:
        with open(r"L5\images\mem1.jpg", "rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("Hata: mem1.jpg Dosyası Bulunamadı!")

# --- İKİNCİ KOMUT: VİDEO GÖNDERİR (!balik) ---
@bot.command()
async def balik(ctx):
    try:
        with open(r"L5\images\balık.mp4", "rb") as f:
            video = discord.File(f)
        await ctx.send(file=video)
    except FileNotFoundError:
        await ctx.send("Hata: balık.mp4 Dosyası Bulunamadı!")

# Botu çalıştırıyoruz
bot.run("MTQ4ODk3ODc5NTc3OTMzMDA5MA.GD-Yag.eYyxTZ61EVtsDazI5iZgEMnxlmdmwmjg15CnTo")