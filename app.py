import random

def tahmin_oyunu():
    # Rastgele bir sayı tut
    tutulan_sayi = random.randint(1, 100)
    deneme_hakki = 3
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
    
    for deneme in range(deneme_hakki):
        try:
            tahmin = int(input(f"{deneme + 1}. tahmininizi girin: "))
            
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue
            
            if tahmin < tutulan_sayi:
                print("Daha yüksek bir sayı tahmin et.")
            elif tahmin > tutulan_sayi:
                print("Daha düşük bir sayı tahmin et.")
            else:
                print(f"Tebrikler! Sayıyı doğru tahmin ettiniz: {tutulan_sayi}")
                break
            
            if deneme == deneme_hakki - 1:
                print(f"Üzgünüm, deneme haklarınız bitti. Tutulan sayı: {tutulan_sayi}")
        
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

# Oyun başlat
tahmin_oyunu()
