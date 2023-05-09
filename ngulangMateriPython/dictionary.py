import os
os.system("cls")

data = {
    "nama":"Ali",
    "umur":19
}

print(data)

# ambil data
print(data["nama"])
print(data["umur"])

print(data.get("nama"))
print(data.get("umu","mo cari apa masseehh"))

# ubah data
data["nama"] = "Ali ganteng"
print(data)

data.update({"nama":"ALi gantengg abisss"})
print(data)

data.update({"hobby":"Ngodingg"})
print(data)

data["cita-cita"] = "pen sukses dari hasil jerit payah ngoding gw dan sholat gw"
print(data)

# loop dictionary
nama = {
    "nama":"Gerry",
    "umur":"sudah di surga"
}

hasil = data.keys()
print(hasil)

for i in nama.keys():
    print(nama.get(i))

hasil = data.values()
print(hasil)

for i in nama.values():
    print(i)

hasil = data.items()
print(hasil)

for i in nama.items():
    print(i)

for key,values in nama.items():
    print(f"key = {key} values = {values}")

from collections import Counter

angka = [10,1,10,5,1,10,5,1,5,3,2,10,5,3,4,10,5,4,1,6,7,8,9,10,1,1,4]

hasil = Counter(angka)
print(hasil)

print(hasil.get(10))