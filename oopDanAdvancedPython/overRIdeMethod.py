import os
os.system("cls")

class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("show info di class hero")
        print("{} dengan health: {}".format(self.name,self.health))

class Hero_intelligent(Hero):

    def __init__(self,name):
        super().__init__(name,100)

    """Overide"""
    def showInfo(self):
        print("show info di subclass Hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(self.name,self.health))

class Hero_strength(Hero):

    def __init__(self,name):
        super().__init__(name,200)

gerry = Hero_intelligent("Gerry")
mogi = Hero_strength("mogi")
sampi = Hero_strength("sampi")

# gerry.showInfo()
mogi.showInfo()
sampi.showInfo()