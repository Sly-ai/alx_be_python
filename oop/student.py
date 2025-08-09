class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def is_adult(self):
        return self.age >= 18

student1 = student("Alice", 20)
print(student1.get_info())
print("Is adult:", student1.is_adult())
student2 = student("Bob", 16)
print(student2.get_info())
print("Is adult:", student2.is_adult())