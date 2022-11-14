string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

replaced_string = string.replace("!", " ")

replaced_string = replaced_string[:-2] + "."

print(replaced_string)

print(replaced_string.upper())

print(replaced_string[::-1])