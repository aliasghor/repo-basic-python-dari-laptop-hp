import os
os.system("cls")
from Hero import HeroIntelligent,HeroStrength


gerry = HeroIntelligent("Gerry")
mogi = HeroStrength("Mogi")

gerry.show_info()
mogi.show_info()

gerry.gainExp = 200
mogi.gainExp = 250

gerry.show_info()
mogi.show_info()