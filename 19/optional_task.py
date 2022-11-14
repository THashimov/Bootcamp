import re

file = open('19/docs/input.txt', 'r')

num_of_lines = 0
num_of_words = 0
num_of_chars = 0
num_of_vowels = 0
vowels = "[aeiouAEIOU]"

# Iterate over each line and increment num_of_lines at the end of the loop
# Split the line into a list of words so we can iterate over the words and increment num_of_words
# Repeat step above for chars
# This ignores any white space characters
for line in file :
    words = line.split()
    for i in words :
        num_of_words += 1
        for k in i :
            num_of_chars += 1
            if re.search(vowels, k) :
                num_of_vowels += 1
    num_of_lines += 1

file.close()

print(num_of_chars)
print(num_of_words)
print(num_of_lines)
print(num_of_vowels)
