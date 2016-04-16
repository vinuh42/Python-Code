#Vinu Harihar

def pow(base, exponent):
    product = base
    for n in range(exponent-1):
        product = product * base
        return (product)
    
numofdays = int(input("How many days to double your penny?: "))
money = pow(2, numofdays - 1)
print ("After", numofdays, "days, you have: ", money)