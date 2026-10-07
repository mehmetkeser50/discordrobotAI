import random
import time
import scipy.io.wavfile as wav
import sounddevice as sd
import speech_recognition as sr

# Ayarlamalar
sample_rate = 44100  # Örnekleme hızı
duration = 5  # Kayıt süresi (saniye)
max_errors = 3  # Maksimum hata sayısı

recognizer = sr.Recognizer()

# Saf Python ile kelime ve çeviri sözlüğü
kelime_sozlugu = {
    "kedi": "cat",
    "köpek": "dog",
    "elma": "apple",
    "süt": "milk",
    "güneş": "sun",
    "muz": "banana",
    "okul": "school",
    "arkadaş": "friend",
    "pencere": "window",
    "sarı": "yellow",
    "teknoloji": "technology",
    "üniversite": "university",
    "bilgi": "information",
    "telaffuz": "pronunciation",
    "hayal gücü": "imagination",
}

# Seviyelere göre kelime grupları
seviyelere_göre_kelimeler = {
    "kolay": ["kedi", "köpek", "elma", "süt", "güneş"],
    "orta": ["muz", "okul", "arkadaş", "pencere", "sarı"],
    "zor": ["teknoloji", "üniversite", "bilgi", "telaffuz", "hayal gücü"],
}

print("Oyunumuza hoş geldiniz! Türkçe kelimelerin İngilizce karşılığını bulun.")

while True:
  skor = 0  # Başlangıç skoru
  errors = 0  # Hata sayacı

  # === Seviyeleri seçme ===
  print("\nSeviye seçin: kolay, orta, zor")
  level = input("Seviye: ").strip().lower()

  while level not in seviyelere_göre_kelimeler:
    print("Geçersiz seviye. Lütfen 'kolay', 'orta' veya 'zor' seçin.")
    level = input("Seviye: ").strip().lower()

  # Orijinal listenin kopyasını alıp karıştırıyoruz
  kelime_list = list(seviyelere_göre_kelimeler[level])
  random.shuffle(kelime_list)

  print(f"\nZorluk seviyesi: {level.capitalize()}")
  print("Hazırlanın, oyun başlıyor...")
  time.sleep(2)

  for kelime in kelime_list:
    print(f"\n--------------------------------")
    print(f"Türkçe Kelime: {kelime}")
    print("Cevap verme yöntemini seç:")
    print("1 ➔ Sesli Söyle (Konuş)")
    print("2 ➔ Klavyeden Yaz (Yaz)")

    secim = input("Seçiminiz (1 veya 2): ").strip()

    tanimlanan = ""
    cevap_basarili = True

    if secim == "1":
      print("🎙️ Şimdi konuşun...")
      try:
        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
        )
        sd.wait()
        wav.write("output.wav", sample_rate, recording)
        print("⏳ Kayıt tamamlandı, algılanıyor...")
      except Exception as e:
        print(f"❌ Ses kaydı sırasında bir hata oluştu: {e}")
        continue

      try:
        with sr.AudioFile("output.wav") as source:
          audio = recognizer.record(source)

        tanimlanan = recognizer.recognize_google(audio, language="en").lower()
        print("🗣️ Algılanan ses:", tanimlanan)

      except sr.UnknownValueError:
        errors += 1
        print(f"🔇 Konuşma tanınamadı. Hatalar: {errors}/{max_errors}")
        cevap_basarili = False
      except sr.RequestError as e:
        print(f"⚠️ Google Ses Tanıma servisinden sonuç alınamadı: {e}")
        continue

    elif secim == "2":
      tanimlanan = (
          input("⌨️ İngilizce çevirisini yazın: ").strip().lower()
      )
      print(f"✍️ Yazdığınız: {tanimlanan}")
    else:
      print("⚠️ Geçersiz seçim yaptınız! Bu kelime atlanıyor.")
      continue

    # Eğer konuşma başarısız olduysa ve hata sınırına ulaşıldıysa kontrol et
    if not cevap_basarili:
      if errors >= max_errors:
        print("\n☠️☠️☠️☠️ Oyun bitti. 3 hata yaptın kaybettin.")
        break
      continue

    # Saf Python sözlüğünden doğru çeviriyi alıyoruz
    ceviri = kelime_sozlugu.get(kelime, "").lower()
    print(f"📝 Doğru Karşılığı: {ceviri}")

    if tanimlanan == ceviri:
      skor += 1
      print("✅ Doğru! +1 puan")
    else:
      errors += 1
      print(
          f"❌ Yanlış! Beklenen: {ceviri}. Hatalar:"
          f" {errors}/{max_errors}"
      )
      if errors >= max_errors:
        print("\n☠️☠️☠️☠️ Oyun bitti. 3 hata yaptın kaybettin.")
        break

  print(f"\n🏁 Oyun bitti! Toplam skorunuz: {skor}")

  # Tekrar oynamak ister mi?
  tekrar = input("\nTekrar oynamak ister misiniz? (E/H): ").strip().lower()
  if tekrar not in ["e", "evet", "y", "yes"]:
    print("👋 Oynadığınız için teşekkürler! Görüşmek üzere.")
    break
