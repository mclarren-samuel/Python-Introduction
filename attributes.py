class Student:
    school = "Strathmore Universtiy"

    def __init__(self, name):
        self.name = name

student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school)
print(student1.name)

student2.school = "Nairobi University"
print(student2.school)
print(student2.name)