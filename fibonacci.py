import scipy.constants
import math


def fib(number):
	if number == 1 or number == 2:
		return 1
	else:
		return fib(number-1) + fib(number-2)
    
    
def fib_cfs(number):
    ''' The closed form solution implementation of a fibonacci number finder
    '''
    phi = scipy.constants.golden
    psi = float(-1/phi)
    return (pow(phi,number) - pow(psi,number))/math.sqrt(5)
    

def main():
	print("\n******This program gives you the n-th Fibonacci number*****\n")
	number = int(input('What Fibonacci number would you like?\n\n'))
	if number < 1:
		while(number < 1):
			number = input('You must input an integer greater than or equal to 1 \n\n')
	answ = fib_cfs(number)
	print("\nOh, it is: " + str(int(answ)) + "\n")


if __name__ == "__main__":
    main()
