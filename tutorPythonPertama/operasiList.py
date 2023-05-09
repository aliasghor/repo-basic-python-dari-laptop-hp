data = [1,5,4,6,7,8,3,4,5,8,9]
print(f"data angka = {data}")

# cound data
jumlahData4 = data.count(4)
jumlahData5 = data.count(5)
print(f"jumlah angka 4 = {jumlahData4} jumlah angka 5 = {jumlahData5}")

# mengambil index
data = ["Ali","Ganteng","Banget"]
dataIndex = data.index("Ali")
print(dataIndex)

# mengurutkan list
data = [1,4,3,2,5,7,6,8,10,9]
print(f"data angka sebelum sort = {data}")
data.sort()
print(f"data angka setelah di sort = {data}")

# membalikan angkanya

data.reverse()
print(f"data angka setelah di reverse = {data}")
