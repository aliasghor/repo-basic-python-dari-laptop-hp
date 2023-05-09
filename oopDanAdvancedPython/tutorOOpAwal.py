import os

class Hero:
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "Gerry"
hero1.health = 100

hero2.name = "Mogi"
hero2.health = 500

hero3.name = "Ali ganteng"
hero3.health = 1000

hero4.name = "Sampi"
hero4.health = 900

def main() -> None:
    print(hero1)
    print(hero1.__dict__)
    print(hero1.name)
    print(hero2)
    print(hero2.__dict__)
    print(hero2.name)
    print(hero3)
    print(hero3.__dict__)
    print(hero3.name)


if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()