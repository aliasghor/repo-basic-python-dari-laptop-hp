import os
os.system("cls")

class Hero:

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info =  "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None

print('merubah info')
gerry = Hero("Gerry",100,10)
print(gerry.info)
gerry.name = "Mogi"
print(gerry.info)

print("gett dan setter unut __armor")
print(gerry.armor)
gerry.armor = 50
print(gerry.armor)
print("Delete armor")
del gerry.armor
print(gerry.__dict__)