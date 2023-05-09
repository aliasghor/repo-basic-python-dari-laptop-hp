import os
os.system("cls")

def ali(nama):
    print(f"Ali gantengg {nama}")

ali("bangett")

def num(x,y):
    hasil = x**y
    return hasil

print(10 + num(8,2))



def nama(name = "Antum lupa masukin argumentnya massehh"):
    return print(f"{name}")

nama()

def angka():
    num = int(input("Silahkan masukan angka antara ganjil dan genap: "))

    if num%2 == 0:
        print(f"angka {num} adalah genap")
    else:
        print(f"angka {num} adalah ganjil")

angka()