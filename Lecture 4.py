# Lecture 4
def f(x):
    y = 1
    x = x + y
    print ('x = ' + str(x))
    return x

x = 3
y = 2
z = f(x)

# L4 Problem 5
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise (i.e., x > lo and x < hi)
    '''
    return min(max(lo, x), hi)
    
