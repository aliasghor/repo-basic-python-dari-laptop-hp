import datetime as dt
import os
os.system("cls")

def taro():
    tahun = int(input("Masukan tahun lahir antum: "))
    bulan = int(input("Masukan bulan lahir antum: "))
    hari = int(input("Masukan tanggal lahir antum: "))
    return tahun,bulan,hari

def lahir(tahun,bulan,hari):
    return dt.datetime(tahun,bulan,hari)

while True:
    TAHUN,BULAN,LAHIR = taro()
    hasil = lahir(TAHUN,BULAN,LAHIR)

    print(f"antum lahir di tahun {hasil} dan antum lahir di hari {hasil:%A}")

    keluar = input("Mo keluar apa kagak??? (Y/N) ")

    if keluar == "Y":
        break