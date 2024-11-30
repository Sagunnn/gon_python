class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name)
        
class Cat(Pet):
    def speak(self):
        print("Meowing")
        
class Dog(Pet):
    def speak(self):
        print("Barking")
        
d=Dog("Tim",20)
c=Cat("Bob",32)
d.display()
c.display()
d.speak()
c.speak()    