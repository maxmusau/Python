# Object Oriented Programming
# object oriented programming langauges:
# C,  C++, Java, Python, Swift etc
# concept of programming that uses objects 
# paradigm that organizes code around objects
# applies classes, attributes/properties, objects, methods/behaviors/function , inheritance,encapsulation 

# class syntax : class (class_name) (parenthesis):
    # class body 
    #attributes, methods
# Rectangle
class Rectangle:
    #init function
    def __init__(self,width,height):
        self.width=width
        self.height=height
    # function to calculate the area of reactangle
    def area(self):
        # formula 
        area_rectangle=self.width * self.height
        print(f"Area of a rectangle with height {self.height} and width {self.width} is {area_rectangle}")
    # another function
    def perimeter(self):
        perimeter_rectangle=self.height + self.width
        print(f"Perimeter of a rectangle with height {self.height} and width {self.width} is {perimeter_rectangle}")
    
# object instantiation
my_object=Rectangle(40,30)
# provide the values of width and height
# my_object.width=40
# my_object.height=30

# calling methods in the object
my_object.area()
my_object.perimeter()

#
