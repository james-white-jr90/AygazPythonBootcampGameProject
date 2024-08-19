import random

def kurallar():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Oyun kuralları: ")
    print("1. Taş, Makas'ı yener.")
    print("2. Makas, Kağıt'ı yener.")
    print("3. Kağıt, Taş'ı yener.")
    print("4. İlk iki turu kazanan oyunu kazanır.\n")

def tas_kagıt_makas_BAYRAM_AKPAN():
    toplam_tur_sayisi = 0
    toplam_oyun_sayisi = 0

    while True:
        oyuncu_skoru = 0
        bilgisayar_skoru = 0
        tur_sayisi = 0
        toplam_oyun_sayisi += 1

        secenekler = ['taş', 'kağıt', 'makas']

        while oyuncu_skoru < 2 and bilgisayar_skoru < 2:
            tur_sayisi += 1
            toplam_tur_sayisi += 1

            print(f"\nOynanan tur sayısı: {tur_sayisi}")

            oyuncu_secimi = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim! Lütfen 'taş', 'kağıt' veya 'makas' yazın.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
                (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or \
                (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş'):
                print("Bu turu kazandınız!")
                oyuncu_skoru += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_skoru += 1

            print(f"Skorlar: Oyuncu {oyuncu_skoru} - Bilgisayar {bilgisayar_skoru}")

        if oyuncu_skoru == 2:
            print("\nTebrikler! Oyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı!")

        print(f"\nToplam oynanan tur sayısı: {toplam_tur_sayisi}")
        print(f"Toplam oynanan oyun sayısı: {toplam_oyun_sayisi}")
        print(f"Son Oyun Skorları: Oyuncu {oyuncu_skoru} - Bilgisayar {bilgisayar_skoru}")

        # Oyuna devam edip etmeme sorgusu
        devam_secimleri = ['evet', 'hayır']
        oyuncu_devam = input("\nOyuna devam etmek ister misiniz? (evet/hayır): ").lower()

        bilgisayar_devam = random.choice(devam_secimleri)
        print(f"Bilgisayarın devam etme seçimi: {bilgisayar_devam}")

        if oyuncu_devam == 'hayır' or bilgisayar_devam == 'hayır':
            print("Oyun sona erdi. Teşekkürler!")
            break
        else:
            print("Oyun yeniden başlıyor!")

if __name__ == "__main__":
    kurallar()
    tas_kagıt_makas_BAYRAM_AKPAN()
