class student:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def full_name(self):
        return f"{self.name} {self.address}"


s =student("paru","pokhara")
print(s.full_name())





