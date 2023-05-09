class Employee:

    raiseAmount = 1.04

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.gmail = firstName + "" + lastName + "@gmail.com"

    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

    def raiseSalary(self):
        self.salary = int(self.salary * Employee.raiseAmount)

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
