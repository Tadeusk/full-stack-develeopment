#import ABC 
# Object Oriented Proramming:

class Dog:

    def __init__(self, name, breed, owner):
        self.breed = breed
        self.name = name
        self.owner = owner

    def __str__(self):
        return f"You are printing a dog that is called: {self.name}"

    def bark(self):
        print("Woof Woof")

class Owner:

    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.number = contact_number

owner1 = Owner("James", "Nastrowa 2", "123456789")
owner2 = Owner("Sarah", "Nastrowa 1", "456123345")

dog1 = Dog(name="Bruce", breed="Terrier", owner=owner1)
print(dog1.breed)
print(dog1.name)
print(dog1.owner.name)
#dog1.bark()

dog2 = Dog(name="Freya", breed="Grayhound", owner=owner2)
print(dog2.breed)
print(dog2.name)
print(dog2.owner.name)
print(dog2)
