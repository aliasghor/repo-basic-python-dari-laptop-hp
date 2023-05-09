import os

class Employee:

    raiseAmount = 1.04

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.gmail = firstName + "." + lastName + "@gmail.com"

    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

    def applyRaise(self):
        self.salary = int(self.salary * self.raiseAmount)

class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self,firstName,lastName,salary,progLang):
        super().__init__(firstName,lastName,salary)
        self.progLang = progLang

class Manager(Employee):

    def __init__(self,firstName,lastName,salary,employees=None):
        super().__init__(firstName,lastName,salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmps(self):
        for i in self.employees:
            print("-->",i.fullName())


def main():
    dev1 = Developer("Ali","Asghor",5000,"Advanced Python")
    dev2 = Developer("Muchsin","Alwi",3000,"NewBie Python")


    mgr1 = Manager("Gerry","Gerryganteng",10000,[dev1])

    print(isinstance(mgr1,Developer))
    print(issubclass(Manager,Developer))

    # print(mgr1.gmail)

    # mgr1.addEmp(dev2)
    # mgr1.removeEmp(dev1)

    # mgr1.printEmps()


    # print(help(Developer))

    # print(dev1.gmail)
    # print(dev1.progLang)

    # print(dev1.salary)
    # dev1.applyRaise()
    # print(dev1.salary)

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()
