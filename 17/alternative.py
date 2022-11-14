string = "Hello World"

# Store the string as a list of chars
split_str = list(string)

# Iterate over each char and if the index is even, convert the char to uppercase
for i in range(len(split_str)) :
    if i % 2 == 0 :
        split_str[i] = split_str[i].upper()

# Join the chars without spaces between them
string = "".join(split_str)

print(string)

string = "I am learning to code"

split_str = string.split()

# Same as above except we split the word into separate words rather than chars
# If index is odd, convert that word to upper case, else, convert to lower case
for i in range(len(split_str)) :
    if i % 2 != 0 :
        split_str[i] = split_str[i].upper()
    else :
        split_str[i] = split_str[i].lower()


# Join the words with a space between each word
string = " ".join(split_str)

print(string)