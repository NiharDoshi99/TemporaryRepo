from models.student import Student
from models.teacher import Teacher
    

s1 = Student("Nihar","Doshi","nihar@gmail.com", 10)
t1 = Teacher("Smita", "Demalo","smita@yahoo.com", "2", 1000000, 3)
t2 = Teacher("PT","ABC","pt@yahoo.com",None,700000,0.5)

teacherList = []

print(s1.getFirstName(), s1.getLastName(), s1.getEmail(), s1.getRollNo())
print(t1.firstName, t1.getSalaryPerMonth())
s1.printAllDetails()

teacherList.append(t1)
teacherList.append(t2)

for teacher in teacherList:
    print(teacher.getFirstName())
