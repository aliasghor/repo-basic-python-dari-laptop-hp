data = ["Ali","ganteng","Banget"]
data0 = data
print(data0)

panjangData = len(data)
print(panjangData)

nama = "Ali ganteng"
panjangData = len(nama)
print(panjangData)

pembatas = "Manipulasi data list".center(87,"=")
print(pembatas)

data = ["Ali","Gerard","Muchin"]
print(f"data sebelum ditambah {data}")

data.insert(1,"Radhi")
print(f"data setelah ditambah {data}")

data.append("Gerry")
print(f"data ditambah lagi {data}")

dataBaru = ["Mogi","Sampi"]
data.extend(dataBaru)
print(f"data ditambah lagi {data}")

# merubah data
pembatas = "Merubah data".center(87,"=")
print(pembatas)

data[1] = "Rodchi"
print(f"data yg sudah ke rubah {data}")

# delete data
pembatas = "Delete data".center(87,"=")
print(pembatas)

data.remove("Mogi")
print(f"data yg sudah ke remove {data}")

# remove data paling belakang
pembatas = "Remove data paling belakang".center(87,"=")
print(pembatas)

data.pop()
print(f"data yg terakhir akan hilang {data}")