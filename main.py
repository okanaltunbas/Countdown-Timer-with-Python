import time
import datetime

while True:
    try:
        saniye = int(input("Süreyi giriniz : "))
        break
    except:
        print("Hatalı giriş! Tekrar deneyin!")

def geri_say(saniye):

    print(f"Başlangıç zamanı {datetime.datetime.now()} :")

    while saniye > 0:

        dakika, saniye = divmod(saniye,60)
        zaman = "{:02d}:{:02d}".format(dakika,saniye)
        print(zaman)

        time.sleep(1)
        saniye -= 1


    print("Süre doldu!")
    print(f"Bitiş zamanı {datetime.datetime.now()} :")


geri_say(saniye)