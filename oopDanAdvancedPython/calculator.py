import os

def angka():
    try:
        angka1 = int(input("Masukan angka pertamanya: "))
        maoApa = input("Masukan operasinya (x or *,/,+,-,%): ")
        angka2 = int(input("Masukan angka keduanya: "))

    except:
        raise ValueError ("Terjadi kesalahan pas masukin input,input harus berupa int bukan float ato str")

    return angka1,maoApa,angka2

def hasil(angka1,maoApa,angka2):
    try:
        match maoApa:
            case "+":
                return angka1 + angka2

            case "-":
                return angka1 - angka2

            case "x" | "*":
                return angka1 * angka2

            case "/":
                return angka1 / angka2

            case "%":
                masukan = input("Mao ditambah apa dikurang persennya?? (+,-): ")
                match masukan:
                    case "+":
                        return angka2*(angka1/100)+angka1

                    case "-":
                        return angka2*(angka1/100)-angka1

                    case other:
                        print(f"Operasi {other} tidak ditemukan")

    except:
        raise ZeroDivisionError ("Seluruh angka yg dibagi 0 = tidak terdefinisi")

    else:
        print("Operasi yg anda masukan tidak ditemukan silahkan masukan lg")

    finally:
        print("Dibawah adalah hasil anda")

def main() -> None:
    while True:
        ANGKA1,MAOAPA,ANGKA2 = angka()
        HASIL = hasil(ANGKA1,MAOAPA,ANGKA2)

        print(f"Hasilnya adalah {HASIL}")

        keluar = input("Mo keluar apa kagak??? (Y/N): ")

        match keluar:
            case "Y":break
            case _:continue

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()

            