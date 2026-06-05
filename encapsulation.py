class Student:
    def __init__(self, name, address):
        self._name = name      # protected/private by convention
        self._address = address
        
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address


my_student = Student("name", "address")

print(my_student.get_name())      # Access name through getter
print(my_student.get_address())   # Access address through getter

# Update values through setters
my_student.set_name("Paru")
my_student.set_address("Kathmandu")

print(my_student.get_name())
print(my_student.get_address())