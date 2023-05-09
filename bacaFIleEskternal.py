import os
os.system("cls")

file = open("data.txt",mode="r")

print(f"status read = {file.readable()}")
print(f"status write = {file.writable()}")

# baca seluruh file
# print(file.read())

# baca perbaris
print(file.readline(),end="")
print(file.readline(),end="")

# baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sdh di close = {file.closed}")
file.close()
print(f"apakah file sdh di close = {file.closed}")

# salah satu teknin buka file di python
with open("data.txt",mode="r") as file:
    content = file.read()
    print(content,end="")
    print(f"apakah file sdh di close = {file.closed}")

print(f"apakah file sdh di close = {file.closed}")
