#accessing and modifying data in OOP
#1: by making the data provate and use getters and setters 
from datetime import datetime
class user:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
        #we can use the _ to make the data protected , it tells the python developer that this is a protected variable
        #and it should not be accessed directly outside the class and it is trusted that python developers will not access the protected variables 
        #we use __ instead of _ to make the data private and it is not accessible outside the class
        #getters and setters are used to access and modify the private data fields
    def get_username(self):
        print(f"email accessed at {datetime.now()}")
        return self.__username
    
    def set_username(self, username):
        self.__username = username

    def get_email(self):
        print(f"email accessed at {datetime.now()}")
        return self.__email
    
    def set_email(self, email):
        #validation logic for email
    
        if "@" not in email:
            raise ValueError("Invalid email address")
        if not email.endswith(".com"):
            raise ValueError("Email must end with .com")
        if len(email) < 5:
            raise ValueError("Email must be at least 5 characters long")
        if len(email) > 50:
            raise ValueError("Email must be at most 50 characters long")
        print(f"email changed at {datetime.now()}")
        self.__email = email

user1 = user("alice", "alice@gmail.com ", "123")
print(user1.get_username())
user1.set_username("alice2004")
print(user1.get_username())


user2=user("bob", "bob@gmail.com", "456")
print(user2.get_email())
email=input("Enter new email for bob: ")
user2.set_email(email)
print(user2.get_email())
#why do we use getters and setters when we can access the data directly?
#1: it provides a way to control access to the data fields
#2: it allows us to add validation logic when setting the data fields
#3: it allows us to change the implementation of the class without affecting the code that uses the class
#4: it provides a way to encapsulate the data and hide the implementation details
#5: it allows us to add additional functionality when getting or setting the data fields
















