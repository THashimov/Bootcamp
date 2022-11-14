import math

user_nums = []

# While there are less than 10 values in the list, run loop
# Ask user to enter a number
# Try cast it as a float
# If successful, push to the list
# If not, ask user to try again

print("Please enter a number")
while len(user_nums) < 10 :
    num = input()
    try :
        float(num)
        user_nums.append(float(num))
        print("Please enter another number")
    except :
        print("Invalid input, please enter a number")


# Print the sum of all numbers in the list
print(sum(user_nums))

# Print highest value and index
print(f"Highest number: {max(user_nums)} at index: {user_nums.index(max(user_nums))}")

# Print lowest number and index
print(f"Lowest number: {min(user_nums)} at index: {user_nums.index(min(user_nums))}")

# Print the average and round to 2 decimal points
print(f"The average of all the numbers in the list is: {round(sum(user_nums) / len(user_nums), 2)}")

# Find the median and print it
# Sort the user nums 
# Get the length of the list and divide by 2 to find the middle
# Print the number in that index
user_nums.sort()
index = int(len(user_nums) / 2) 
print(f"The median number is: {user_nums[index]}")