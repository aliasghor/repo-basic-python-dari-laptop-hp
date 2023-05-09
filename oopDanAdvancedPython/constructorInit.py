import os
os.system("cls")

class Hero:
    """Class variabel"""
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        """Instance variabel"""
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama " + inputName)

hero1 = Hero("Gerry",100,10,0)
print(hero1.jumlah)
hero2 = Hero("Mogi",1000,100,10)
print(hero2.jumlah)
hero3 = Hero("Ali Ganteng",10000,1000,100)
print(hero3.jumlah)
# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(Hero.__dict__)
