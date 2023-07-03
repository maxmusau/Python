# calculate the area of a circle 
radius=int(input("Enter Radius: "))
PI=3.14
Area_circle=PI*radius**2 #exponentiation
print(f"The area of a circle with radius {radius}m is {Area_circle}m2")

# find the area of a triangle provided; 
# area_triangle=1/2*base*height
base=int(input("Enter base value: "))
height=int(input("Enter height value: "))
area_triangle=1/2 * base *height
print(f"The area of a Triangle with base {base} and height {height} is {area_triangle}")

print(type(area_triangle))

