import math

len_one = int(input("Enter the length of one side of a triangle "))
len_two = int(input("Enter the length of another side of a triangle "))
len_three = int(input("Enter the length of the last side of a triangle "))

# We will use herons formula for this

perimeter = int((len_one + len_two + len_three) / 2)

area = math.sqrt(perimeter * (perimeter - len_one) * (perimeter - len_two) * (perimeter - len_three))

print(area)