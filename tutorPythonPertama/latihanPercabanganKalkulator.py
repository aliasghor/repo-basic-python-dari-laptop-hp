angka1 = float(input("Masukan angka pertama = "))
operator = input("operator(+,-,x,/) : ")
angka2 = float(input("Masukan angka kedua = "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka1 * angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasilnya adalah {hasil}")
else :
    print("operator yg anda masukan salah")
print("Akhir dari program")