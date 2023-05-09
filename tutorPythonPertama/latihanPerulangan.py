# latiha perulangan membuat segitiga

sisi = 10
pembatas = "menggunakan for".center(87,"=")
print(pembatas)
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

pembatas = "menggunakan while".center(87,"=")
print(pembatas)

count = 1
while count:
    print("*"*count)
    count += 1
    if count > sisi:
        break

pembatas = "mengambil ganjil saja".center(87,"=")
print(pembatas)

count = 1
sisi = 10
while count:
    if count%2 == 1:
        print("*"*count)
        count += 1
    else:
        count +=1
        continue
    if count > sisi:
        break