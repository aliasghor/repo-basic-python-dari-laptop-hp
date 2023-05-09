# operator dictionary

data = {
    "Gerry":"Gery",
    "Mogi":"Mogi"
}
# panjang data dictionary
LENDICT = len(data)
print(f"panjang dari dictionary = {LENDICT}")

# cek key exist
KEY = "Muchin"
CHECKKEY = KEY in data
print(f"apakah {KEY} ada di dictionary? = {CHECKKEY}")

# akses value (read) dengan get
print(data["Gerry"])
print(data.get("Gerry"))
print(data.get("Damar","Mo cari apa massehh"))

# update data
data["Gerry"] = "Gerry ganteng"
print(data)

# nambah data
data["Ali"] = "Ali ganteng"
print(data)

# nambah data gunakan update
data.update({"Gerry":"Gerry ganteng"})
print(data)

# delete data
del data["Gerry"]
print(data)