import os

class Hero:

    def __init__(self,name,health,armor):
        self.__name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name: {} \nhealth: {}".format(self.__name,self.__health)

    @property
    def armor(self):
        return "name: {} \narmor: {}".format(self.__name,self.__armor)

    @property
    def name(self):
        return "name: {}".format(self.__name)

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @name.setter
    def name(self,name):
        self.__name = name

def main():
    gerry = Hero("Gerry",100,10)

    print(gerry.info)

    gerry.name = "Ali"
    print(gerry.info)
    
    gerry.armor = 150
    print(gerry.armor)

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()