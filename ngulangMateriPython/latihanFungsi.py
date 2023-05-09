import os
os.system("cls")
import datetime as dt

def rumus():
    lebar = int(input("Masukan lebarnya: "))
    panjang = int(input("Masukan panjangnya: "))
    return lebar,panjang

def angka(lebar,panjang):
    return lebar * panjang

def hasil(lebar,panjang):
    return 2*(lebar + panjang)

while True:
    LEBAR,PANJANG = rumus()
    ANGKA = angka(LEBAR,PANJANG)
    HASIL = hasil(LEBAR,PANJANG)

    print(f"hasil luas = {ANGKA}")
    print(f"hasil keliling = {HASIL}")

    keluar = input("Mo keluar apa kgk (Y/N)?: ")
    if keluar == "Y":
        break
    elif keluar == "N":
        continue
    else:
        print("Nulis apaan cok")
        break

def masukan():
    tahun = int(input("Masukan tahun lahir antum: "))
    bulan = int(input("Masukan bulan lahir antum: "))
    lahir = int(input("Masukan tanggal lahir antum: "))
    return tahun,bulan,lahir

def lahir(tahun,bulan,lahir):
    return dt.datetime(tahun,bulan,lahir)

while True:
    TAHUN,BULAN,LAHIR = masukan()
    LAHIR = lahir(TAHUN,BULAN,LAHIR)

    print(f"Antum lahir di tahun {LAHIR} dan antum lahir di hari {LAHIR:%A}")

    keluar = input("Mo keluar apa kagak??? (Y/N): ")

    if keluar == "Y":
        print("Makasihh ngabb")
        break
    elif keluar == "N":
        continue
    else:
        print("Ngomong apaan sih cokk???")
        break
