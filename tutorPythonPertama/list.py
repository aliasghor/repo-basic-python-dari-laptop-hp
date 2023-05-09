dataAngka = [1,2,3]
print(dataAngka)

dataStr = ["Ali","ganteng","abiss"]
print(dataStr)

kumpulanData = ["Ali",False,True,1,2,3,["Gerry"]]
print(kumpulanData)

# cara laen nge print list

data = range(0,10,2)
dataList = list(data)
print(dataList)

# list comprenhesion

data = [i*2 for i in range(0,10)]
print(data)

listPakeFor = [i for i in range(0,10) if i != 5]
print(listPakeFor)

listPakeFor = [i for i in range(0,10) if i%2 == 1]
print(listPakeFor)