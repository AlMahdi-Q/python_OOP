from Employee import Employee
from Project import Project
from Roles import *
from Payment import *

class Programmer(Employee, ProgrammerRole, Salary):

    def __init__(self, first_name, last_name, salary, lang, projects=None):
        Employee.__init__(self, first_name, last_name)
        ProgrammerRole.__init__(self, lang, projects)
        Salary.__init__(self, salary)

    def info(self):
        return f'{self.first_name} {self.last_name}, Job title: {self.__class__.__name__}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary, lang = emp_str.split('-')
        salary = int(salary)
        return cls (first_name, last_name, salary, lang)


class FreelancerProgrammer(Employee, ProgrammerRole, HourlyPayment):
    def __init__(self, first_name, last_name, hour_rate, work_hours, lang, projects):
        ProgrammerRole.__init__(self, lang, projects)
        Employee.__init__(self, first_name, last_name)
        HourlyPayment.__init__(self, hour_rate, work_hours)

    def info(self):
        return f'{self.first_name} {self.last_name}, Job title: {self.__class__.__name__}, Work Hours: {self.work_hours}'

    def calculate_salary(self):
        return HourlyPayment.calculate_salary(self)