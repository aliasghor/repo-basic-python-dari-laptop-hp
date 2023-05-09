# nama = "Ali ganteng"

# def dict():
#     data = {
#         "nama":"ALi Asghor",
#         "hobby":"Coding and make AI and robot"
#     }
#     return data["hobby"]

# def angka(y):
#     return lambda x:x**y

def tambah(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def kali(*args):
    hasil = 1
    for i in args:
        hasil *= i
    return hasil

def pangkat(y):
    return lambda x:x**y