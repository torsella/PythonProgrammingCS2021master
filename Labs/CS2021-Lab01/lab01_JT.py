"""Required questions for lab 1"""
__author__ = "Joni Torsella" # Your name
__credits__ = ["NA"] # Your list of helpers
__email__ = "joni.torsella@uc.edu" # Your email address


## Boolean Operators ##

# Q4
"""Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
"*** YOUR CODE HERE ***"
def both_positive(x, y):
    if x > 0 and y > 0:
        print('True')
        print('x=%d and y=%d are both positive' % (x,y))
    else:
        print('False')
        print('x=%d and y=%d are NOT both positive' % (x,y))
    return x and y > 0

x=int(input('Enter an x value: '))
y=int(input('Enter a y value: '))
both_positive(x,y)


## while Loops ##

# Q9
 """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
def factors(n):
    
   
    count=n
    while count>=1:
        if n%count==0:
            factor=count
            print(factor)
        count=count-1


n=int(input('Enter a number to be factored: '))
factors(n)




# Q10
def fib(n):
    a=0
    b=1
    c=a+b
    if n==0:
        fibsum=a
    elif n==1:
        fibsum=b
    else:
        count=2
        a=1
        b=1
        fibsum=b
        while count<n:
            count=count+1
            if n==2:
                fibsum=b
            else:
                c=a+b
                fibsum=c
                a=b
                b=c
    return fibsum


    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    "*** YOUR CODE HERE ***"
