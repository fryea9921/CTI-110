# Aiden Frye
# 9/14/2026
# Calculations of a circle

#Import the value for pi
from math import pi

# Get radius from the user
radius = input("Enter the radius: ")

# Show the data type of the radius and print the value and type of pi
print(type(radius))
print(f"The value of pi is: {pi:.8f}")
print(type(pi))

#Convert raidus to a float
radius = float(radius)

print()
# Show the data type of the radius
print(type(radius))

# Calculate the Diameter
diameter = 2 * radius

#Display diameter using an f-string(Formatted string)
print(f"The diameter of the circle is: {diameter:.1f}")

#Calculate the Circumference
Circumference = 2 * radius * pi

print()
print(f"The circumference of a circle is: {Circumference:.2f}")

#Calculate the Area of the circle
Area = pi * radius ** 2

# Display the Area of the circle
print()
print(f"The Area of the circle is: {Area:.2f}")

# Loop the program(A neat addition I figured out while tinkering with the code)
while True:
    #Import the value for pi
    from math import pi

    # Get radius from the user
    radius = input("Enter the radius: ")

    # Show the data type of the radius and print the value and type of pi
    print(type(radius))
    print(f"The value of pi is: {pi:.8f}")
    print(type(pi))

    #Convert raidus to a float
    radius = float(radius)

    print()
    # Show the data type of the radius
    print(type(radius))

    # Calculate the Diameter
    diameter = 2 * radius

    #Display diameter using an f-string(Formatted string)
    print(f"The diameter of the circle is: {diameter:.1f}")

    #Calculate the Circumference
    Circumference = 2 * radius * pi

    print()
    print(f"The circumference of a circle is: {Circumference:.2f}")

    #Calculate the Area of the circle
    Area = pi * radius ** 2

    # Display the Area of the circle
    print()
    print(f"The Area of the circle is: {Area:.2f}")

