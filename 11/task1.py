num1 = 10
num2 = 11
num3 = 12

if num1 > num2 :
    print(num1)
else :
    print(num2)

if num1 % 2 == 0 :
    print("Number is even")
else :
    print("Number is odd")

if num1 > num2 and num1 > num3 :
    high_num = num1
    if num2 > num3 :
        mid_num = num2
        low_num = num3 
    else :
        mid_num = num3
        low_num = num2
elif num2 > num1 and num2 > num3 :
    high_num = num2
    if num1 > num3 :
        mid_num = num1
        low_num = num3
    else :
        mid_num = num3
        low_num = num2
else :
    high_num = num3  
    if num1 > num2 :
        mid_num = num1
        low_num = num2
    else :
        mid_num = num2
        low_num = num1

print(f"{high_num} {mid_num} {low_num}")