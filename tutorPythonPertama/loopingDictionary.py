name = {
    "Ali":"Ali ganteng",
    "Gerry":"Gerry",
    "Mogi":"Mogi"
}

# looping dictionary
for i in name:
    print(i)

# operatur untuk ambil item
keys = name.keys()
print(keys)

for i in name.keys():
    print(name.get(i))

value = name.values()
print(value)

for i in name.values():
    print(i)

item = name.items()
print(item)

for i in name.items():
    print(i)

for key,value in name.items():
    print(f"key = {key}, value = {value}")