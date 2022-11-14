import re

user_str = input("Please enter a sentence\n")

valid_input = False

# Check that the user has only entered characters and not numbers
print("Which characters would you like to delete?")
while valid_input == False :
    chars_to_del = input()
    if re.findall("[0-9]", chars_to_del) :
        print("Invalid input, please enter only characters")
    else :
        # Convert the chars to delete into a list so we can access each number individually
        chars_to_del = chars_to_del.split()

        while True :
            # Iterate over all the chars 
            # If the len of any of the chars is more than 1, then the char is not a single character so we break the loop which breaks the outer loop, running everything again
            for i in range(len(chars_to_del)) :
                if len(chars_to_del[i]) > 1 :
                    print("Invalid input, please enter only characters")
                    break
                # If i == number of chars then we must have iterated over all of them
                # That means we can break out of the loop
                if i == len(chars_to_del) - 1 :
                    valid_input = True
            break
        

# Create a function which takes a string and a char as arguments and then deletes them
def del_char(string, char) :
    return user_str.replace(char, "")

# Run for every char we want to delete
# Pass the original string as an arg along with the char we want to delete
# Save the returned string to user_str and then pass it into the function again with the next char
# Kind of like a recursive function but not quite
for i in range(len(chars_to_del)) :
    user_str = del_char(user_str, chars_to_del[i])


print(user_str)