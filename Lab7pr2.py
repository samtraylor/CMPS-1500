import time
def F(n):
    '''
    Code to recursively find and return the n-th number in the fibbonaci sequence

    Keyword arguments:
    n -- an integer representing how deep you want the fibonacci sequence to go

    '''
    if n == 0: #two-part base case
        return 0
    if n == 1:
        return 1
    else:
        return F(n-1) + F(n-2) #recursive case
    

def f(n):
    '''
    Code to find and return n-th fibonacci number using iteration

    Keyword arguments:
    n -- an integer representing how deep you want the fibonacci sequence to go

    '''
    fibonacci = [0,1] 
    x = 2
    while len(fibonacci) != n + 1:
        fibonacci.append(fibonacci[x-1] + fibonacci[x-2])
        x += 1
    return fibonacci[-1]

t = time.time()
print(F(40))
t1 = time.time()
print(round(t1-t,6))


