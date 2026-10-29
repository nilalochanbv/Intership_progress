class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_student(self):
        self.display_person()
        print("Department:", self.department)


student = Student("Nila", 22, "Computer Science")
student.display_student()