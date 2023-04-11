class Employee():

    __count = 0
    __salary = []
    __avg_salary = 0

    def __init__(self):
        self.name = input("Enter your name: ")
        self.designation = input("Designation: ")
        self.salary = int(input("Salary: "))
        Employee.__salary.append(self.salary)
        Employee.__count += 1
        for i in Employee.__salary:
            total = 0
            total += i
            Employee.__avg_salary = total/len(Employee.__salary)

    def getdata(self):
        print("""
        Name: {}
        Designation: {}
        Salary: {}
        """.format(self.name, self.designation, self.salary)
              )

    def display(self):
        print("""
        Employee Name: {}
        Employee Designation: {}
        Employee Salary: {}
        """.format(self.name, self.designation, self.salary))

    def emp_count():
        print("Total No. of  Employees: ", Employee.__count)

    def avg_salary():
        print("Average Salary of All Employees: ", Employee.__avg_salary)
