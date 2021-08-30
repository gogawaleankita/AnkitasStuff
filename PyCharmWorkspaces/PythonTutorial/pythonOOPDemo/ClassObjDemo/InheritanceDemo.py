class Person:
    def __init__(self,name,lname):
        self.name=name;
        self.lname=lname;

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in self:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees

class Employee(Person):
    all_Employees=EmployeesList()
    def __init__(self,name,lname,empid):
        Person.__init__(self,name,lname)
        self.empid=empid

    def getSalary(self):
        return 'You get Monthly salary.'

    def getBonus(self):
        return 'You are eligible for Bonus.'

e1=Employee("Ankita","Gogawale","1708974")
print(e1.name+" "+e1.lname+"-"+e1.empid)




e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('George', 'Brown', 656721)
print(Employee.all_Employees.search('or'))


class ContractEmployee(Employee):
   def getSalary(self):
        return 'You will not get Salary from Organization.'

   def getBonus(self):
        return 'You are not eligible for Bonus.'
e1 = Employee('Jack', 'simmons', 456342)
e2 = ContractEmployee('John', 'williams', 123656)
print(e1.getBonus())
print(e2.getBonus())

