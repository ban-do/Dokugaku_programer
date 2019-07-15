class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name

mick = Person("mick Jagger")
dog1 = Dog("hachi","shiba",mick)
print(dog1.owner.name)
