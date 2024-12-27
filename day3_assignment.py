####1
age = int(25)
print(age)
###2
height = float(65)
print(height)
###3
complexNumber = complex(1+1j)
print(complexNumber)
###4
base = float(input("Enter the base of the triangle :"))
height = float(input("Enter the height of the triangle :"))
area = 0.5*base*height
print("The area of the triangle is : ", area)

###5
a = float(input("Enter side a:"))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a+b+c
print(f"The perimeter of the triangle is {perimeter}")


##6
length = float(input("Enter the length of the rectangle :"))
width = float(input("Enter the  width of the rectangle: "))
area = length*width
perimeter = 2*(length+width)
print("The area of the rectangle is : ", area)
print("The perimiter of the rectanlge is : ", perimeter)

## Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input("Enter the radius of the circle :"))
pi = 3.14
area = pi*radius*radius
circumference = 2 * pi  * radius
print("The area of the circle is: " , area)
print("The circumference of the circle is :", circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope = 2
y_intercept = -2
x_intercept = y_intercept / -slope
print(f"The slope is : {slope}")
print(f"X intercept is : {x_intercept}")
print(f"Y intercept is : {y_intercept}")

##Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

x2,x1 = 6, 2
y2,y1 = 10, 2
slope1  = (y2-y1)/(x2-x1)
distance = math.sqrt(x2-x1)**2 + (y2-y1)**2
print("The slope of the given equation is :", slope)
print(f"The distance between these two points is : {distance}")

##Compare the slopes in tasks 8 and 9.
if slope == slope1:
    print("The slopes from 8 and 9 are equal")
else:
    print("The slopes are not equal")


#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

print("Given equation is y = x^2 + 6x + 9")
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    print(f"For {x} the value of y is {y}")
    if y == 0:
        print(f"The value of y  is 0 at x = {x}")


##Find the length of 'python' and 'dragon' and make a falsy comparison statement.

len('python') > len('dragon')

      
##Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("Check on in python : ", ('on' in 'python') and ('on' in 'dragon'))

##I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("Checking Jargon in the given sentence", 'jargon' in 'I hope this course is not full of jargon')

##There is no 'on' in both dragon and python
print("Checking no in  both dragon and python", ('no' in 'dragon') and ('no' in 'python'))

#Find the length of the text python and convert the value to float and convert it to string
print("The length in the float is :", float(len('python'))) 
print("The length in the string is :", str(len('python')))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = int(input("Enter the number :"))
remainder = number % 2
if remainder == 0:
    print(f"Given number {number} is even")
else:
    print(f"The givennumber {number} is not even")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
a = int(2.7)
floor_division = 7//3
if (a == floor_division):
    print(f"Floor division of 7 by 3 is equal to {a} ")
else:
    {f"Floor division of 7 by 3 is not equal to {a}"}

#Check if type of '10' is equal to type of 10
type1 = type('10')
type2= type(10)
if(type1==type2):
    print("Type of both the data is same")
    print(f"Type of '10' is {type1}")
    print(f"Type of 10 is {type2}")
else:
    print("Type of the data is not same")
    print(f"Type of '10' is {type1}")
    print(f"Type of 10 is {type2}")

#Check if int('9.8') is equal to 10
a = int(float('9.8'))
b = 10
if (a==b):
    print("True. Value of a is :", a , "and value of b is : ", b)

else:
   print("False. Value of a is :", a , "and value of b is : ", b)
    

##Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = int(input("Enter hours: " ))
rate = int(input ("Enter rate per hour :"))
weekly_earning = rate * hour
print("Your weekly earning is :", weekly_earning)

##Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred year

age = int(input("Enter the numbr of years you have lived :"))
age_in_second = age * 365 * 24 * 60 * 60
print(f"You have lived {age_in_second} seconds of you life")

#Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

for i in range (1, 6):
    print(i , 1, i, i**2, i**3, sep="\t")