import os
os.system("cls")

class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower


    """Getter"""
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    """Settter"""
    def diserang(self,attackPower):
        self.__health -= attackPower

    def setAttackPower(self,nilaiBaru):
        self.__attackPower = nilaiBaru

"""Awal dari game"""
gerry = Hero("Gerry",100,10)
print(gerry.__dict__)

"""Game berjalan"""
print(gerry.getName())
print(gerry.getHealth())
gerry.diserang(5)
print(gerry.getHealth())
