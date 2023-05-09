list = [6,5,4,3,2,1]

for i in list:
    print(f"angka = {i}")

peserta = ["Gerry","Mogi","Sparky"]

for i in peserta:
    print(f"nama = {i}")

# for loop dan range
pembatas = "Pake for loop in range".center(68,"=")
print(pembatas)
angka = [1,3,2,6,5,4]

panjang = len(angka)

for i in range(panjang):
    print(f"angka = {angka[i]}")

# pake while
pembatas = "Pake while".center(68,"=")
print(pembatas)
angka = [1,3,2,6,5,4]

panjang = len(angka)
i = 0

while i < panjang:
    print(f"angka = {angka[i]}")
    i += 1

# list comprehension
pembatas = "Pake list comprehension".center(68,"=")
print(pembatas)

data = ["Gerry",1,True,"Mogi"]

[print(f"data = {i}") for i in data]

angka = [1,2,3,4,5]
angkaKuadrat = [i**2 for i in angka]
print(angkaKuadrat)

# enumerate
pembatas = "Pake enumerate".center(68,"=")
print(pembatas)

dataList = ["Gerry",1,True,"Mogi"]

for index,data in enumerate(dataList):
    print(f"index = {index}, data = {data}")