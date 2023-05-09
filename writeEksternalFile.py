import os
os.system("cls")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Ali ganteng abiss\n")

# append
with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("Ali ganteng abiss\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("Ali ganteng abiss gillee\n")

# mode r+
with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.write("baris ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("gerry")