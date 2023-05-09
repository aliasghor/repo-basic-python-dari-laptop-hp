import os
os.system("cls")

def fungsi(parameter = 8):
    hasil = parameter**2
    return print(f"hasil = {hasil}")

fungsi()

# penggunaan type hints
import string

def hint(arg:string) -> string:
    nama = arg
    return nama

hasil = hint(False)
print(hasil)