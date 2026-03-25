import random

sir = random.randint(0,21)
trials = 8

for i in range(trials):
    guess = int(input("trials" + str(i + 1) + ": 1 den 20 ye kadar olan sayıları tahmin et:"))
    if guess == sir:
        print("Tebrikler 🤩 Doğru Bildin. Kazandın!🎉")
        break

    elif guess < sir:
        print("Sayı Daha Yüksek. Malesef Bilemedin! Tekrar Dene! ☹️")
    else:
        print("Sayı Daha Yüksek. Malesef Bilemedin! Tekrar Dene! ☹️")
else:
    print(f"Malesef Hakkınız Kalmadı. Kaybettiniz Oley Ben Kazandım 😏 ama yinede iyi oyundu 😉 tekrar görüşmek üzere gizli sayı {sir} ")
