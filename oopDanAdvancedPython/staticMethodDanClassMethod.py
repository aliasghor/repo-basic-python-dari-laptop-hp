import os
os.system("cls")

class Hero:

    """Private class variabel"""
    __jumlah = 0

    def __init__(self,name):
        self.name = name
        Hero.__jumlah += 1

    """Method ini hanya berlaku untuk objek"""

    def getJumlah(self):
        return Hero.__jumlah

    """Method ini gk berlaku untuk objek"""
    def getJumlah1():
        return Hero.__jumlah

    """Method static (decorator)"""
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(self):
        return self.__jumlah

gerry = Hero("Gerry")
print(Hero.getJumlah2())
mogi = Hero("Mogi")
print(mogi.getJumlah2())
sampi = Hero("Sampi")
print(gerry.getJumlah3())