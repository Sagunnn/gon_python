class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print("Dog Barks!")
        
    def meow(self):
        print("It's a cat!")

    def getname(self):
        return self.name

d1=Dog("Tiger")
print(d1.getname())
d1.bark()
d1.meow()