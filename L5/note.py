#‘w’ - bir dosyayı yazma modunda açar fakat içindeki her şeyi siler;
#‘r’ - bir dosyayı salt okunur modda açar;
#‘a’ - dosyadan hiçbir şey çıkarmadan dosyanın sonuna veri kaydeder;
#‘rb’ - okumak için metin olmayan bir dosya açar;
#'wb’ - yazmak için metin olmayan bir dosya açar.

e = open("notetext.txt", "w", encoding="utf-8")
text = "merhaba"
e.write(text)
e.close()

o=open("notetext.txt", "r", encoding="utf-8")
file = o.read()
print(file)
o.close()

e = open("notetext.txt", "w", encoding="utf-8")
text = "nasılsın?"
e.write(text)
e.close()

o=open("notetext.txt", "r", encoding="utf-8")
file = o.read()
print(file)
o.close()

bot.run("MTQ4ODk3ODc5NTc3OTMzMDA5MA.GD-Yag.eYyxTZ61EVtsDazI5iZgEMnxlmdmwmjg15CnTo")