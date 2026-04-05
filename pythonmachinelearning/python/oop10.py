#create a class employee and add salary and increment property to it 
#write a salary after increment method to it with a property decorator with a setter which changes the salary 
class Employee:
    def __init__(self,name , salary):
        self.name=name 
        self._salary=salary

    @property
    def salary(self):
            return self._salary
    @salary.setter
    def salary(self, salary):
            self._salary=salary

    def salary_after_increment(self, increment):
        print("the salary after increment is accessed")
        self._salary+=increment 
        return self._salary
    
user1=Employee("soham", 50000)
print(f"current salary is {user1.salary}")
user1.salary=60000
print(f"new salary is {user1.salary}")
increment=5000
print(f"salary after increment is {user1.salary_after_increment(increment)}")
