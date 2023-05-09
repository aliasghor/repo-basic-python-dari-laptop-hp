import gerry
import os
os.system("cls")

def main():
    hasil = gerry.angka(1,2)
    print(hasil)

    hasil = gerry.dict()
    print(hasil.get("nama"))

if __name__ == '__main__':
    main()