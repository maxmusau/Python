# Object Oriented Programming
# Triangle
class Triangle:
    def __init__(self,height,base):
        self.height=height
        self.base=base
    # methods
    def Area_rectangle(self):
        # formula 1/2 *base*height
        area=1/2 *self.height*self.base
        print(f"Height= {self.height} \n base= {self.base} \n Area= {area}")
        
    # create a function to calculate the perimeter
    def Perimeter(self):
        # hypotenuse **2= height **2 + (1/2*base)**2
        H2=self.height**2 + (0.5*self.base)**2
        import math
        H=math.sqrt(H2)
        print("H2= ",H2)
        print("H= ",H)
        perimeter=H + H+ self.base
        print(f"base= {self.base} \n Hypotenuse= {H} \n Perimeter= {perimeter}")
    
# create the object
triangle_object=Triangle(20, 40)
# call the function
triangle_object.Area_rectangle()
triangle_object.Perimeter()