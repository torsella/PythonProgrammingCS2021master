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
from fractions import Fraction

# Ask user to enter input.
p=int(input('Enter numerator of fraction: '))
q=int(input('Enter denominator of fraction: '))

f=Fraction(p,q)
print(f)
print('is equal to the sum of the following fractions: ')

n = 1
while f > 0:
    if f>=Fraction(1,n):
        print(Fraction(1,n))
        f=f-Fraction(1,n)
    n=n+1




