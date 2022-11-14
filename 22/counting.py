char_occurrence = {}

test_str = "google.com"

# Iterate over the string with a nested loop
# Starting at the first char, we iterate over the rest of the string until we find the same char
# When we do, we add it to the dictionary
# If we the char we are looking at is already in the dictionary, we can skip the iteration. We can check this using the key
for i in range(len(test_str)) :
    num_of_same_char = 0
    for j in range(len(test_str)) :
        char_found = test_str[i]
        if char_found in char_occurrence :
            break
        elif test_str[i] == test_str[j] :
            num_of_same_char += 1
    char_occurrence[char_found] = num_of_same_char
    num_of_same_char = 0
    
print(char_occurrence)
