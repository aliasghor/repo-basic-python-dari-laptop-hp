import os
os.system("cls")

data = [0,1,2,3,4,5,6,7,8,9,10]

for i in data:
    print(f"data = {i}")

data = [0,1,2,3,4,5,6,7,8,9,10]
panjang = len(data)

for i in range(panjang):
    print(f"data = {data[i]}")
    if data[i] == 5:
        break

data = [0,1,2,3,4,5,6,7,8,9,10]
panjang = len(data)
i = 0

while i < panjang:
    print(f"hasil while loop = {data[i]}")
    i += 1

# list comprehension
data = [0,1,2,3,4,5,6,7,8,9,10]
[print(f"loop pake list comprehension = {i}") for i in data]

# list enumerate
data = [0,1,2,3,4,5,6,7,8,9,10]

for index,data in enumerate(data):
    print(f"index = {index} data = {data}")