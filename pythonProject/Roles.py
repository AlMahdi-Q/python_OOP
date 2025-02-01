import Project

class ProgrammerRole:
    def __init__(self, lang, projects=None):
        self.lang = lang
        if projects is None:
            self.projects = []
        self.projects = projects

    def assign_project(self, name, description, days, done):
        project = Project.Project(name, description, days, done)
        self.projects.append(project)

    def get_projects(self):
        print('Projects:')
        print('='*10)
        projects_list = []
        for num, project in enumerate(self.projects):
            projects_list.append(f'{num+1}. {project}')
        return '\n'.join(projects_list)

class ManagerRole:
    def __init__(self, employees=None):
        if employees is None:
            self.employees = []
        self.employees = employees

    def get_employees(self):
        print('Employees:')
        print('='*10)
        employees_list = []
        for num, employee in enumerate(self.employees):
            employees_list.append(f'{num+1}. {employee.info()}')
        return '\n'.join(employees_list)
