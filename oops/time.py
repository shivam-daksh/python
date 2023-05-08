class Department:
    Subjects=[]
    Labs = []
    def __init__(self):
        self.subjects_name = []
        self.subjects_code = []
        no_of_subjects = int(input("Enter the number of subjects"))
        for i in range(no_of_subjects):
            sub_name = input("Subject Name: ")
            sub_code = input("""Subject Code: """)
            print("----------------------------")
            self.subjects_name.append(sub_name)
            self.subjects_code.append(sub_code)
        self.subject_with_code = [self.subjects_name, self.subjects_code]
#     def __init__(self):
#         pass
class Person:
    no_of_person=0
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
        self.designation="Faculty"
        self.department=input("Enter your department: ")
        self.subject = input("Enter your subject: ")
        self.no_of_lectures = int(input("Enter the number of lectures: "))
        self.lectures_in_classes = []
        for i in range(self.no_of_lectures):
            class_name = input(f"Enter the class name {i+1} (in which you take lecture) :")
            self.lectures_in_classes.append(class_name)
        pass
    def showDetails(self):
        super().showDetails()
        print(f"""
        Department: {self.department}
        Subject: {self.subject}
        No. of Lectures: {self.no_of_lectures}
        Classes: {self.lectures_in_classes}
        """)
# Python program for traversal of a linked list
# Node class
