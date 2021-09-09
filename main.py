import math

# 1.1 Part A 
fahrenheit = float(input("Enter temperature in Fahrenheit:  "))
celsius = (5/9) * (fahrenheit - 32)
print("The temperature in Celsius:", round(celsius, 2), '\n')

# 1.2 Part B
height = float(input("Enter the height of the trapezoid:  "))
bottom_base_length = float(input("Enter the length of the bottom base:  "))
top_base_length = float(input("Enter the length of the top base:  "))
area_of_trapezoid = (1/2) * (bottom_base_length + top_base_length) * (height)
print("The area is:", round(area_of_trapezoid, 2), '\n')

# 1.3 Part C
radius = float(input("Enter the radius of the circle:  "))
area_of_circle = (math.pi) * (radius)**2
print ("The area is:", round(area_of_circle, 2), '\n')
