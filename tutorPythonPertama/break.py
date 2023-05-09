angka = 0
while angka < 5:
    angka += 1
    print(f"angka skrg = {angka}")
    if angka == 3:
        print("gerry")
        break
    print("yombekk")
print("cukuupp massehh")

masukanAngka = int(input("Masukan angka: "))
angka = 0

while angka < masukanAngka:
    angka += 1
    print(f"count = {angka}")
    if angka == masukanAngka:
        print("yombekk")
        break
print("oopppp")

masukanAngka = int(input("Masukan angka bilangan ganjil dan genap: "))

if masukanAngka %2 == 0:
    print(f"{masukanAngka} adalah bilangan genap")
else:
    print(f"{masukanAngka} adalah bilangan ganjil")


