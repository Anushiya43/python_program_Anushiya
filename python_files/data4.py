import math

integer_num = 10
float_num = 3.14
complex_num=2+3j

name="Anushiya"

fruits=["apple","banana","cherry"]

student={
    "name":"Sneha",
    "age":20,
    "course":"Python Programing"
}

print("\nList of Fruits")
for fruit in fruits:
    print(fruit)
    
if integer_num > 5:
    print(f'\n{name} has a number greater than 5.')
else:
    print(f'\n{name} has a number less than or equal to 5.')

square_root = math.sqrt(float_num)
print(f"\nThe squre root of the {float_num} is {square_root}")

print("\nStudent Information")
print("Name: ",student["name"])
print("Age: ",student["age"])
print("Course: ",student["course"])