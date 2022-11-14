import re

file = open('19/docs/DOB.txt', 'r')

name = ""
birthdate = ""

# Split the line into a list 
# Push the first 2 words into name
# Push the last 3 words into birthdate
# I feel like there is too much hardcoding. Other attempt below

#for line in file :
#    line_split = line.split()
#    for i in range(2) :
#        name += line_split[i] + " "
#    name += "\n"
#    for i in range(3) :
#        birthdate += line_split[i + 2] + " "
#    birthdate += "\n"
#


# Iterate over every line in the file
# Cast each line to a list
# Iterate over the list
# Check if the the current word is a word and not a number
# If it is, push the current word to name
# If we find a number, push the next 3 words to birthdate and then break the loop
for line in file :
    line_split = line.split()
    for i in range(len(line_split)) :
        if re.findall("[a-zA-Z]", line_split[i]) :
            name += line_split[i] + " "
        elif re.findall("[0-9]", line_split[i]) :
            name += "\n"
            for i in range(3) :
                birthdate += line_split[i + 2] + " "
            birthdate += "\n"
            break

file.close()

print("\033[1m" + "Name" + "\033[0m")
print(name)

print()

print("\033[1m" + "Birthdate" + "\033[0m")
print(birthdate)