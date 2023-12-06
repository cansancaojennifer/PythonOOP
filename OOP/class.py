class Dog:

    def __init__(self, name):
        self.name = name
        print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Snow")
d.bark()
print(d.add_one(5))

print(type(d))
