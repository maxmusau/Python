# Arithmetic caculations
# input function
name=input("Enter name of the student: ")
print(type(name))
maths=int(input("Enter marks for maths: "))
english=int(input("Enter marks for english: "))
science=int(input("Enter marks for science: "))
kiswahili=int(input("Enter marks for kiswahili: "))
sost=int(input("Enter marks for sost: "))
# formula
total_marks=maths+english+science+kiswahili+sost
# output
print(f"{name} scored {total_marks} marks in the closing exams")


