# 6. WAP to calculate the area of triangle, rectangle, circle, sphere.
import math

print("Select a shape to calculate its area:")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle")
print("4. Sphere (Surface Area)")

choice = input("Enter your choice")

if choice == '1':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
elif choice == '2':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
elif choice == '3':
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area}")
elif choice == '4':
    radius = float(input("Enter the radius of the sphere: "))
    surface_area = 4 * math.pi * (radius ** 2)
    print(f"The surface area of the sphere is: {surface_area}")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
