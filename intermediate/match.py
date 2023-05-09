import os

"""angka yg berupa tuple"""
angka = (8,1)

match angka:
    case (0,gerry):
        print("on y -axis")
    case (gerry,0):
        print("on x-axis")
    case (gerry,mogi):
        print("not on axis")


"""angka integer"""
angka = 2

match angka:
    case 1:
        print("angka 1")
    case 2:
        print("angka 2")
    case 3:
        print("angka 3")


"""angka float"""
angka = 1.5

match angka:
    case 1.8:
        print("angka 1.8")
    case 1.2:
        print("angka 1.2")
    case 1.5:
        print("angka 1.5")


"""String"""
huruf = "S"

match huruf:
    case "S":
        print("huruf S Kapital letter")
    case "Med":
        print("Medium")
    case "Lg":
        print("Larger")

"""Underscore statment"""
angka = 3

match angka:
    case 1 | 4:
        print("Small")
    case 5 | 10:
        print("Medium")
    case _:
        print("Large")


"""Studi kasus"""
def grade(score: int) -> int:
    match score:
        # case >= 90 or case > 90 these 2 cases won't work
        case score if score >= 90:
            print("A")
        case score if score >= 80:
            print("B")
        case score if score >= 75:
            print("C")
        case _:
            print("The grade is either D or F")

def gerry(ukuranBaju: str) -> str:
    match ukuranBaju:
        case "S" | "Sm":
            print("Ukuran Baju Small")
        case "M" | "Med":
            print("Ukuran Baju Medium")
        case "L" | "large":
            print("Ukuran Baju Large")
        case x:
            print(f"ukuran baju {x} gkada")

def ganjilGenap(angka: int) -> int:
    match angka:
        case angka if angka%2==0:
            print(f"{angka} adalah genap")
        case _:
            print(f"{angka} adalah ganjil")


def main() -> None:
    grade(75)
    grade(60)
    grade(100)
    gerry("Large")
    ganjilGenap(1)

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")
        
    main()