class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def full_name(self):
        return f"{self.name} {self.address}"


s = Student("paru", "pokhara")
print(s.full_name())

# Inheritance
class School(Student):
    def __init__(self, name, address, age):
        super().__init__(name, address)
        self.age = age


my_school = School("paru", "pokhara", 18)

print(my_school.full_name())
print(my_school.age)