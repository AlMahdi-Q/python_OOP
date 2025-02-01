from Employee import Employee
from Payment import Salary
from Roles import *

class Manager(Employee, ManagerRole, Salary):

    def __init__(self, first_name, last_name, salary, employees=None):
        Employee.__init__(self, first_name, last_name)
        Salary.__init__(self, salary)
        ManagerRole.__init__(self, employees)

    def info(self):
        return f'{self.first_name} {self.last_name}, Job title: {self.__class__.__name__}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split('-')
        salary = int(salary)
        return cls (first_name, last_name, salary)