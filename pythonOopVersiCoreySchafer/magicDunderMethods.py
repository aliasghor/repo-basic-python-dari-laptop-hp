import os
os.system("cls")

class Employee:

    raiseAmount = 1.04

    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last 
        self.gmail = first + "." + last + "@gmail.com" 
        self.pay = pay

    def fullName(self):
        return "{} {}".format(self.first,self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount) 

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullName(),self.gmail)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())

def main():
    emp1 = Employee("Ali","asghor",5000)
    emp2 = Employee("Muchsin","alwi",4000)

    # print(emp1)
    print(repr(emp1))
    print(str(emp1))

    print(str.__add__("Hello"," World"))
    print(len(emp1))
    # print("Gerry".__len__())

    print(emp1 + emp2)


if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()