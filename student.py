class Student:
    def __init__(self, student_id=None, name=None, schedule=None, email=None, phone=None):
        self.student_id = student_id
        self.name = name
        self.schedule = schedule
        self.email = email
        self.phone = phone

    def __str__(self):
        return (f'Name: {self.name}, Schedule: {self.schedule}, Email: {self.email}, Phone: {self.phone}')
