# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

import re

# Missing parenthesis. New line escape is in a new print statement, this forces 2 new lines. Removed as it's unnecessary
print ("Welcome to the error program")
# Incorrect indentation
# AgeStr is not defined, change == to =
ageStr = "24 years old"

# Incorrect indentation
# Cannot cast a string of letters to an integer    
# Use a regex to find any number in the string
# Get all the numbers in the list and join them into a string
# We can now cast it to an int
regex = "[0-9]"
nums = re.findall(regex, ageStr)
age = "".join(nums)

# Incorrect indentation
# Space after I'm and before years old
print("I'm " + age + " years old.")

# Incorrect indentation
# Not really sure why this is even here
#three = "3"

# This will just convert age to a string and then add 3 to the end of the string, returning 243
#answerYears = age + three

answerYears = age

# Missing parenthesis
# Remove quotes on answerYears
print("The total number of years: " + answerYears)

# Answer does not exist. This should be age * 12
# use of undeclared variable
answerMonths = int(age) * 12

# We need to add 3 years and 6 months to our answer
answerMonths += (3 * 12) + 6

# Missing parenthesis
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")

#HINT, 330 months is the correct answer

