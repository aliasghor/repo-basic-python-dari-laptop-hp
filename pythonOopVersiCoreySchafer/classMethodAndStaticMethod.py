import os
import datetime

class Employee:

    totalEmp = 0

    raiseAmount = 1.04

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.gmail = firstName + "." + lastName + "@gmail.com"

        Employee.totalEmp += 1

    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

    def raiseSalary(self):
        self.salary = int(self.salary * self.raiseAmount)

    @classmethod
    def setRaiseAmount(cls,amount):
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls,empStr):
        firstName,lastName,salary = empStr.split("-")
        return cls(firstName,lastName,salary)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

def main():
    # print(f"Total employee = {Employee.totalEmp}")
    emp1 = Employee("Ali","Asghor",5000)
    emp2 = Employee("Muchsin","Alwi",4000)
    emp3 = Employee("Adika","Yusuf",3000)

    myDate = datetime.date(2023,2,2)

    print(Employee.isWorkDay(myDate))

    # empStr1 = "Gerry-gerry-7000"
    # empStr2 = "Sampi-sampi-3000"
    # empStr3 = "Mogi-mogi-4000"

    # newEmp1 = Employee.fromString(empStr1)


    # print(newEmp1.gmail)
    # print(newEmp1.salary)


    # Employee.setRaiseAmount(1.05)
    # print(Employee.raiseAmount)
    # print(emp1.raiseAmount)
    # print(emp2.raiseAmount)
    # print(emp3.raiseAmount)

    # print(f"Employee name = {emp1.firstName}")
    # print(f"Employee name = {emp2.firstName}")
    # print(f"Employee name = {emp3.firstName}")

    # print(f"Employee full name = {emp1.fullName()}")
    # print(f"Employee full name = {emp2.fullName()}")
    # print(f"Employee full name = {emp3.fullName()}")

    # print(f"Employee salary = {emp1.salary}")
    # print(f"Employee salary = {emp2.salary}")
    # print(f"Employee salary = {emp3.salary}")

    # emp1.raiseSalary()
    # emp2.raiseSalary()
    # emp3.raiseSalary()

    # print(f"Employee raise salary = {emp1.salary}")
    # print(f"Employee raise salary = {emp2.salary}")
    # print(f"Employee raise salary = {emp3.salary}")

    # print(f"Total employee = {Employee.totalEmp}")

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":
            os.system("clear")

        case "nt":
            os.system("cls")

    main()