import os
import datetime as dt

def taro() -> int:
    try:
        tahunLahir = int(input("Masukan tahun lahir antum: "))
        bulanLahir = int(input("Masukan bulan lahir antum pake angka e.g (1-12): "))
        hariLahir = int(input("Masukan hari lahir antum pake angka e.g (1-31): "))

    except:
        raise ValueError ("Terjadi kesalahan pas input masukin harus berupa int bukan str dan float")

    return tahunLahir,bulanLahir,hariLahir

def akhir(tahunLahir: int,bulanLahir: int,hariLahir: int) -> int:
    return dt.datetime(tahunLahir,bulanLahir,hariLahir)

def main() -> None:
    while True:
        TAHUNLAHIR,BULANLAHIR,HARILAHIR = taro()
        gerry = akhir(TAHUNLAHIR,BULANLAHIR,HARILAHIR)
        print(f"Antum lahir di tahun {gerry} dan antum lahir di hari {gerry:%A}")

        keluar = input("Mo cabut apa kagak?? (Y/N): ")
        match keluar:
            case "Y":break
            case _:continue

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()

