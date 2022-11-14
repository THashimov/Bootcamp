import re

print("Please enter a word")

# Ensure user only enters a word
# Check for any spaces and any numbers
# Only break the loop if the regex is false
while True :
    user_str = input()
    if re.findall(" ", user_str.strip()) :
        print("Invalid input. Please enter a single word")
    elif re.findall("[0-9]", user_str) :
        print("Invalid input. Please enter a single word")
    else :
        break

# Create a new string which is the a reversed copy of the original
user_str_rev = user_str[::-1]

if user_str_rev == user_str :
    print(f"The word {user_str} is a palindrome")
else :
    print(f"The word {user_str} is not a palindrome")
