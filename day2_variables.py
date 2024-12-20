# Variables and Built in functions

first_name = 'Aayush'
last_name = 'Koirala'
country = 'Nepal'
city = 'Kathmandu'
age = 20
is_graduated = True
skills = ['HTML', 'CSS', 'React', 'Python', 'Sailpoint'] 
basic_info = {
    'first_name' : 'Aayush',
    'last_name' : 'Koirala',
    'country' : 'Nepal',
    'City' : 'Kathmandu',
    'Age' : 20,
    'is_Graduated' : True,
    'Skills' : ['Java' , 'Python']
} 

print('First name' , first_name)
print('Last name', last_name)
print('Country', country)
print('City', city)
print('Age', age)
print('Graduated ?', is_graduated)
print('Skills ', skills)
print('Users Basic Information is: ', basic_info)

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_graduated))
print(type(skills))
print(type(basic_info))

def radiusOfCircle():
    pi = 3.14
    radius = 30
    area = pi *(radius**2)
    circumference = 2*pi*radius
    print("The area of the circle is  : ", area)
    print("The circumference of the circle is :", circumference)

def areaOfRectangle():
    a = float(input("Enter Length of the Rectangle : "))
    b = float(input("Enter bredth of the Rectangle : "))
    Area = a*b
    print("The area of the Rectangle is :", Area)


areaOfRectangle()
radiusOfCircle()


