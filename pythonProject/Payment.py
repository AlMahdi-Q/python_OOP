class Salary:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class HourlyPayment:
    def __init__(self, hour_rate, work_hours):
        self.hour_rate = hour_rate
        self.work_hours = work_hours

    def calculate_salary(self):
        return self.hour_rate * self.work_hours