import math

# Use a while loop to stop the program progressing until we get a valid input from the user
# Print to 2 decimal places
while True :
    shape = input("Please enter a shape. SQ for square, RECT for rectangle or ROU for round\n")
    if shape.upper() ==  'SQ' :
        len = float(input("Please enter the length of a side\n"))
        area = pow(len, 2)
        print(round(area, 2))
        break
    elif shape.upper() == 'RECT' :
        len = float(input("Please enter the length of the longest side\n"))
        width = float(input("Please enter the length of the shortest side\n"))
        area = len * width
        print(round(area, 2))
        break
    elif shape.upper() == 'ROU' :
        rad = float(input("Please enter the radius of the circle\n"))
        area = math.pi * (pow(rad, 2))
        print(round(area, 2))
        break
