# Vinu Harihar
# Math Library Exercises
import math

# functions
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)+(y2-y1))
    return(dist)
    
def slope(x1, y1, x2, y2):
    slp = (y2-y1) / (x2-x1)
    return(slp)
    
def quadroot1(A, B, C):
    if (B*B - (4*A*C)) <= 0:
        return("No Solution")
    else:
        root = ((0-B) + math.sqrt((B*B) - (4*A*C)))/(2*A)
        return(root)
    
def quadroot2(A, B, C):
    if (B*B - (4*A*C)) <= 0:
        return("No Solution")
    else:
        root = ((0-B) - math.sqrt((B*B) - (4*A*C)))/(2*A)
        return(root)

# main script
print(distance(2, 3, 3, 4))
print(slope(2, 3, 6, 5))
print(quadroot1(1, 4, 3))
print(quadroot2(1, 4, 3))

