fav_rest = input("What is your favorite restaurant?\n")

fav_int = int(input("What is your favorite number?\n"))

print(fav_rest)

print(fav_int)

# This cannot cast to an integer as there are letters in the sentence
# For a cast to work there must be only numbers, a mixture or numbers and letters does not work either
int(fav_rest)