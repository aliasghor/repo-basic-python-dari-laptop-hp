import os
os.system("cls")

class Hero:

    """Private class variabel"""
    __jumlah = 0

    def __init__(self,name,health,attackPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attackPowerStandar = attackPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attackPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name,"Level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attackPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self,musuh):
        self.gainExp = 50


gerry = Hero("gerry",100,5,10)
mogi = Hero("Mogi",100,5,10)
print(gerry.info)

gerry.attack(mogi)
gerry.attack(mogi)
gerry.attack(mogi)
print(gerry.info)
    