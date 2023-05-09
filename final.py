import os
import CRUD as CRUD

if __name__ == '__main__':
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print(25*"=")

    # check database ada ato tidak

    CRUD.init_console()

    while True:
        match sistem_operasi:
          case "posix":
              os.system("clear")
          case "nt":
              os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print(25*"=")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Remove Data\n")

        user_option = input("Masukan opsi: ")

        match user_option:
            case "1":CRUD.read_console()
            case "2":CRUD.create_console()
            case "3":CRUD.update_console()
            case "4":print("Remove data: ")

        is_done = input("Apakah sdh selesai (Y/N) ")
        if is_done == "Y":
            print("Makasih sd nyoba")
            break