class Project:
    def __init__(self, name, description, days, done):
        self.name = name
        self.description = description
        self.days = days
        self.done = done

    def __str__(self):
        return f'{self.name}: {self.description}, {'done' if self.done else 'not done'}'
