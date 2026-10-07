import discord
from discord.ext import commands
from L17.main2 import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    print("Hello")
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def check(ctx):
    if not ctx.message.attachments:
        await ctx.send("Lütfen bir resim yükle.")
        return

    for attachment in ctx.message.attachments:
        if not attachment.content_type or not attachment.content_type.startswith("image/"):
            await ctx.send(f"`{attachment.filename}` bir resim değil.")
            continue
        file_path = f"./{attachment.filename}"
        try:
            await attachment.save(file_path)
            result = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=file_path
            )
            await ctx.send(f"Tahmin: {result}")
        except Exception as e:
            print("HATA:", repr(e))
   
            await ctx.send("Resim analiz edilirken bir hata oluştu.")
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

bot.run("MTU0NzMxODgxNjU2Mjg4MDU3Mg.GmwL7_.iIcKa8bf__HnjDXSi3eVM_TBIW_gaVFO_6Zl0Y")