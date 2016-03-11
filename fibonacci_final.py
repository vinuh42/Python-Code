#Vinu Harihar
#Fibonacci Sequence

number1 = 0
number2 = 1
for i in range(25):
    number = number1
    number1 = number2
    number2 = number+number2
    print (number, end = " ")