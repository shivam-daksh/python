class Person:
    def __init__(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.blood_group = input("Blood Group: ")
        self.age = int(input('Age: '))


class Faculty(Person):
    def __init__(self):
        super().__init__()
        self.subject = input('Subject: ')
        self.department = input('Department: ')
        self.lectures = int(input('No. of Lectures: '))


class Student(Person):
    def __init__(self):
        super().__init__()
        self.course = input('Course/Program: ')
        self.branch = input('Branch: ')
        self.spln = input('Specialisation: ')
        self.section = input('Section: ')
class Class:
    def __init__(self):
        self.branch = input('Branch: ')
        self.section = input('Section: ')
        self.strength = input('Strength: ')
        self.lectures = input('No. of Lectures: ')
        self.building = input('Building: ')
        self.floor = int(input('Floor: '))
        self.room_no = input("Room No.: ")
