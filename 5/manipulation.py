str_manip = input("Please type a sentence\n")

print(f"Length of sentence is {len(str_manip)}")

last_char = str_manip[len(str_manip)-1]

print(str_manip.replace(last_char, "@"))

last_three_chars = str_manip[len(str_manip) - 3 :: 1]

print(last_three_chars[::-1])

first_three_chars = str_manip[:3]

last_two_chars = str_manip[len(str_manip) - 2 :: 1]

print(first_three_chars + last_two_chars)

# Oops, totally missed the last part! 

print(str_manip.replace(" ", '\n'))