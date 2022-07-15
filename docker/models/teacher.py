from models.person import Person

class Teacher(Person):
    
    def __init__(self, firstName, lastName, email, classTeacher, salary, experience):
        Person.__init__(self, firstName, lastName, email)
        self.classTeacher = classTeacher
        self.salary = salary
        self.experience = experience
        
    def getSalaryPerMonth(self):
        return "{:.2f}".format(self.salary / 12)