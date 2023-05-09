import os
os.system("cls")

# lebar = int(input("Masukan nilai lebar: "))
# panjang = int(input("Masukan nilai panjang: "))

# luas = panjang * lebar
# keliling = 2*(panjang + lebar)

# print(f"Hasil perhitungan luas = {luas}")
# print(f"Hasil perhitungan keliling = {keliling}")

def rumus():
    lebar = int(input("Masukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))
    return lebar,panjang

def luas(lebar,panjang):
    return lebar * panjang

def keliling(lebar,panjang):
    return 2*(lebar + panjang)

while True:
    lebar,panjang = rumus()
    LUAS = luas(lebar,panjang)
    KELILING = keliling(lebar,panjang)

    print(f"hasil perhitungan luas = {LUAS}")
    print(f"hasil perhitungan keliling = {KELILING}")

    lanjut = input("Mo lanjut apa kgk??? (Y/N) ")
    if lanjut == "N":
        break

print("Makasih telah mencoba")