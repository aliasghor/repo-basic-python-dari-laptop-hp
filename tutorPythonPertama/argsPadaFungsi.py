import os
os.system("cls")

def num(*angka):
    output = 0
    for i in angka:
        output += i

    return output

hasil = num(100,100,200)
print(f"hasil = {hasil}")

def jumlah(x,y,*j):
    return x,y,j

hasil = jumlah(1,1,[1,2,3,4,5,6])
print(hasil)