import discord
from discord import app_commands
from discord.ext import commands
import os
import random

TOKEN = "MTQ4ODk3ODc5NTc3OTMzMDA5MA.GD-Yag.eYyxTZ61EVtsDazI5iZgEMnxlmdmwmjg15CnTo"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class Cevrebot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @app_commands.command(name="başla", description="atık azaltmaya başlamak için ilk adımları gösterir")
        async def basla(self, interaction: discord.Interaction):
            mesaj = (
            "atık azaltmaya başlamak için 3 kolay adım: \n"
            "1. Tek kullanımlık ürünleri azalt \n" 
            "2. Su matası ve bez çanta kullan. \n"
            "3. Evde kağıt, plastik ve camı ayrı toplamaya başla."
            )
            await interaction.response.send_message(mesaj)

        @app_commands.command(name="başla", description="atık azaltmaya başlamak için ilk adımları gösterir")
        async def basla(self, interaction: discord.Interaction):
            mesajlar = [
            "yere çöp atmayın \n"
            "çevrenizi temiz tutun" 
            "odanızı temiz tutun"

            ]
            await interaction.response.send_message(mesajlar)
              
        @app_commands.command(name="başla", description="atık azaltmaya başlamak için ilk adımları gösterir")
        async def basla(self, interaction: discord.Interaction):
            mesajlar = [
            "çöpleri geri dönüşümde ayrıştırın"
            "fosil yakıtları, gaz, petrol ve egzoz gazlarnı azaltın" 
            ]
            await interaction.response.send_message(mesajlar)

        @app_commands.command(name="başla", description="atık azaltmaya başlamak için ilk adımları gösterir")
        async def basla(self, interaction: discord.Interaction):
            mesajlar = [
            "ve yerdeki çöpleri çöpe atın."
            ]
            await interaction.response.send_message(mesajlar)
@bot.event
async def on_ready():
    await bot.add_cog(Cevrebot(bot))
    try:
        synced = await bot.tree.sync()
        print(f"{bot.user} otomaitk olarak giriş yapıldı.")
        print(f"{len(synced)} slash komutu senkronlandı.")
    except Exception as e:
        print("komutlar senkronlandı :", e)

bot.run(TOKEN)
            
            
            

            

            