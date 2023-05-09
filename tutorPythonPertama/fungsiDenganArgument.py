import os
os.system("cls")

def ali(ali):
    print(f"Alii ganntenggg gkk??? {ali}")

ali("Iyalahhh masaihh nanya aee eluuu")

def bagi(x,y):
    hasil = x / y
    print(f"{x} dibagi {y} = {hasil}")

bagi(100,2)

def gerry():
    nama = ["Gerry","Mogi","Sparky"]
    for i in nama:
        print(f"nama tikus = {i}")

gerry()

def gerry(nama):
    nama[2] = "Gerard"

    dataNama = nama.copy()
    for i in dataNama:
        print(f"nama = {i}")

anggota = ["Gerry","Mogi","Sampi","Ali"]

gerry(anggota)
print(anggota[2])