from package import Employee
import datetime as dt

def main():
    emp1 = Employee("Ali","Asghor",5000)
    print(emp1.firstName)
    print(emp1.fullName())
    print(emp1.salary)

    emp1.raiseSalary()
    print(emp1.salary)

    newEmp = "Dhamar-Bisma-4000"

    newEmp1 = Employee.fromString(newEmp)

    print(newEmp1.gmail)
    print(newEmp1.salary)

    tanggal = dt.datetime(2023,2,2)
    print(Employee.isWorkDay(tanggal))

if __name__ == '__main__':
    main()