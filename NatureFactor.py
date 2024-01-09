def printDivisors(n) : 
    i = 1
    while i <= n : 
        if (n % i==0) : 
            print (i,end=" ") 
        i = i + 1
          
# Driver method 
print ("The divisors of 100 are: ") 
printDivisors(100)

import math 
  
# Method to print the divisors 
  
  
def printDivisors(n): 
    list = [] 
  
    # List to store half of the divisors 
    for i in range(1, int(math.sqrt(n) + 1)): 
  
        if (n % i == 0): 
  
            # Check if divisors are equal 
            if (n / i == i): 
                print(i, end=" ") 
            else: 
                # Otherwise print both 
                print(i, end=" ") 
                list.append(int(n / i)) 
  
    # The list will be printed in reverse 
    for i in list[::-1]: 
        print(i, end=" ") 
  
  
# Driver method 
printDivisors(100) 
print("The divisors of 100 are: ") 


