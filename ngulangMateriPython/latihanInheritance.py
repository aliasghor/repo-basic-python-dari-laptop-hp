import os
os.system("cls")
from Hero import HeroStrength,HeroIntelligent

gerry = HeroIntelligent("Gerry")
mogi = HeroStrength("Mogi")

gerry.showInfo()
mogi.showInfo()

gerry.gainExp = 200
gerry.gainExp = 250

gerry.showInfo()
mogi.showInfo()