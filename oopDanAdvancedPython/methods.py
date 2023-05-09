import os
os.system("cls")

class Hero:

    """Class variabel"""
    jumlahHero = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        """Instance variabel"""
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        # Hero.jumlahHero += 1
        # print("Membuat hero dengan nama " + inputName)

    """Void function, method tanpa return"""
    def gerry(self):
        print(f"nama eug adalah {self.name}")

    """Method dengan argument"""
    def healthUp(self,up):
        self.health += up

    """Method dengan return"""
    def getHealth(self):
        return self.health


hero1 = Hero("Gerry",100,10,0)
hero2 = Hero("Ali ganteng",1000,100,10)

hero2.gerry()
hero2.healthUp(10)
print(hero2.getHealth())


# hero1 = Hero("Gerry",100,10,0)
# print(hero1.jumlahHero)
# hero2 = Hero("Mogi",1000,100,100)
# print(hero2.jumlahHero)
# hero3 = Hero("Ali ganteng",100000,10000,1000)
# print(hero3.jumlahHero)
# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(hero3.__dict__["name"])