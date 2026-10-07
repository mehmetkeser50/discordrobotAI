import tempfile
import os
import time
import requests

import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import pyttsx3

SAMPLE_RATE = 16000
CHANNELS = 1

DURATION = 4
SOURCE_LANG = "en-US"
TARGET_LANG = "tr"

ENERGY_THRESHOLD = 300
TRANSLATION_DELAY = 1.0
MAX_RETRIES = 3

engine = pyttsx3.init()

engine.setProperty("rate", 165)

turkish_voice_found = False

for voice in engine.getProperty("voices"):

    voice_name = str(voice.name).lower()
    voice_id = str(voice.id).lower()

    if (
        "turkish" in voice_name
        or "turkish" in voice_id
        or "tr-tr" in voice_id
        or "tr_" in voice_id
    ):

        engine.setProperty("voice", voice.id)

        print(" Türkçe ses bulundu:", voice.name)

        turkish_voice_found = True

        break


if not turkish_voice_found:

    print(" Türkçe ses bulunamadı.")
    print("Mac'te Türkçe ses yüklü olmayabilir.")

translation_cache = {}

def speak_text(text):

    if not text:
        return

    try:

        print("Türkçe seslendiriliyor...")

        engine.say(text)

        engine.runAndWait()

    except Exception as e:

        print("❌ Seslendirme hatası:", e)

def record_audio(
    duration=DURATION,
    sample_rate=SAMPLE_RATE
):

    print()
    print(" Dinleniyor...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    return recording


def save_temp_wav(
    recording,
    sample_rate=SAMPLE_RATE
):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_file.close()

    wav.write(
        temp_file.name,
        sample_rate,
        recording
    )

    return temp_file.name


def speech_to_text(
    audio_path,
    source_lang=SOURCE_LANG
):

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = ENERGY_THRESHOLD

    recognizer.dynamic_energy_threshold = True

    with sr.AudioFile(audio_path) as source:

        audio = recognizer.record(source)

    print(" Konuşma yazıya çevriliyor...")

    text = recognizer.recognize_google(
        audio,
        language=source_lang
    )

    return text


def translate_text(
    text,
    source_lang="en",
    target_lang="tr"
):

    text = text.strip()

    if not text:

        return ""

    cache_key = (
        text.lower(),
        source_lang,
        target_lang
    )

    if cache_key in translation_cache:

        print(" Çeviri önbellekten alındı.")

        return translation_cache[cache_key]

    time.sleep(TRANSLATION_DELAY)

    url = "https://api.mymemory.translated.net/get"


    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            print(
                f" MyMemory çeviri "
                f"({attempt}/{MAX_RETRIES})..."
            )

            response = requests.get(
                url,
                params=params,
                timeout=10
            )


            # HTTP hatası varsa exception
            response.raise_for_status()


            data = response.json()

            response_data = data.get(
                "responseData",
                {}
            )

            translated = response_data.get(
                "translatedText"
            )


            if translated:

                translated = translated.strip()

                if (
                    translated.lower()
                    != "please select two distinct languages"
                ):

                    translation_cache[cache_key] = translated

                    return translated


            print(
                " MyMemory geçerli bir çeviri "
                "döndürmedi."
            )


        except requests.exceptions.RequestException as e:

            print(
                f" İnternet/API hatası "
                f"({attempt}/{MAX_RETRIES}):"
            )

            print(e)


        except Exception as e:

            print(
                f" Çeviri hatası "
                f"({attempt}/{MAX_RETRIES}):"
            )

            print(e)


        # Tekrar denemeden önce bekle

        if attempt < MAX_RETRIES:

            wait_time = attempt * 3

            print(
                f" {wait_time} saniye bekleniyor..."
            )

            time.sleep(wait_time)


    return "Çeviri yapılamadı."

def interpreter_loop():

    print()
    print("=" * 60)
    print("         GERÇEK ZAMANLI İNGİLİZCE → TÜRKÇE")
    print("=" * 60)

    print()
    print(" Kaynak dil :", SOURCE_LANG)
    print(" Hedef dil  :", TARGET_LANG)
    print(" Dinleme     :", DURATION, "saniye")
    print()
    print(" Çeviri      : MyMemory API")
    print(" Ses         : pyttsx3")
    print()
    print("Çıkmak için CTRL + C")
    print("=" * 60)


    while True:

        temp_wav = None

        try:

            recording = record_audio()

            temp_wav = save_temp_wav(
                recording
            )

            text = speech_to_text(
                temp_wav,
                SOURCE_LANG
            )

            if not text or not text.strip():

                print(
                    " Konuşma algılanmadı."
                )

                continue


            text = text.strip()


            print()
            print(" İngilizce:")
            print(text)


            translated = translate_text(
                text,
                source_lang="en",
                target_lang="tr"
            )


            print()
            print(" Türkçe:")
            print(translated)

            if (
                translated
                and translated != "Çeviri yapılamadı."
            ):

                speak_text(
                    translated
                )


            print()
            print("-" * 60)

        except sr.UnknownValueError:

            print(
                " Konuşma anlaşılamadı."
            )


        except sr.RequestError as e:

            print()
            print(
                " Google Speech Recognition "
                "hatası:"
            )

            print(e)

            print(
                " 5 saniye bekleniyor..."
            )

            time.sleep(5)

        except KeyboardInterrupt:

            print()
            print("=" * 60)
            print(" Program durduruldu.")
            print("=" * 60)

            break

        except Exception as e:

            print()
            print(
                " Beklenmeyen hata:"
            )

            print(e)

            time.sleep(2)

        finally:

            if (
                temp_wav
                and os.path.exists(temp_wav)
            ):

                try:

                    os.remove(temp_wav)

                except Exception:

                    pass

if __name__ == "__main__":

    interpreter_loop()  