

class Person:

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def printAllDetails(self):
        print(self.firstName, self.lastName, self.email)
    
class Student(Person):

    def __init__(self, firstName, lastName, email, rollNo):
        Person.__init__(self, firstName, lastName, email)
        self.rollNo = rollNo

    def getRollNo(self):
        return self.rollNo

class Teacher(Person):
    def __init__(self, firstName, lastName, email, classTeacher, salary, experience):
        Person.__init__(self, firstName, lastName, email)
        self.classTeacher = classTeacher
        self.salary = salary
        self.experience = experience

    def getSalaryPerMonth(self):
        return "{:.2f}".format(self.salary / 12)

    

s1 = Student("Nihar","Doshi","nihar@gmail.com", 10)
t1 = Teacher("Smita", "Demalo","smita@yahoo.com", "2", 1000000, 3)

print(s1.getFirstName(), s1.getLastName(), s1.getEmail(), s1.getRollNo())
print(t1.firstName, t1.getSalaryPerMonth())
s1.printAllDetails()
t1.printAllDetails()

# print(p1.getName())

