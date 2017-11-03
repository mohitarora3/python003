def increment(i):
    '''
    objective:to increment the value of a number
    input parameters:i-a number which value is to be incremented
    approach:using addition operator
             (+)
    '''
    i+=1
    return i
    
def sum(x,y):
    '''
    objective:to add two numbers
    input parameteres:
         x-first number
         y-second number
    approach-use the function increment and recursion
    return value-sum of the two numbers
    '''
    for i in range(0,y):
            j=increment(x)
            x=j
    return x
