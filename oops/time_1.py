# class NIET:
#     def __init__():
#         pass
# class Campus:
#     def __init__(self):
#         pass
class Person:
    def __init__(self):
        self.name=input('Enter your name: ')
        self.age = int(input("Enter your age: "))
        self.idno = input("Enter you ID number: ")
        pass
    def showDetails(self):
        print(f"""
        Name: {self.name}
        Age: {self.age}
        ID: {self.idno}
        """)
# class Admin(Person):
#     def __init__(self):
#         pass
# class Management(NIET):
#     def __init__(self):
#         pass
class Student(Person):
    def __init__(self):
        super().__init__()
        pass
class Faculty(Person):
    def __init__(self):
        super().__init__()
        department=input("Enter your department: ")
        subject = input(input("Enter your subject: "))
        no_of_lectures = int(input("Enter the number of lectures: "))
        lectures_in_classes = []
        for i in range(no_of_lectures):
            class_name = input(f"Enter the class name {i+1} (in which you take lecture) :")
            lectures_in_classes.append(class_name)
        pass
    def showDetails(self):
        super().showDetails()
        print(f"""
        Department: {self.department}
        Subject: {self.subject}
        No. of Lectures: {self.no_of_lectures}
        Classes: {self.lectures_in_classes}
        """)