class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def gmail(self):
        return "{}.{}@gmail.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Data has been deleted")
        self.first = None
        self.last = None

emp1 = Employee("Ali","asghor")

# emp1.first = "Gerry"

emp1.fullname = "Gerry ganteng"

print(emp1.first)
print(emp1.gmail)
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)