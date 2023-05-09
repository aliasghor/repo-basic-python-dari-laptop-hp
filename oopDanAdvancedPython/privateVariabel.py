import os
os.system("cls")

class Hero:

    """Class variabel"""
    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        """Variabel instance private"""
        self.__private = "private"
        """Variabel instance protected"""
        self._protected = "Protected"

gerry = Hero("Gerry",100)

print(gerry.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)