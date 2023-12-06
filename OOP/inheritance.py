class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say.")

class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}.")

    def speak(self):
        print("Meow")

class Dog(Pet):

    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Barry", 3)
p.show()
p.speak()
c = Cat("Gary", 5, "Orange")
c.show()
c.speak()
d = Dog("Charlie", 11)
d.show()
d.speak()
f = Fish("Bubbles", 1)
f.speak()
