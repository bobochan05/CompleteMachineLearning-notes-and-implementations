#create a class vector and a subclass vector3D
# The vector class should have x and y components, and the vector3D class should have x, y, and z components.
class vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def add(self):
        print(f"the 2D vector is {self.x}i + {self.y}j")

class vector3D(vector):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def v3D(self):
        print(f"the 3D vextor is {self.x}i + {self.y}j + {self.z}k")

x=input("Enter the x component of the vector: ")
y=input("Enter the y component of the vector: ")
z=input("Enter the z component of the vector: ")
try:
    x==int(x) , y==int(y), z==int(z)
    v2d=vector(x,y)
    v3d=vector3D(x,y,z)
    v2d.add()
    v3d.v3D()
except ValueError:
    print("Please enter valid numbers for the vector components.")





    

