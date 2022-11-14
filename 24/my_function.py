def print_days_of_the_week() :
    print("Monday")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("Friday")
    print("Saturday")
    print("Sunday")


print_days_of_the_week()

# Split the sentence into a list
# If I is odd, replace the word with hello
def replace_words(string) :
    words = string.split()
    for i in range(len(words)) :
        if i % 2 != 0 :
            words[i] = "hello"
    print(" ".join(words))


replace_words("Who is this person over here")