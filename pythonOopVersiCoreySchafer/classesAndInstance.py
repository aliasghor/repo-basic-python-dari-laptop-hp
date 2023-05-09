import os
os.system("cls")

# class Employee:

#     pass

# emp1 = Employee()
# emp2 = Employee()

# print(emp1)
# print(emp2)

# emp1.first = "Ali"
# emp1.last = "Asghor"
# emp1.email = "aliasghor6@gmail.com"
# emp1.pay = "3000$"

# emp2.first = "Mogi"
# emp2.last = "Mogi"
# emp2.email = "mogi@gmail.com"
# emp2.pay = "2000$"

# print(emp1.email)
# print(emp2.email)


class Boss:

    def __init__(self,firstName,lastName,balance,email):
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        self.email = email

    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

    def totalSaldo(self):
        return "{} {} saldo rekening: {}".format(self.firstName,self.lastName,self.balance)

ali = Boss("Ali","Asghor","10 kuadrilliun","aliasghor6@gmail.com")
print(ali.__dict__)
print(ali.firstName)
print(ali.fullName())
print(ali.totalSaldo())
