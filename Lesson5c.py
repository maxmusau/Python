# program  to check if triangle is equilateral, isosceles,scalene
# equilateral= all the sides are equal
# isosceles= two sides are equal
# scalene= no side is equal to the other
S1=int(input("Enter value of side 1: "))
S2=int(input("Enter value of side 2: "))
S3=int(input("Enter value of side 3: "))
# equilateral
if S1==S2==S3:
    print("equilateral")
    #isosceles
elif S1==S2 or S2==S3  or S1==S3:
  print("isosceles")
else:
    print("scalene")
