import os

def rehber_dosyası_oku(dosya_adi):
    rehber = {}
    if os.path.exists(dosya_adi):
        with open(dosya_adi, 'r') as dosya:
            for satır in dosya:
                parcalar = satır.strip().split(':', 1)
                if len(parcalar) == 2:
                    isim, telefon = parcalar
                    rehber[isim] = telefon
    return rehber

def rehber_dosyası_yaz(dosya_adi, rehber):
    with open(dosya_adi, 'w') as dosya:
        for isim, telefon in rehber.items():
            dosya.write(f"{isim}:{telefon}\n")

def kişi_ekle(rehber, dosya_adi):
    isim = input("Kişinin ismi: ")
    telefon = input("Kişinin telefon numarası: ")
    rehber[isim] = telefon
    rehber_dosyası_yaz(dosya_adi, rehber)
    print(f"{isim} isimli kişi rehbere eklendi.")
    input("Devam etmek için Enter'a basın...")

def kişileri_listele(rehber):
    if not rehber:
        print("Rehberde kişi bulunmamaktadır.")
    else:
        for isim, telefon in rehber.items():
            print(f"İsim: {isim}, Telefon: {telefon}")
    input("Devam etmek için Enter'a basın...")

def kişi_ara(rehber):
    isim = input("Aramak istediğiniz kişinin ismi: ").lower()
    bulundu = False
    for kayıtlı_isim, telefon in rehber.items():
        if kayıtlı_isim.lower() == isim:
            print(f"İsim: {kayıtlı_isim}, Telefon: {telefon}")
            bulundu = True
            break
    if not bulundu:
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")
    input("Devam etmek için Enter'a basın...")

def kişi_düzelt(rehber, dosya_adi):
    isim = input("Düzeltmek istediğiniz kişinin ismi: ").lower()
    bulundu = False
    for kayıtlı_isim in rehber.keys():
        if kayıtlı_isim.lower() == isim:
            yeni_telefon = input(f"{kayıtlı_isim} için yeni telefon numarasını girin: ")
            rehber[kayıtlı_isim] = yeni_telefon
            rehber_dosyası_yaz(dosya_adi, rehber)
            print(f"{kayıtlı_isim} isimli kişinin telefon numarası güncellendi.")
            bulundu = True
            break
    if not bulundu:
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")
    input("Devam etmek için Enter'a basın...")

def kişi_sil(rehber, dosya_adi):
    isim = input("Silmek istediğiniz kişinin ismi: ").lower()
    bulundu = False
    for kayıtlı_isim in list(rehber.keys()):
        if kayıtlı_isim.lower() == isim:
            del rehber[kayıtlı_isim]
            rehber_dosyası_yaz(dosya_adi, rehber)
            print(f"{kayıtlı_isim} isimli kişi rehberden silindi.")
            bulundu = True
            break
    if not bulundu:
        print(f"{isim} isimli kişi rehberde bulunmamaktadır.")
    input("Devam etmek için Enter'a basın...")

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

def rehber_uygulaması():
    dosya_adi = "rehber.txt"
    rehber = rehber_dosyası_oku(dosya_adi)
    while True:
        seçim = menu()
        if seçim == '1':
            kişi_ekle(rehber, dosya_adi)
        elif seçim == '2':
            kişileri_listele(rehber)
        elif seçim == '3':
            kişi_ara(rehber)
        elif seçim == '4':
            kişi_düzelt(rehber, dosya_adi)
        elif seçim == '5':
            kişi_sil(rehber, dosya_adi)
        elif seçim == '6':
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Rehber Uygulamasını başlat.
rehber_uygulaması()