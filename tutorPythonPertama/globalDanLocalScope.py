import os
os.system("cls")

nama = ["Gerry","Mogi","Sparky"]

def fungsi():
    print(f"nama = {nama}")

fungsi()

angka = 0
nama = "Gerry"

def hasil(nilai):
    angka = nilai
    global nama

print(f"angka = {angka,nama}")
hasil(1)
print(f"angka = {angka,nama}")