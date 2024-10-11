#22100011055 Ceyda Ünal
#Otel Otomasyonu

def oda_ara(oda_no):

    with open("otel_verileri.txt","r") as dosya:
        veriler = dosya.readlines()

        for veri in veriler:
            kontrol = True
            oda_bilgileri = veri.split(",")
            if oda_bilgileri[0] == oda_no:
                kontrol = False
                oda_no = oda_bilgileri[0]
                oda_tipi = oda_bilgileri[1]
                fiyat = oda_bilgileri[2]
                rezerve = oda_bilgileri[3]
                print("Oda no:{}\nOda Tipi:{}\nFiyat:{}\nRezerve Durumu:{}\n ".format(oda_no, oda_tipi, fiyat, rezerve))
                return
        print("Boyle bir oda bulunamadi.")

def oda_ekle(oda_no,oda_tipi,fiyat,rezerve):
    with open("otel_verileri.txt", "r") as dosya:
        veriler = dosya.readlines()

        for veri in veriler:
            oda_bilgileri = veri.split(",")
            odalar = []
            odalar.append(oda_bilgileri[0])
    try:
        for i in odalar:
            if oda_no == i:
                print("Bu oda numarasi zaten mevcut.")
            else:
                with open("otel_verileri.txt", "a") as dosya:
                    dosya.write(f"{oda_no},{oda_tipi},{fiyat},{rezerve}\n")
                    print("{} nolu oda eklendi".format(oda_no))
    except UnboundLocalError:
        print("Daha once hic oda girilmemis")
        with open("otel_verileri.txt", "a") as dosya:
            dosya.write(f"{oda_no},{oda_tipi},{fiyat},{rezerve}\n")
            print("{} nolu oda eklendi".format(oda_no))

def oda_sil(oda_no):

    with open("otel_verileri.txt","r") as dosya:
        veriler = dosya.readlines()
    with open("otel_verileri.txt","w") as dosya:
        for veri in veriler:
            oda_bilgileri = veri.split(",")
            if oda_bilgileri[0] != oda_no:
                dosya.write(veri)
        print(f"{oda_no} numaralı oda silindi.")

def oda_guncelle(oda_no, oda_tipi=None, fiyat=None, eklenecekMiktar=None,  rezerve=None):

    with open("otel_verileri.txt", "r") as dosya:
        veriler = dosya.readlines()

    with open("otel_verileri.txt","w") as dosya:
        for veri in veriler:
            oda_bilgileri = veri.split(",")
            if oda_bilgileri[0] == oda_no:
                if oda_tipi:
                    oda_bilgileri[1] = oda_tipi
                if fiyat:
                    oda_bilgileri[2] = str(fiyat)
                if eklenecekMiktar:
                    yeniFiyat = int(oda_bilgileri[2]) + eklenecekMiktar
                    oda_bilgileri[2] = str(yeniFiyat)
                if rezerve:
                    oda_bilgileri[3] = str(rezerve)
            dosya.write(",".join(oda_bilgileri) )

def tum_odalar(): #butun odalari ozellikleriyle gorebilmek icin
    with open("otel_verileri.txt", "r") as dosya:
        veriler = dosya.readlines()

        for veri in veriler:
            oda_bilgileri = veri.strip().split(",")
            oda_no = oda_bilgileri[0]
            oda_tipi = oda_bilgileri[1]
            fiyat = int(oda_bilgileri[2])
            rezerve = oda_bilgileri[3]
            print(f"Oda No: {oda_no}\nOda Tipi: {oda_tipi}\nFiyat: {fiyat} TL\nRezerve Durumu: {rezerve}\n")

def oda_ekstra(oda_no):
    ekstra_fiyatlari = {"jakuzi": 500, "manzara" : 800, "kuvet": 200}
    with open("otel_verileri.txt", "r") as dosya:
        veriler = dosya.readlines()
        odalar = []
        toplam = 0
        for veri in veriler:
            oda_bilgileri = veri.split(",")
            odalar.append(oda_bilgileri[0])

    for i in odalar:
        if i == oda_no:
            print("Ekstra oda ozelliklerimizin fiyatlari su sekildedir:")
            for k in ekstra_fiyatlari:
                print(k, ekstra_fiyatlari[k])
            jakuzi = input("jakuzili oda ister misiniz:(E/H)")
            j = jakuzi.upper()
            if j == "E":
                toplam += 500
            manzara = input("manzarali oda ister misiniz:(E/H)")
            m = manzara.upper()
            if m == "E":
                toplam += 800
            kuvet = input("kuvetli oda ister misiniz:(E/H)")
            k = kuvet.upper()
            if k == "E":
                toplam += 200

    oda_guncelle(oda_no, eklenecekMiktar=toplam)

def menu():

    while True:

        print("------ OTEL OTOMASYONUNA HOSGELDİNİZ ------")
        print("1. Oda Ekle")
        print("2. Oda Ara")
        print("3. Oda Güncelle")
        print("4. Oda Sil")
        print("5. Odaya Ekstralari icin Seçin")
        print("6. Tum Odalari Gor")
        print("7. Çıkış")
        secim = input("İstenilen islemi giriniz(1-7):")

        if secim == "7":
            print("cikis yaptiniz.")
            break

        elif secim =="2":
            oda_no = input("aranacak oda numarasini giriniz:")
            oda_ara(oda_no)

        elif secim == "1":
            oda_no = input("Oda numarası giriniz:")
            oda_tipi = input("Oda tipini giriniz (tek, cift, kral, aile, suit, dubleks):")
            fiyat = input("Odanin ucretini giriniz:")
            rezerve = input("Rezervelik durumu(True,False):")
            oda_ekle(oda_no,oda_tipi,fiyat,rezerve)

        elif secim == "4":
            oda_no = input("silmek istediginiz oda numarasini giriniz:")
            oda_sil(oda_no)

        elif secim == "3":
            oda_no = input("Güncellenecek Oda Numarası: ")
            oda_tipi = input("Yeni Oda Tipi: ")
            fiyat = input("Yeni Fiyat: ")
            rezerve = input("Yeni Rezerve Durumu (True/False): ")
            oda_guncelle(oda_no, oda_tipi, fiyat, rezerve)

        elif secim == "6":
            tum_odalar()

        elif secim == "5":
            oda_no = input("Ekstra ozellik eklemek istediginiz oda numarasini giriniz:")
            oda_ekstra(oda_no)

menu()



