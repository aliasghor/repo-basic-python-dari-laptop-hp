data1 = [1,2]
data2 = [3,4]
dataGabungan = [data1,data2,1900]
print(dataGabungan)
dataCopy = dataGabungan.copy()
print(dataCopy)

print(f"address dari data gabungan {hex(id(dataGabungan))}")
print(f"address dari data gabungan {hex(id(dataCopy))}")

dataGabungan[1][0] = 5
print(dataGabungan)
print(dataCopy)

from copy import deepcopy

dataDeep = deepcopy(dataGabungan)
dataGabungan[1][1] = 100 
print(f"address dari data gabungan {hex(id(dataGabungan))}")
print(f"address dari data gabungan {hex(id(dataCopy))}")
print(f"address dari data gabungan {hex(id(dataDeep))}")
print(dataGabungan)
print(dataCopy)
print(dataDeep)