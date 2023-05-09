# date and time latihan
import datetime as dt

# hariIni = dt.date.today()
# print(f"hari ini adalah hari : {hariIni:%A}")

# pembatas = "pembatas".center(68,"=")
# print(pembatas)

# tanggalLahir = dt.date(2003,6,6)
# tanggalLahir = f"""
# eug lahir di tahun : {tanggalLahir}
# dan eug lahir di hari : {tanggalLahir:%A}
# """
# print(tanggalLahir)

# pembatas = "pembatas".center(68,"=")
# print(pembatas)

# print("masukan tahun lahir,bulan dan hari anda")
# tanggal = int(input("Tanggal: "))
# bulan = int(input("Bulan: "))
# tahun = int(input("Tahun: "))
# hasil = dt.date(tahun,bulan,tanggal)
# print(f"Antum lahir di tahun: {tahun}, bulan: {bulan}, tanggal {tanggal}, ")
# print(f"dan antum lahir di hari: {hasil:%A}")
# pembatas = "pembatas".center(68,"=")
# print(pembatas)

# tahun = int(input("Silahkan masukan tahun sekarang : "))
# lahir = int(input("silahkan masukan tahun lahir : "))
# hasil = tahun - lahir
# print(f"umur anda sekarang adalah {hasil}")

tanggalLahir = dt.date(2003,6,6)
lahir = f"""
eug lahir di tanggal: {tanggalLahir}
dan eug lahir di hari: {tanggalLahir:%A}
"""
print(lahir)

print("masukan tanggal lahir bulan lahir dan tahun lahir")
tanggal = int(input("masukan tanggal lahir antum: "))
bulanLahir = int(input("masukan bulan lahir antum: "))
tahunLahir = int(input("Masukan tahun lahir antum: "))
hasil = dt.date(tahunLahir,bulanLahir,tanggal)
print(f"antum lahir di tahun {tahunLahir}, dan bulan {bulanLahir}, dan tanggal {tanggal}")
print(f"dan antum lahir di hari {hasil:%A}")

tanggalLahir = dt.date(2003,5,31)
lahir = f"""
eug lahir di tanggal: {tanggalLahir}
dan eug lahir di hari: {tanggalLahir:%A}
"""
print(lahir)