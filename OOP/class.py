class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Snow", 6)
print(d.get_name())
print(d.get_age())
d2 = Dog("Butter", 9)
d2.set_age(12)
print(d2.get_name())
print(d2.get_age())

d.bark()
print(d.add_one(5))

print(type(d))
