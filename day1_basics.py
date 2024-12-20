import math
# Define global variables
a = 0
b = 0

def get_inputs():
    global a, b
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

def addition():
    c = a + b
    print(f"The sum of {a} and {b} is {c}")

def subtraction():
    c = a - b
    print(f"The difference of {a} and {b} is {c}")

def multiplication():
    c = a * b
    print(f"The multiplication of {a} and {b} is {c}")

def division():
    if b != 0:  # Handle division by zero
        c = a / b
        print(f"The division of {a} by {b} is {c}")
    else:
        print("Error: Division by zero is not allowed.")
def modulus():
    c = a % b
    print(f"The modulus of {a} and {b} is {c}")
def exponential():
    c = a ** b
    print(f"The exponential value of {a} and {b} is {c}")
def floorDivision():
    c = a//b
    print(f"The floor division of {a} and {b} is {c}")

def string():
    print("Aayush Koirala")
    print("Kathmandu, Nepal")
    print("I am enjoying the 30 days of python")
def checkDataType():
    a = 15
    print(type(a))

def printArray():
    a = {"Aayush", "Koirala", "Nuwakot"}
    print(a)

def complexNumber():
    a = 1 + 5j
    print(f"The given complex number is {a}")
    print(type(a))
def euclidianDistance():
    point1 = (2, 3)
    point2 = (10, 8)
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    print(f"The Euclidean distance between {point1} and {point2} is: {distance}")
    distance1 = math.sqrt((point2[0] - point1[0])**2 + (point2[1]-point1[0])**2)
    print(f"The distance from method2 is {distance1}")

get_inputs()
addition()
subtraction()
multiplication()
division()
modulus()
exponential()
floorDivision()
string()
checkDataType()
printArray()
complexNumber()
euclidianDistance()
