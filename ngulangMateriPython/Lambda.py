import os
os.system("cls")

hasil = lambda x:x*2
print(f"hasil = {hasil(2)}")

hasil = lambda x,y:x**y
print(f"hasil = {hasil(10,2)}")

# list filter angka
angka = [0,1,2,3,4,5,6,7,8,9,10]
hasil = list(filter(lambda x:(x < 5), angka))
print(f"hasil filter angka lebih kecil dari 5 = {hasil}")

angka = [0,1,2,3,4,5,6,7,8,9,10]
hasil = list(filter(lambda x:(x%2==0), angka))
print(f"hasil angka genap = {hasil}")

# anonymous function
def angka(y):
    return lambda x:x**y

hasil = angka(2)
print(f"hasil pangkat 2 dari anonymous function = {hasil(5)}")

print((lambda x,y:x**y)(10,2))

contoh = [1,2,3,4,5,6]

print(list(filter(lambda x:(x < 3), contoh)))