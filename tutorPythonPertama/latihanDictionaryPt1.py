# fromkeys
import datetime as dt
import os
os.system("cls")
namaMahasiswa = {
    "nama":"nama",
    "umur":0,
    "Lahir":dt.datetime(1111,1,1)
}

dataMahasiswa = {}

mahasiswa = dict.fromkeys(namaMahasiswa.keys())
mahasiswa["nama"] = input("Silahkan masukan nama: ")
mahasiswa["umur"] = int(input("Silahkan masukan umur antum: "))
tahun = int(input("Sialhkan masukan tahun lahir antum: "))
bulan = int(input("Sialhkan masukan bulan lahir antum: "))
tanggal = int(input("Sialhkan masukan tanggal lahir antum: "))
mahasiswa["Lahir"] = dt.datetime(tahun,bulan,tanggal)