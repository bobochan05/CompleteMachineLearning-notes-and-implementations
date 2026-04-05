#abstraction 
#reduce complexity by hiding details 
#a user who wants to send an email only needs to know how to call the send method 
class sendemail:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def _connect(self):
        print(f"connecting to email server for {self.username}")

    def _authenticate(self):
        print(f"authenticating...")

    def connected(self):
        self._connect()
        self._authenticate()
        print(f"{self.username} is connected to the email server")

    def send(self,toemail,subject,body):
       
        print(f"Sending email to {toemail} with subject '{subject}' and body '{body}' from {self.email}")

username1=input("Enter your username: ")
email1=input("Enter your email: ")
user1=sendemail(username1,email1)
user1.connected()
sentto=input("Enter the email address to send to: ")
subject=input("Enter the subject of the email: ")
body=input("Enter the body of the email: ")

user1.send(sentto, subject, body)




    
    





        
    
    
