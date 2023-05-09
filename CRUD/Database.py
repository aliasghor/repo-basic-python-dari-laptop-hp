from . import Operasi


DB_NAME = "data_4.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console() -> None:
    try:
        with open(DB_NAME,'r') as file:
            print("Database tersedia")

    except:
        print("Database tidak ada ane bikinin yak")
        Operasi.create_first_data()
            