import os
os.system("cls")

def fungsi(**gerry):
    return gerry["nama"]

print(fungsi(nama="Gerry",umur=19))

# studi kasus

def math(*mogi,**gerry):
    output = 0
    if gerry["option"] == "tambah":
        for i in mogi:
            output += i
    elif gerry["option"] == "kali":
        output = 1
        for i in mogi:
            output *= i
    else:
        print("tidak ada operasi")
    return output


hasil = math(1,2,3,4,5,6,option="tambah")
print(f"hasil jumlah = {hasil}")

hasil = math(1,2,3,4,5,6,option="kali")
print(f"hasil perkalian = {hasil}")