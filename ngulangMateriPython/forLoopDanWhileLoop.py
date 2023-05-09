import os
os.system('cls')

# angka = [1,2,3,4,5]

# for i in angka:
#     if i == 3:
#         break

#     print(f" i = {i}")

# for i in range(1,5):
#     print(f"i pake range = {i}")

# # while
# print('='*20)
# print("nge loop pake while")
# print('='*20)

# angka = 0
# print(f"angka sebelum = {angka}")

# while angka < 5:
#     angka += 1
#     print(f"angka sesudah = {angka}")

# latihan loop
jumlah = 10
bintang = 1

for i in range(jumlah):
    print("*"*bintang)
    bintang += 1

jumlah = 10
bintang = 1

while True:
    print("*"*bintang)
    bintang +=1

    if bintang > jumlah:
        break