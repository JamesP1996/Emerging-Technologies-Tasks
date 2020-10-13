#Newton Rashad Method
# Returns the square root of n. 
# Note that the function  
def squareRoot(n): 
    # We are using n itself as 
    # initial approximation (It is accurate but not fully)
        x = int(n) 
        y = int(1.00000)
          
        # accuracy decides the accuracy/precision level 
        accuracy = 0.100
        while(x - y > accuracy): 
      
            x = (x + y) // 2
            y = n // x 
      
        return int(x) 

# Set N to a high integer value where the values are pushed to the left
n = 2 * 10 ** 200

# Print the Square root of 2. fString explanation = squareRoot of 2 function floor divide(integer divide) by 10*100 
# and then add a . and then get the numbers after decimal in this case our function's 
# Remainder after being divided by 10 to the power of 100 to 100 decimal places 
print(f'Square Root of 2 to 100 Decimal Places : {squareRoot(n) // 10**100}.{squareRoot(n) % 10**100 :100d}')

