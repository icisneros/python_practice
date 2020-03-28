def analyze_choice(temp_choice):
	""" Ensures that user only inputs a valid string.
		Valid strings are 'fahrenheit', 'celsius', 'f', or 'c'.
		Capitalization does not matter, but proper spelling does.

		Returns either 'f', or 'c' depending on user's choice.       
    """
	temp_choice = temp_choice.lower()
	
	while(not (temp_choice == 'fahrenheit' or temp_choice == 'celsius' or temp_choice == 'f' or temp_choice == 'c')):
			print '\n\nSorry, that is not a recognized input.  You must input a valid string (either F or C).'
			temp_choice = raw_input('\nWould you like to convert to Fahrenheit or to Celsius?\nWhat')
			temp_choice = analyze_choice(temp_choice)
	
	if temp_choice == 'fahrenheit' or temp_choice == 'f':
		return 'f'
	else:
		return 'c'
		

def analyze_temp(temp):
	""" Ensures that user only inputs a float.
		Inputting a non-numeric string prompts the user to input another choice 
		until a valid query is achieved.

		Returns the float rounded to 2 decimal places       
    """
	while (temp.isalpha()):
		print '\n\nSorry, that is not a recognized input.  You must input a valid float.'
		temp = raw_input('\n\nWhat temperature would you like to convert? (Please input as float)\n')
		temp_choice = analyze_temp(temp)
	return round(float(temp),2)


def cels(temp_F):
	""" Converts temperature from Fahrenheit to Celsius.
		Returns a float rounded to 2 decimal places.       
    """
	return round((temp_F - 32) * (5.0/9.0), 2)


def fahr(temp_C):
	""" Converts temperature from Celsius to Fahrenheit.
		Returns a float rounded to 2 decimal places.      
    """
	return round((temp_C * (9.0/5.0)) + 32, 2)


def main():
    print "\n\n\n******This program converts temperatures from F to C or C to F*****\n\n"
    temp_choice = raw_input('Would you like to convert to Fahrenheit or to Celsius?\n')
    temp_choice = analyze_choice(temp_choice)

    temp = raw_input('\n\nWhat temperature would you like to convert? (Please input as float)\n')
    temp = analyze_temp(temp)
    
    if temp_choice == 'f':
    	answ = fahr(temp)
    	print '\n\nYour given temperature is', answ, 'degrees Fahrenheit'
    elif temp_choice == 'c':
    	answ = cels(temp)
    	print '\n\nYour given temperature is', answ, 'degrees Celsius'

    print '\n\n'

if __name__ == "__main__":
    main()