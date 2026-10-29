
class Student:

    # Constructor
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    # Method
    def display_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


# Creating objects
student1 = Student("Nila", 22, "Computer Science")
student2 = Student("Arun", 21, "Information Technology")

student1.display_details()

print("----------------")

student2.display_details()
