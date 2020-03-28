#!/usr/bin/env python
from math import log

def H(n):
    """Returns an approximate value of n-th harmonic number.

       http://en.wikipedia.org/wiki/Harmonic_number
    """
    # Euler-Mascheroni constant
    gamma = 0.57721566490153286060651209008240243104215933593992
    return gamma + log(n) + 0.5/n - 1./(12*n**2) + 1./(120*n**4)


def main():
    print "\n******This program gives you the n-th harmonic number*****\n"
    number = input('What harmonic number would you like?\n\n')
    if number < 1:
        while(number < 1):
            number = input('You must input an integer greater than or equal to 1 \n\n')
    answ = H(number)
    print "\nOh, it is %s\n" % answ


if __name__ == "__main__":
    main()