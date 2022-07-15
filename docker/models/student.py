from models.person import Person

class Student(Person):

    def __init__(self, firstName, lastName, email, rollNo):
        Person.__init__(self, firstName, lastName, email)
        self.rollNo = rollNo

    def getRollNo(self):
        return self.rollNo