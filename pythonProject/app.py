import Employee
import Accountant
from Manager import *
import Project
from Roles import *
from Payment import *
from Programmer import FreelancerProgrammer, Programmer
from Project import Project
from Profile import *

if __name__ == '__main__':

    project1 = Project('calculator', 'calculate and give the answer of equations', 4, True)
    project2 = Project('calender', 'show, sort and manage events', 3, False)

    ahmed = FreelancerProgrammer('Ahmed', 'khaled', 130, 33, 'python', [project1, project2])
    ahmed.profile = Profile('Iraq-Baghdad', 92382938, 'ahmed003@gmail.com', True)

    khaled = Programmer('Khaled', 'Kamal', 3000, 'PHP', [project1])

    almahdi = Manager('Al Mahdi', 'Rashid', 5000, [ahmed, khaled])

    print(ahmed.get_projects())
    print(khaled.get_projects())
    print(almahdi.info())
    print(almahdi.get_employees())

    for employee in (ahmed, khaled, almahdi):
        print(f'{employee.first_name} {employee.last_name} is paid:')
        print(employee.calculate_salary())
        print('-'*20)