#Vinu Harihar
#Airline Baggage Fee Calculator

# inputs
status = input("Are you a Fairview Airlines Premier Status Member? (Y/N): ")
bags = int(input("How many bags are you checking?: "))
international = input("Are you Travelling Internationally? (Y/N): ")
cost = 0

# cost calculations for the number of bags
if (international == "Y" and status == "Y"):
    if bags > 3:
        cost = cost + 100 * (bags - 3)
if (international == "N" and status == "Y"):
    if bags > 2:
        cost = cost + 100 * (bags - 2)
if status == "N":
    if bags == 1:
        cost = cost + 25
    elif bags == 2:
        cost = cost + 60
    else:
        cost = cost + 60 + 100 * (bags - 2)

# for loop for overweight and oversize calculations
for bag in range(1, bags + 1):
    overweight = int(input("What does this bag weigh?: "))
    oversize = input("Is this bag oversize? (Y/N): ")
    
    #calculations for premier status members
    if (status == "Y" and oversize == "N"):
        if (overweight > 70):
            cost = cost + 200
    if (status == "Y" and oversize == "Y"):
        if (overweight > 70):
            cost = cost + 200
        else:
            cost = cost + 100
            
    #calculations for non-premier status members
    if (status == "N" and overweight < 51):
        if oversize == "Y":
            cost = cost + 100
    elif (status == "N" and overweight <= 70):
        cost = cost + 100
    elif (status == "N" and overweight > 70):
        cost = cost + 200

# printing
print ("Your total cost for baggage is $", cost)
    