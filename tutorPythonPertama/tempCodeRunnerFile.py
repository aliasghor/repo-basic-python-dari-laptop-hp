print("masukan tahun lahir,bulan dan hari anda")
tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: "))
tahun = int(input("Tahun: "))
hasil = dt.date(tahun,bulan,tanggal)
print(f"Antum lahir di tahun: {tahun}, bulan: {bulan}, tanggal {tanggal}, ")
print(f"dan antum lahir di hari: {hasil:%A}")