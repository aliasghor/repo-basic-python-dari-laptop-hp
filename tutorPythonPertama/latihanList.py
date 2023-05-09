# program list buku

listBuku = []
while True:
    judul = input("Masukan judul buku: ")
    penulis = input("Masukan penulis: ")

    bukuBaru = [judul,penulis]
    listBuku.append(bukuBaru)
    
    print("\n\n","="*10)
    for index,buku in enumerate(listBuku):
        print(f"{index+1}\t | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    lanjut = input("Mo lanjut apa kgk? (y/n): ")

    if lanjut == "n":
        break

print("Makasih ngab")