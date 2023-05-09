dataA = ["Ali","Gerard","Muchsin"]
print(dataA)

dataB = dataA
print(dataB)

print(f"addres a = {hex(id(dataA))}")
print(f"addres b = {hex(id(dataB))}")

dataC = dataA.copy()
print(f"a = {hex(id(dataA))}")
print(f"b = {hex(id(dataB))}")
print(f"c = {hex(id(dataC))}")

dataC[1] = "Diki"
print(f"data yg blom ke copy = {dataA}")
print(f"data yg blom ke copy = {dataB}")
print(f"data yg sudah ke copy = {dataC}")

pembatas = "Pembatas".center(63,"=")
print(pembatas)
num = [1,3,2,4,6,5,8,7,10,9]
print(num)
num2 = num
print(num2)

num[-1] = 11
num.sort()
print(f"num pertama = {num}")
print(f"num kedua = {num2}")

num3 = num.copy()
print(f"num pertama = {hex(id(num))}")
print(f"num kedua = {hex(id(num2))}")
print(f"num ketiga = {hex(id(num3))}")

num3[-1] = 9
print(f"num pertama = {num}")
print(f"num kedua = {num2}")
print(f"num ketiga = {num3}")