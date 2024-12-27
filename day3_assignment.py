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





