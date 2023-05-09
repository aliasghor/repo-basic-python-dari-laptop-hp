import os

class Team:

    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class TypeHero:

    def setType(self,type):
        self.type = type

    def showType(self):
        print(self.type)

class Hero(Team,TypeHero):

    def __init__(self,name,health):
        self.name = name 
        self.health = health

def main():
    gerry = Hero("Gerry",100)

    print(gerry.name)
    gerry.setTeam("Offlaner")
    gerry.setType("Fighter")

    gerry.showTeam()
    gerry.showType()

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear") 
        case "nt":os.system("cls")

    main()