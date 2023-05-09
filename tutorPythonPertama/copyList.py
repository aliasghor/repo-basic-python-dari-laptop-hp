# teknik menduplikasi list

a = ["Ali","Ganteng","Bangett"]
print(f"a = {a}")
b = a
print(f"b = {b}")

# merubah member dari a

# ini akan merubah kedua list

a[1] = "gerry"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres kedua list

print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# menduplikasi list dengan copy

pembatas = "menduplikasi list dengan copy".center(87,"=")
print(pembatas)

c = a.copy()
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[1] = "Gantengg"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")