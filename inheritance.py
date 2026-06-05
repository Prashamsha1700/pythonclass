# Parent class
class Parent:
    def __init__(self, father_name, mother_name):
        self.__father_name = father_name
        self.__mother_name = mother_name

    # Getters
    def get_father_name(self):
        return self.__father_name

    def get_mother_name(self):
        return self.__mother_name

    # Setters
    def set_father_name(self, father_name):
        self.__father_name = father_name

    def set_mother_name(self, mother_name):
        self.__mother_name = mother_name

    def display_parent_details(self):
        print("Father Name:", self.__father_name)
        print("Mother Name:", self.__mother_name)


# Child class inheriting Parent class
class Student(Parent):
    def __init__(self, student_name, roll_no, father_name, mother_name):
        super().__init__(father_name, mother_name)
        self.__student_name = student_name
        self.__roll_no = roll_no

    # Getters
    def get_student_name(self):
        return self.__student_name

    def get_roll_no(self):
        return self.__roll_no

    # Setters
    def set_student_name(self, student_name):
        self.__student_name = student_name

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def display_student_details(self):
        print("Student Name:", self.__student_name)
        print("Roll Number:", self.__roll_no)
        self.display_parent_details()


# Creating object
s1 = Student("Prashamsha", 1, "Narayan", "Laxmi")

# Display details
s1.display_student_details()

# Accessing through getters
print("\nUsing Getters:")
print(s1.get_student_name())
print(s1.get_father_name())

# Modifying through setters
s1.set_roll_no(2)
print("\nUpdated Roll No:", s1.get_roll_no())