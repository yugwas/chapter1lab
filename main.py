import math

# 1.1 Part A 
fahrenheit = input("Enter temperature in Fahrenheit:  ")
fahrenheit = float(fahrenheit)
celsius = (5/9) * (fahrenheit - 32)
print("The temperature in Celsius:", round(celsius, 2), '\n')


# 1.2 Part B
height = input("Enter the height of the trapezoid:  ")
bottom_base_length = input("Enter the length of the bottom base:  ")
top_base_length = input("Enter the length of the top base:  ")
height = float(height)
bottom_base_length = float(bottom_base_length)
top_base_length = float(top_base_length)
area_of_trapezoid = (1/2) * (bottom_base_length + top_base_length) * (height)
print("The area is:", round(area_of_trapezoid, 2), '\n')


# 1.3 Part C
radius = input("Enter the radius of the circle:  ")
radius = float(radius)
area_of_circle = (math.pi) * (radius)**2
print ("The area is:", round(area_of_circle, 2), '\n')

# Mr. Heine said I got 9 points.