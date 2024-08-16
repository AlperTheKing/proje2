def menu():
    print("\n--- Rehber Uygulaması ---")
    print("1. Kişi Ekle")
    print("2. Kişileri Listele")
    print("3. Kişi Ara")
    print("4. Kişiyi Düzelt")
    print("5. Kişiyi Sil")
    print("6. Çıkış")
    choice = input("Seçiminiz nedir? ")
    return choice

def kişi_ekle(rehber):
    isim = input("Kişinin ismi: ")
    telefon = input("Kişinin telefon numarası: ")
    rehber[isim] = telefon
    print(f"{isim} isimli kişi rehbere eklendi.")

def kişileri_listele(rehber):
    if not rehber:
        print("Rehberde kişi bulunmamaktadır.")
    else:
        for isim, telefon in rehber.items():
            print(f"İsim: {isim}, Telefon: {telefon}")

def kişi_ara(rehber):
    isim = input("Aramak istediğiniz kişinin ismi: ")
    if isim in rehber:
        print(f"İsim: {isim}, Telefon: {rehber[isim]}")
    else:
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")

def kişi_düzelt(rehber):
    isim = input("Düzeltmek istediğiniz kişinin ismi: ")
    if isim in rehber:
        yeni_telefon = input(f"{isim} için yeni telefon numarasını girin: ")
        rehber[isim] = yeni_telefon
        print(f"{isim} isimli kişinin telefon numarası güncellendi.")
    else:
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")

def kişi_sil(rehber):
    isim = input("Silmek istediğiniz kişinin ismi: ")
    if isim in rehber:
        del rehber[isim]
        print(f"{isim} isimli kişi rehberden silindi.")
    else:
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")

def rehber_uygulaması():
    rehber = {}
    while True:
        seçim = menu()
        if seçim == '1':
            kişi_ekle(rehber)
        elif seçim == '2':
            kişileri_listele(rehber)
        elif seçim == '3':
            kişi_ara(rehber)
        elif seçim == '4':
            kişi_düzelt(rehber)
        elif seçim == '5':
            kişi_sil(rehber)
        elif seçim == '6':
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Rehber Uygulamasını başlat
rehber_uygulaması()