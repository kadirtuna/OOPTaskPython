class Canlılar():
    def __init__(self, ad, sınıf, hareketKabiliyeti, beslenme, solunum, üreme, ölüm):
        self.ad = ad
        self.sınıf = sınıf
        self.hareketKabiliyeti = "Var" if hareketKabiliyeti == True else "Yok"
        self.beslenme = beslenme
        self.solunum = solunum
        self.üreme = üreme
        self.ölüm = ölüm

    def bilgileriniYazdır(self):
        print(f"{self.ad} türünden bu canlının özellikleri şunlardır;\nSınıfı : {self.sınıf}\nHareket Kabiliyeti : {self.hareketKabiliyeti}\nBeslenme şekli : {self.beslenme}\nSolunum Şekli : {self.solunum}\nÜreme Şekli : {self.üreme}\nÖlüm Yaşı : {self.ölüm}\n\n")


class Hayvanlar(Canlılar):
    hareketKabiliyeti = True  # A noktasından B noktasına hareket edebilme özelliği
    sınıf = "Hayvan"

    def __init__(self, tür, beslenme, solunum, üreme, ölüm):
        Hayvanlar.beslenmeControl(self, beslenme)
        Hayvanlar.solunumControl(self, solunum)
        super().__init__(tür,  Hayvanlar.sınıf, Hayvanlar.hareketKabiliyeti, beslenme, solunum, üreme, ölüm)

    def beslenmeControl(self, beslenme):
        while 1:
            if beslenme == "Etçil":
                break
            elif beslenme == "Otçul":
                break
            elif beslenme == "Hepçil":
                break
            else:
                beslenme = input(f"Beslenmeyi \"{beslenme}\" olarak girdin.\nBir canlının beslenme şekli sadece \"Etçil\", \"Otçul\"veya \"Hepçil\" olabilir. Beslenme şeklini tekrar giriniz : ")

    def solunumControl(self, solunum):
        solunumCesitleri = ["Deri", "Solungaç", "Trake", "Akciğer"]
        if solunum in solunumCesitleri:
            pass
        else:
            print(f"Solunum \"{solunum}\" olarak girdin.\nBir canlının solunum şekli sadece")
            for index, i in enumerate(solunumCesitleri):
                print(f"#{index + 1} - {i}")
            solunum = input("olabilir. Solunum şeklini tekrar harflerle yazarak giriniz : ")

    def üremeControl(self, üreme):
        üremeCesitleri = ["Eşeyli", "Eşeysiz"]
        if üreme in üremeCesitleri:
            pass
        else:
            print(f"Üreme'yi \"{üreme}\" olarak girdin.\nBir canlının üreme şekli sadece")
            for index, i in enumerate(üremeCesitleri):
                print(f"#{index + 1} - {i}")
            üreme = input("olabilir. Üreme şeklini tekrar harflerle yazarak giriniz : ")


class Bitkiler(Canlılar):
    sınıf = "Bitki"
    hareketKabiliyeti = False
    solunum = "Fotosentez"
    beslenme = "Toprak"

    def __init__(self, tür, üreme, ölüm):
        Bitkiler.üremeControl(self, üreme)
        super().__init__(tür, Bitkiler.sınıf, Bitkiler.hareketKabiliyeti, Bitkiler.beslenme, Bitkiler.solunum, üreme, ölüm)

    def üremeControl(self, üreme):
            üremeCesitleri = ["Vejetatif", "Sporla", "Bölünerek", "Tomurcuklanarak", "Yenilenerek"]
            if üreme in üremeCesitleri:
                pass
            else:
                print(f"Üreme'yi \"{üreme}\" olarak girdin.\nBir canlının üreme şekli sadece")
                for index, i in enumerate(üremeCesitleri):
                    print(f"#{index + 1} - {i}")
                üreme = input("olabilir. Üreme şeklini tekrar harflerle yazarak giriniz : ")


class Omurgalılar(Hayvanlar):  # Hayvanlar sınıfından Omurgalı Hayvanlar alt sınıfı
    üreme = "Eşeyli"

    def __init__(self, tür, beslenme, solunum, ölüm):
        super().__init__(tür, beslenme, solunum, Omurgalılar.üreme, ölüm)


class Omurgasızlar(Hayvanlar):  # Hayvanlar sınıfından Omurgasız Hayvanlar alt sınıfı
    def __init__(self, tür, beslenme, solunum, üreme, ölüm):
        super().__init__(tür, beslenme, solunum, üreme, ölüm)


class ÇiçekliBitkiler(Bitkiler):  # Hayvanlar sınıfından Omurgalı Hayvanlar alt sınıfı
    def __init__(self, tür, üreme, ölüm):
        super().__init__(tür, üreme, ölüm)


class ÇiçeksizBitkiler(Bitkiler):  # Hayvanlar sınıfından Omurgasız Hayvanlar alt sınıfı
    üreme = "Sporla"
    def __init__(self, tür, ölüm):
        super().__init__(tür, ÇiçeksizBitkiler.üreme, ölüm)


boncuk = Omurgalılar("Kedi", "Etçil", "Akciğer", 15)
max = Omurgalılar("Köpek", "Hepçil", "Akciğer", 10)
doru = Omurgalılar("At", "Otçul", "Akciğer", 25)
denizYıldızı = Omurgasızlar("Deniz Yıldızı", "Etçil", "Solungaç", "Eşeyli", 35)
ahtapot = Omurgasızlar("Ahtapot", "Etçil", "Solungaç", "Eşeyli", 5)
lale = ÇiçekliBitkiler("Lale", "Vejetatif", 0.5)
menekşe = ÇiçekliBitkiler("Menekşe", "Vejetatif", 0.5)
eğreltiOtu = ÇiçeksizBitkiler("Eğrelti Otu", 1)
suYosunu = ÇiçeksizBitkiler("Su Yosunu", 1)
liken = ÇiçeksizBitkiler("Liken", 1)


eğreltiOtu.bilgileriniYazdır()
max.bilgileriniYazdır()

hayvanlar = [boncuk, max, doru, denizYıldızı, ahtapot]
bitkiler = [lale, menekşe, eğreltiOtu, suYosunu, liken]


for index, hayvan in enumerate(hayvanlar):
    print(f"{index}. Hayvan;")
    hayvan.bilgileriniYazdır()

for index, bitki in enumerate(bitkiler):
    print(f"{index}. Bitki;")
    bitki.bilgileriniYazdır()
