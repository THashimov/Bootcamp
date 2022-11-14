num1 = input("Please enter a number \n")
num2 = input("Please enter a number \n")

print(num1 + " " + num2)

tmp_num = num2

num2 = num1
num1 = tmp_num

print(num1 + " " + num2)
