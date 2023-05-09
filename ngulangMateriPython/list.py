import os
os.system("cls")

# gerry = [0,1,2,3,4,5,6,7,8,9,10]

# gerry[1] = "Gerry"
# print(gerry)

# data = range(0,10,5)

# hasil = list(data)
# print(hasil)

# [print(i) for i in range(10) if i%2==0]

# output = 1

# while output <= 10:
#     print(f"angka = {output}")
#     output += 1

# output = [1,2,3,4,5,6,7,8,9,10]
# panjang = len(output)
# i = 0

# while i <= panjang:
#     print(f"i = {i}")
#     i += 1


# list = ["Gerry","Mogi","Sparky"]
# print(list)

# list[0] = "Ali"
# print(list)

# list.insert(2,"Ali ganteng")
# print(list)

# list.append("Gerry")
# print(list)

# data = ["Gerard","Muchsin","Diki"]
# list.extend(data)
# print(list)

# list.remove("Ali")
# print(list)

# angka = [0,0,6,4,6,5,0,8,6,9,10,10,9,6,7,]

# angka0 = angka.count(0)
# print(f"banyak angka 0 = {angka0}")

# angka6 = angka.count(6)
# print(f"banyak angka 0 = {angka6}")

# list = [10,5,9,7,8,4,2,3,1,6]
# list.sort()
# print(f"sorted list = {list}")

# list.reverse()
# print(f"reversed list = {list}")

# nama = ["Gerry","Mogi","Sparky"]
# hasil = nama.index("Gerry")
# print(f"index gerry berada pada = {hasil}")

# hasil = nama.index("Sparky")
# print(f"index sparky berada pada = {hasil}")

# a = ["Gerry","Mogi","Sparky"]
# print(f"a = {a}")
# b = a
# print(f"b = {b}")

# a[2] = "Ali ganteng"
# b.sort()
# print(f"a = {a}")
# print(f"b = {b}")

# print(f"addres a = {hex(id(a))}")
# print(f"addres b = {hex(id(b))}")

# c = a.copy()
# print(f"addres c = {hex(id(c))}")

# a[0] = "Ali ganteng"
# c[0] = "Mogi"
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")

# data1 = [1,2]
# data2 = [3,4]

# hasil = [data1,data2]
# print(f"nested list = {hasil}")

# nama1 = ["Gerry",4,"Laki-Laki"]
# nama2 = ["Mogi",3,"perempuan"]
# nama3 = ["sampi",2,"perempuan"]

# hasil = [nama1,nama2,nama3]
# print(f"nama tikus = {hasil}")

# for index,data in enumerate(hasil):
#     print(f"index ke = {index} data = {data}")
#     print(f"index ke = {index} umur = {data[1]}")
#     print(f"index ke = {index} jenis-kelamin = {data[2]}")

# listBuku = []

# while True:
#     print("Masukan data buku")
#     judul = input("Judul buku:\t ")
#     penulis = input("Nama buku:\t ")

#     bukuBaru = [judul,penulis]
#     listBuku.append(bukuBaru)
    
#     print("No.\t |\t Judul\t\t|\tpenulis\t\t\t penulis")
#     for index,buku in enumerate(listBuku):
#         print(f"{index}\t\t {buku[0]}\t\t\t {buku[1]}")

#     keluar = input("Mo cabut apa kagak?? (Y/N) ")
#     if keluar == "Y":
#         break