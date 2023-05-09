# import os
# os.system("cls")

# class Hero:

#     def __init__(self,name,health,attackPower,armorPower):
#         self.name = name
#         self.health = health
#         self.attackPower = attackPower
#         self.armorPower = armorPower

#     def attack(self,opponent):
#         print(self.name + " is attacking " + opponent.name)
#         opponent.underAttack(self,self.attackPower)

#     def underAttack(self,opponent,attackPower):
#         print(self.name + " got under attack by " + opponent.name)
#         total = attackPower / self.armorPower
#         print("total damage did: " + str(total))
#         self.health -= total
#         print("leftover's " + self.name + " health is " + str(self.health))

#     def buff(self,opponent):
#         print(self.name + " picked the buff from " + opponent.name)
#         opponent.stole(self,self.attackPower)

#     def stole(self,opponent,attackPower):
#         print(self.name + " just stole " + opponent.name + " buff ")
#         total = attackPower + self.armorPower
#         print("total damage did from buff = " + str(total))
#         self.health -= total
#         print("leftover's " + self.name + " health is " + str(self.health))

#     def lifesteal(self,opponent):
#         print(self.name + " life steal" + opponent.name)
#         opponent.result(self,self.attackPower)

#     def result(self,opponent,health):
#         print(self.name + " just got life steal by " + opponent.name)
#         total = health + self.armorPower
#         print(self.name + " health is " + str(total))
#         self.health += total
#         print(self.name + " total health is " + str(self.health))

#     def super(self,opponent):
#         print(self.name + " activate super to " + opponent.name)
#         opponent.gotSupered(self,self.attackPower)

#     def gotSupered(self,opponent,power):
#         print(self.name + " just got supered by " + opponent.name)
#         total = power + self.attackPower
#         print("total damage from super: " + str(total))
#         self.health -= total
#         print("leftover's " + self.name + " health is " + str(self.health))

# gerry = Hero("Gerry",100,10,10)
# mogi = Hero("Mogi",95,20,5)
# gerry.attack(mogi)
# print("\n")
# mogi.attack(gerry)
# print("\n")
# gerry.buff(mogi)
# print("\n")
# mogi.buff(gerry)
# print("\n")
# gerry.lifesteal(mogi)
# print("\n")
# mogi.lifesteal(gerry)
# print("\n")
# gerry.super(mogi)
# print("\n")
# mogi.super(gerry)

# gerry.attack(mogi)
# print("\n")
# mogi.attack(gerry)
# print("\n")
# gerry.buff(mogi)
# print("\n")
# mogi.buff(gerry)
# print("\n")
# gerry.lifesteal(mogi)
# print("\n")
# mogi.lifesteal(gerry)
# print("\n")
# gerry.super(mogi)
# print("\n")
# mogi.super(gerry)

import os
os.system("cls")

class Hero:

    def __init__(self,name,health,attackPower,armorPower):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorPower = armorPower

    def attack(self,opponent):
        print(self.name + " attack " + opponent.name)
        opponent.underAttack(self,self.attackPower)

    def underAttack(self,opponent,attackPower):
        print(self.name + " got atacked by " + opponent.name)
        total = attackPower / self.armorPower
        print("Total damage did " + self.name + " is " + str(total))
        self.health -= total
        print("health " + self.name + " = " + str(self.health))

    def super(self,opponent):
        print(self.name + " super " + opponent.name)
        opponent.gotSupered(self,self.attackPower)

    def gotSupered(self,opponent,super):
        print(self.name + " just got supered by " + opponent.name)
        total = super + self.attackPower
        print("Total damage did using super = " + str(total))
        self.health -= total
        print("health " + self.name + " = " + str(self.health))

    def lifeSteal(self,opponent):
        print(self.name + " just stole buff from " + opponent.name)
        opponent.life(self,self.attackPower)

    def life(self,opponent,attackPower):
        print("buff "+ self.name + " just got stole by " + opponent.name)
        total = attackPower + self.armorPower
        print("Total damage from buff = " + str(total))
        self.health += total
        print("health " + self.name + " = " + str(self.health))

    

gerry = Hero("Gerry",100,15,10)
mogi = Hero("Mogi",90,25,5)
gerry.attack(mogi)
print("\n")
mogi.attack(gerry)
print("\n")
gerry.super(mogi)
print("\n")
mogi.super(gerry)
print("\n")
gerry.lifeSteal(mogi)
print("\n")
mogi.lifeSteal(gerry)