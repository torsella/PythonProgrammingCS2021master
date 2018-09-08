"""HW#1.py: Egyptian Fractions Program - This program reads two integers p and q
from a user and outputs a listing representing a sum of no more than p unit
fractions, with sum equal to p/q."""

__author__ = "Joni Torsella" # Your name
__credits__ = ["https://howchoo.com/g/nddmztjkmwe/dealing-with-fractions-in-python"] # Your list of helpers
__email__ = "joni.torsella@uc.edu" # Your email address

# Describe what user is entering.
print('Egyptian Fractions')
print(' ')
print('At the prompt, enter the numerator, p, and the denominator, q, which you would like to be represented as Egyptian fractions.')

#Import Fraction function.
#from fractions import Fraction
#Note:  I used Python's Fraction function in the first code I wrote.  Then I realized that this Fraction function may not be considered
# as writing the code from "scratch".  So I rewrote my code without the Fraction function.

# Ask user to enter input.
p=int(input('Enter numerator of fraction: '))
q=int(input('Enter denominator of fraction: '))

f_num=p
f_den=q
print('%d/%d'%(f_num,f_den))
print('is equal to the sum of the following fractions: ')

n = 1
while f_num > 0 and f_den > 0:
    if f_num*n>=f_den*1:
        print('1/%d'%n)
        f_num=f_num*n-f_den*1
        f_den=f_den*n
    n=n+1




