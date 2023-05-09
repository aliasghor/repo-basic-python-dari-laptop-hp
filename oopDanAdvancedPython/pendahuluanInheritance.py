import os
os.system("cls")

class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

gerry = Hero("Gerry",100)
mogi = Hero_intelligent("Mogi",50)
sampi = Hero_strength("Sampi",50)
print(gerry.name)
print(mogi.name)
print(sampi.name)