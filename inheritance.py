class Student:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.fees = 40000

    def fullName(self):

        print(f'Fullname of the student is {self.firstname}  and {self.lastname}')

    def Fees(self):
        print(f'Fees of the student is {self.fees}')


class NarayanaStudent(Student):
    
    def __init__(self, fname, lname):

        self.firstname = fname
        self.lastname = lname
        
        print(f"{self.firstname} {self.lastname} says that Narayana students are the smartest in the world!!")

stud1 = Student("Ishaan", "Awasthi")
stud1.fullName()
stud1.Fees()

nar1 = NarayanaStudent("Dhruv", "Pathak") 
nar1.fullName()
