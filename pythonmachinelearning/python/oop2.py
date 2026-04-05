class P:
    def __init__(self, name,age):
     self.name = name
     self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
person1 = P("John", 30)
person1.greet()
person2 = P("Jane", 25)
person2.greet()

#accessing and modifying data in OOP
class user:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self , user ):
        print(f"sending message to {user.username} at {user.email} from {self.username}.")

user1 = user("alice", "alice2004@gmail.com")
user2 = user("bob", "bob2005@gmail.com")
user1.greet(user2)
user2.greet(user1)

#modifying data fields
user1.email = "alice204@gmail.com"
user2.email = "bob205@gamil.com"
user1.greet(user2)
user2.greet(user1)
