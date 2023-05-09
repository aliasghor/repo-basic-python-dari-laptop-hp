# lambda function
import os
os.system("cls")

def kuadrat(angka):
    return print(f"hasil = {angka**2}")

kuadrat(3)

# lambda function
kuadrat = lambda angka:angka**2
print(f"hasil dari lambda function {kuadrat(3)}")

pembagian = lambda angka:angka/0.5
print(f"hasil pembagian = {pembagian(10)}")

# kegunaan
dataList = ["Mogi","Gerry","Sparky"]

def data(nama):
    return len(nama)

dataList.sort(key=list)
print(f"sorted list panjang = {dataList}")

# sort pake lambda
dataList = ["Mogi","Gerry","Sparky"]
dataList.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {dataList}")

# filter
lebihDari5 = [1,2,3,4,5,6,7,8,9,10]

def lebih(angka):
    return angka > 5

hasil = list(filter(lebih,lebihDari5))
print(f"hasil data filter pake function biasa = {hasil}")

# filter pake lambda
hasil = list(filter(lambda x:x>5,lebihDari5))
print(f"hasil filter data pake lambda = {hasil}")

# filter ganjil genap pake lambda
angka = [0,1,2,3,4,5,6,7,8,9,10,11,100,999,1000]
hasil = list(filter(lambda x:(x%2==1),angka))
print(f"filter ganjil genap pake lambda = {hasil}")

# anonymous function
def pangkat(x):
    return lambda angka:angka**x

hasil = pangkat(2)
print(f"hasil = {hasil(8)}")