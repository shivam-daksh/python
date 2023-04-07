class person:
    def __init__(self, fname, lname, age, bgroup,e_type, p_id:
    fname=input("Input your first name: ")
    lname= input('Enter your last name: ')
    age = int(input("Enter you age: "))
    bggroup = input("Enter your blood group: ")
    e_type = input("Enter your profession: ")
    profession= input("What is your profession? : ")
    self.firstName = fname
    self.lastName = lname
    self.age = age
    self.bgroup = bggroup
    self.e_type = e_type
    self.profession = profession
    self.person_id = p_id
class faculty(person):
    def __init__(self, subject, dept, lec):
        sub = input("Enter your subject")
        dept = input("Enter you department")
        lec = int(input("Enter the no. of lectures : "))
        self.subject = sub
        self.department = dept
        self.lectures = lec
            
        
