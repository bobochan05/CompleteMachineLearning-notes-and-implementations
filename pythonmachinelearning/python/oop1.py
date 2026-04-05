#Object oriented programming in python is a programming paradigm that uses objects and classes to structure code
#objects are instances of classes and classes are blueprints for creating objects
#class is created using the class keyword followed by the class name
class Dog:
#__init__ is a special method that is called when an object is created 
    def __init__(self, name , age):
    #self is a reference to the current instance of the class
     #it is used to access variables that belong to the class
      self.name = name
      self.age = age

    def bark(self):
        print(f"{self.name} of age {self.age} says Woof!")

dog1=Dog("Buddy", 3)
dog1.bark()
dog2=Dog("Max", 5)
dog2.bark()

#we add datafields to the class using the __init__ method
#we can create multiple objects of the same class with different data
#each object has its own set of data fields
#we can call methods on the objects to perform actions

class owner:
    def __init__(self, name, dog):
       self.name = name
       self.dog = dog
    def introduce(self):
        print(f"My name is {self.name} and this is my dog {self.dog.name} who is {self.dog.age} years old.")

owner1 = owner("Alice", dog1)
owner1.introduce()



