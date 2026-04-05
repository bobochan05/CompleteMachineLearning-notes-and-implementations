#static attributes 
#a static attribute(also known as a class attribute) is an attribute that is shared by all instances of a class.
#it is defined within the class but outside of any instance methods
#it is accessed using the class name or an instance of the class
#it is useful for storing data that is common to all instances of the class
#it can be accessed using the class name or an instance of the class
#it is defined using the class name followed by the attribute name

class user:
    user_count=0 #static attribute

    def __init__(self, username, email):
        self.username=0
        self.email=email
        user.user_count += 1 #increment the user count when a new user is created

    def display(self):
        print(f"Username: {self.username}, Email: {self.email}")
        print(f"Total users: {user.user_count}")

user1 = user("soham","bobo@gmail.com")
user2 = user("alice","slice@gmail.com")
print(user.user_count) #accessing static attribute using class name

#static methods 
#a static method is a method that belongs to the class raer than an instance of the class 
#it is defined using the @staticmethod decorator 
#it does not take the self parameter and cannot access instance attributes or methods
#it is used for utility functions that do not require access to instance data
#for example a static method can be used to perform a calculation or to validate data 
class Bank:
    min_balance =100

    def __init__(self, name ,balance):
        self.balance = balance
        self.name=name
    
    def deposit(self, amount):
    
        
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

user1 = Bank("Soham", 500)
user1.deposit(200)

#when to use static methods:
#1. When the method does not need to access or modify instance-specific data.
#2. When the method is a utility function that is related to the class but does not require instance data.
#3. When you want to group related functions together within a class for better organization.
#4. When you want to provide a method that can be called without creating an instance of the class.






