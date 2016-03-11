#Vinu Harihar
#Fibonacci Sequence


user_choice_lowerbound = input("Enter the lowest term you want, please")
user_choice_higherbound = input("Enter the highest term you want")
a = int(user_choice_lowerbound)
b = int(user_choice_higherbound)

number1 = 0
number2 = 1
for i in range(a-3):
    number = number1
    number1 = number2
    number2 = number+number2
for i in range (a, b+1):
    if i == 0:
        print (number1, end = " ")
    elif i == 1:
        print (number2, end = " ")
    else:
        number = number1 + number2
        print (number, end = " ")
        number1 = number2
        number2 = number
    
    
