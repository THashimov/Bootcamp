num = int(input("Please enter a number\n"))

if num % 2 == 0 and num % 5 == 0 :
    print("The number you selected is divisible by 2 and 5")
elif num % 2 == 0 or num % 5 == 0 :
    print("The number you selected is divisible by 2 or 5")
else :
    print("The number you selected is not divisible by 2 or 5")