name = {
    "Sampi":"Sampi",
    "Gerry":"Gerry",
    "Mogi":"Mogi"
}

nama = name.copy()
print(nama)
print(name)

nama["Ali"] = "Ali ganteng"
print(f"nama sudah dicopy {nama}")
print(f"nama blom dicopy {name}")

# pop dictionary
sampi = nama.pop("Sampi")
print(f"data sebelum di pop = {nama}")
print(f"data sesudah di pop = {sampi}")

# pop item dictionary
mogi = nama.popitem()
print(f"data sebelum di popitem = {nama}")
print(f"data sesudah di popitem = {mogi}")