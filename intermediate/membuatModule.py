import os
os.system("cls")
import time
start = time.time()
from module import tambah as t
from module import kali as k
from module import pangkat as p

hasil = t(1,2,3,4,5)
print(f"hasil tambah = {hasil}")

kali = k(1,2,3,4,5)
print(f"hasil tambah = {kali}")

pangkat = p(2)
print(f"hasil pangkat = {pangkat(5)}")

end = time.time()

print(f"hasil waktu execute prosess = {end - start}")