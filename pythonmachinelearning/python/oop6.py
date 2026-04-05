#encapsulation in oops
#encapsulation is the bundling of data with the methods that operate on that data
#it restricts direct access to some of an object's components   
#and can prevent the accidental modification of data
class Student:
    def __init__(self, name, age):
        self.__name = name  # private variable
        self.__age = age    # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
# Example usage
student = Student("Alice", 20)
student.display_info()  # Output: Name: Alice, Age: 20
student.set_age(25)
student.display_info()  # Output: Name: Alice, Age: 25
student.set_name("Bob")
student.display_info()  # Output: Name: Bob, Age: 25
student.set_age(-5)  # Output: Age must be positive
# student.__name = "Charlie"  # This will raise an AttributeError
# print(student.__name)  # This will also raise an AttributeError
