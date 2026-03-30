import time

C_RESET = '\033[0m'
C_CYAN = '\033[96m'
C_GREEN = '\033[92m'
C_YELLOW = '\033[93m'
C_RED = '\033[91m'
C_MAGENTA = '\033[95m'
C_BOLD = '\033[1m'
#Konsol renklendirme icin renk kodlari yapay zeka ile yapilmistir.

# 1-Metni tersine ceviren sinif.
class MetinTersCevirici:
    def __init__(self, metin):
        self.metin = metin

    def ters_cevir(self):
        return self.metin[::-1]


# 2- Ters metni kullanarak sezar sifresi yapan sinif.
class SezarSifreleyici:
    def __init__(self, metin, anahtar):
        self.metin = metin
        self.anahtar = anahtar

    def sifrele(self):
        sifreli_metin = ""
        for harf in self.metin:
            # Bosluk ve noktalama isaretlerini atla.
            if harf.isalpha():
                baslangic = ord('A') if harf.isupper() else ord('a')

                sifreli_harf = chr((ord(harf) - baslangic + self.anahtar) % 26 + baslangic)
                sifreli_metin += sifreli_harf
            else:
                sifreli_metin += harf
        return sifreli_metin


# 3- Sifre cozucu sinif.
class SifreCozucu:
    def __init__(self, sifreli_metin):
        self.sifreli_metin = sifreli_metin

    def coz(self):
        print(f"{C_YELLOW}Ele Geçirilen Şifreli Metin: {self.sifreli_metin}{C_RESET}")
        print(f"{C_CYAN}{C_BOLD}Ters Metin      \t\t            Düz Metin{C_RESET}")
        print(f"{C_CYAN}{'-' * 60}{C_RESET}")

        for key in range(26):
            cozulmus_ters_metin = ""
            for harf in self.sifreli_metin:
                if harf.isalpha():
                    baslangic = ord('A') if harf.isupper() else ord('a')
                    cozulmus_harf = chr((ord(harf) - baslangic - key) % 26 + baslangic)
                    cozulmus_ters_metin += cozulmus_harf
                else:
                    cozulmus_ters_metin += harf

            duz_metin = cozulmus_ters_metin[::-1]

            print(f"{C_MAGENTA}Key {key:<4}{C_RESET} : {C_YELLOW}{cozulmus_ters_metin:<25}{C_RESET} : {C_GREEN}{duz_metin}{C_RESET}")
            time.sleep(0.1)


print(f"{C_CYAN}{C_BOLD}ŞİFRELEME SÜRECİ{C_RESET}")
girilen_metin = input(f"{C_MAGENTA}Lütfen bir metin giriniz:\n{C_RESET}")

tersleyici = MetinTersCevirici(girilen_metin)
ters_metin = tersleyici.ters_cevir()
print(f"{C_YELLOW}Ters Çevrilmiş hali:{C_RESET}")
print(f"{C_GREEN}{ters_metin}{C_RESET}")

anahtar = int(input(f"{C_MAGENTA}Lütfen öteleme sayısını giriniz:\n{C_RESET}"))
sifreleyici = SezarSifreleyici(ters_metin, anahtar)
sifreli_metin = sifreleyici.sifrele()
print(f"{C_YELLOW}Sezar ile Şifrelenmiş hali:{C_RESET}")
print(f"{C_GREEN}{sifreli_metin}{C_RESET}")

print(f"\n{C_CYAN}{C_BOLD}ŞİFRE ÇÖZME SÜRECİ{C_RESET}")
cozucu = SifreCozucu(sifreli_metin)
cozucu.coz()