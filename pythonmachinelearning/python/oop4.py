#using python properties to access and modify data and make data private or protected 
class user:
        def __init__(self, username, email, password):
         self.__username = username
         self.__email = email
         self.__password = password
        #we can use the _ to make the data protected , it tells the python developer that this is a protected variable
        #property decorators are used to access and modify the private data fields 
        #getter property is used to access the provate data field 
        @property
        def email(self):
            print("email accessed ")
            return self.__email
        
        @email.setter
        def email(self, email):
            self.__email=email

            
            
user2=user("B","B204@gmailcom", "456")
print(user2.email)
user2.email="this is not an email"
print(user2.email)

