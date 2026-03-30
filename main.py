# 1-Metni Tersine Çeviren Sınıf
class MetinTersCevirici:
    def __init__(self, metin):
        self.metin = metin

    def ters_cevir(self):
        return self.metin[::-1]


# 2- Ters metni alıp Sezar Şifrelemesi yapan sınıf
class SezarSifreleyici:
    def __init__(self, metin, anahtar):
        self.metin = metin
        self.anahtar = anahtar

    def sifrele(self):
        sifreli_metin = ""
        for harf in self.metin:
            # Boşluk veya noktalama işaretlerini atla
            if harf.isalpha():
                baslangic = ord('A') if harf.isupper() else ord('a')

                sifreli_harf = chr((ord(harf) - baslangic + self.anahtar) % 26 + baslangic)
                sifreli_metin += sifreli_harf
            else:
                sifreli_metin += harf
        return sifreli_metin


# 3- Şifre Çözücü Sınıf
class SifreCozucu:
    def __init__(self, sifreli_metin):
        self.sifreli_metin = sifreli_metin

    def coz(self):
        print(f"Ele Geçirilen Şifreli Metin: {self.sifreli_metin}")
        print("Ters Metin\t\tDüz Metin")
        print("-" * 60)

        for key in range(26):
            cozulmus_ters_metin = ""
            for harf in self.sifreli_metin:
                if harf.isalpha():
                    baslangic = ord('A') if harf.isupper() else ord('a')
                    cozulmus_harf = chr((ord(harf) - baslangic - key) % 26 + baslangic)
                    cozulmus_ters_metin += cozulmus_harf
                else:
                    cozulmus_ters_metin += harf

            # Düz Metin
            duz_metin = cozulmus_ters_metin[::-1]

            print(f"Key {key:<4} : {cozulmus_ters_metin:<25} : {duz_metin}")


print("ŞİFRELEME SÜRECİ")
girilen_metin = input("Lütfen bir metin giriniz:\n")

# 1. Aşama: Metni ters çevir
tersleyici = MetinTersCevirici(girilen_metin)
ters_metin = tersleyici.ters_cevir()
print("Ters Çevrilmiş hali:")
print(ters_metin)

anahtar = 3
sifreleyici = SezarSifreleyici(ters_metin, anahtar)
sifreli_metin = sifreleyici.sifrele()
print("Sezar ile Şifrelenmiş hali:")
print(sifreli_metin)

print("\nŞİFRE ÇÖZME SÜRECİ")
cozucu = SifreCozucu(sifreli_metin)
cozucu.coz()