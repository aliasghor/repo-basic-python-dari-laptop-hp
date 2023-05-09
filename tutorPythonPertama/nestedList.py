data1 = [1,2]
data2 = [3,4]
print(data1)
print(data2)
dataList = [5,6,7,8,9,10]
print(dataList)
kumpul = [data1,data2,dataList,11,12]
print(f"ini array didalem array {kumpul}")

# contoh penggunaan
pembatas = "pembatas".center(87,"=")
print(pembatas)

nama1 = ["Ali","umur: 20","jurusan: computer science"]
nama2 = ["Gerard","umur: 19","jurusan: management"]
nama3 = ["Muchsin","umur: 19","jurusan: computer management"]

listNama = [nama1,nama2,nama3]
print(listNama)

for i in listNama:
    print(f"nama\t: {i[0]}")
    print(f"umur\t: {i[1]}")
    print(f"jurusan\t: {i[2]}")

# dengan refrenece
listCopy = listNama.copy()
print(f"peserta = {listCopy}")
nama1[0] = "Gerry"
print(f"peserta = {listCopy}")
print(f"peserta = {listNama}")