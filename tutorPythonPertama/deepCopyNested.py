data1 = [1,2]
data2 = [3,4]

data3 = [data1,data2,10]
data3Copy = data3.copy()
print(f"data = {data3}")
print(f"data copy = {data3Copy}")

# mengambil data

data = data3[0][0]
print(f"data = {data}")

# address semuanya

print(f"address asli = {hex(id(data3))}")
print(f"address copy = {hex(id(data3Copy))}")

print("address dari member 1")
print(f"address asli = {hex(id(data3[0]))}")
print(f"address copy = {hex(id(data3Copy[0]))}")

data3[1][0] = 5
data3[2] = 9
print(f"data = {data3}")
print(f"data copy = {data3Copy}")

# gunakan deep copy

from copy import deepcopy

data3 = [data1,data2,10]
data3DeepCopy = deepcopy(data3)

print(f"address asli = {hex(id(data3))}")
print(f"address deep copy = {hex(id(data3DeepCopy))}")

print(f"address asli = {hex(id(data3[0]))}")
print(f"address deep copy = {hex(id(data3DeepCopy[0]))}")

data3[1][0] = 30
print(f"data = {data3}")
print(f"data copy = {data3Copy}")
print(f"data deep copy = {data3DeepCopy}")