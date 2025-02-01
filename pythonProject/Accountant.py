from Employee import Employee

class Accountant(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.__salary = salary

    def info(self):
        return f'{self.first_name} {self.last_name}, Job title: {self.__class__.__name__}'

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split('-')
        salary = int(salary)
        return cls (first_name, last_name, salary)
