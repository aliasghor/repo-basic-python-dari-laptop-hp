from . import Database
from .Util import random_string
import time


def create(tahun: int,judul: str,penulis: str) -> str:
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%Sz",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["penulis"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["penulis"]}, {data["tahun"]}'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gerry")

def create_first_data() -> None:
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa angka (yyyy)")
        except:
            print("Tahun harus berupa angka (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%Sz",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["penulis"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["penulis"]}, {data["tahun"]}'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)

    except:
        print("Gerry")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            print(jumlah_buku)
            if "index" in kwargs:
                print("Terdeteksi index")
            return content
    except:
        print("Membaca database erorr")
        return False
    
