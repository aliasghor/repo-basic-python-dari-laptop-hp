import os
os.system("cls")

class Employee:

    totalEmployee = 0

    raiseAmount = 1.04

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.gmail = firstName + "" + lastName + "@gmail.com"

        Employee.totalEmployee += 1

    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

    def raiseSalary(self):
        self.salary = int(self.salary * self.raiseAmount)

def main():
    print(f"Total employee  before initalize new variabel = {Employee.totalEmployee}")
    emp1 = Employee("Ali","Asghor",5000)
    emp2 = Employee("Muchsin","Alwi",4000)
    emp3 = Employee("Adika","Yusuf",3000)

    print(emp1.__dict__)
    print(emp2.__dict__)
    print(emp3.__dict__)

    print(f"Employee name = {emp1.firstName}")
    print(f"Employee name = {emp2.firstName}")
    print(f"Employee name = {emp3.firstName}")

    print(f"Emplyoee full name = {emp1.fullName()}")
    print(f"Emplyoee full name = {emp2.fullName()}")
    print(f"Emplyoee full name = {emp3.fullName()}")

    print(f"Employee salary = {emp1.salary}")
    print(f"Employee salary = {emp2.salary}")
    print(f"Employee salary = {emp3.salary}")

    emp1.raiseSalary()
    emp2.raiseSalary()
    emp3.raiseSalary()
    print(f"Employee after got the raise salary = {emp1.salary}")
    print(f"Employee after got the raise salary = {emp2.salary}")
    print(f"Employee after got the raise salary = {emp3.salary}")
    print(f"Total employee after initalize new variabel = {Employee.totalEmployee}")

if __name__ == '__main__':
    operatingSystem = os.name

    match operatingSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    main()