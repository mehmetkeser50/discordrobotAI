# Görev 1

ad = input("adınız nedir?")
yas = int(input("kaç yaşındasınız?"))

gelecek_yil_yas = + 1

print(f"Hoşgeldin {ad} gelecek yıl {gelecek_yil_yas} yaşında olacaksın")

# Görev 2
kelime = input("bir kelime yazarmısın?")
unluler = "aeıioöuüAEIİOÖUÜ"
sayac = 0

for harf in kelime:
    if harf in unluler:
        sayac +=1

    print("Sesli Harf sayısı: ", sayac)

# Görev 3

metin = input("bir metin giriniz: ")

if len(metin) > 10:
    print("Sonuç: ", metin[:10]+"...")
else :
    print("Sonuç: ", metin)
    

