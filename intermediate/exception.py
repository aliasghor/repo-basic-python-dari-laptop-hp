import os
os.system("cls")
import datetime as dt

def angka():
    angka1 = float(input("Masukan angka pertamanya: "))
    maoApa = input("Masukin pilihan berikut (+,-,*,/) ")
    angka2 = float(input("Masukan angka keduanya: "))
    
    return angka1,maoApa,angka2

def masukin(angka1,maoApa,angka2):
    try:
        if maoApa == "+":
            return angka1 + angka2

        elif maoApa == "-":
            return angka1 - angka2

        elif maoApa == "*":
            return angka1 * angka2

        elif maoApa == "/":
            return angka1 / angka2

        else:
            print("Masukin apaan cok???")

    except:
        print("Hasil pembagian dari 0 sama dengan tidak terdefinisi terimakasih")


while True:
    ANGKA1,MAOAPA,ANGKA2 = angka()
    MASUKIN = masukin(ANGKA1,MAOAPA,ANGKA2)

    print(f"hasilnya = {MASUKIN}")

    keluar = input("Mao keluar apa kagak?? (Y/N) ")

    if keluar == "Y":
        print("Makasih sudah gunain kalkulator sederhana ane")
        break


def gerry():
    tahun = int(input("Masukin tahun lahir antum: "))
    bulan = int(input("Masukin bulan lahir antum: "))
    hari = int(input("Masukin hari lahir antum: "))

    return tahun,bulan,hari

def lahir(tahun,bulan,hari):
    try:
        return dt.datetime(tahun,bulan,hari)

    except:
        print("Masukin yg benerr weiii tahun lahir bulan lahir dan hari lahirrnya jan sampee kebalik cokk!!")

while True:
    TAHUN,BULAN,HARI = gerry()
    LAHIR = lahir(TAHUN,BULAN,HARI)

    print(f"antum lahir di tahun {LAHIR} dan antum lahir di hari {LAHIR:%A}")

    keluar = input("Mao keluar apa kagak?? (Y/N) ")
    
    if keluar == "Y":
        print("Makasihh brokk")
        break

while True:
    try:
        with open("data_test.txt",'r') as file:
            print(file.read())
        break

    except:
        print("Mo cari apaa maseeh?? gw bikinin yak filenya")
        with open("data_test.txt",'w',encoding="utf-8") as file:
            file.write("File baru")
        break


# def tambah(x,y):
#     if not isinstance(x,Number) or not isinstance(y,Number):
#         raise "input pertama harus angka"
#     return x + y

# hasil = tambah(5,"5")
# print(hasil)