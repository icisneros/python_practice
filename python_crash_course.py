

if __name__ == "__main__":
    
    # ========================================================================
    # Print statements
    # ========================================================================
    print("\nPrint statements ===============================")
    
    # can multiple (replicate) a string using multiplication and print it
    viking_song = "Spam" * 5
    print(viking_song)
    # can print out the output of a function
    spam_amount = 0
    print(type(spam_amount))
    print(type(19.95))
    # can use commas to separate print out objects
    h_meters = 1.2
    print("Heigh in meters = ", h_meters, "?")
    
    
    
    # ========================================================================
    # Functions
    # ========================================================================
    print("\nFunctions ===============================")
    
    # can use help function to get documentation on other functions
    help(round) # remember to only pass in the function name and nothing else
    
    # a function is defined thusly:
    def least_difference(a,b,c):
        """
        Parameters
        ----------
        a : int
        b : int
        c : int

        Returns
        -------
        int
            returns the smallest difference between any two numbers among
            a, b, and c.

        """
        diff1 = abs(a - b)
        diff2 = abs(a - c)
        diff3 = abs(b - c)
        return min(diff1, diff2, diff3)
    # we also include docstrings using """ for documentation purposes
    # we can now see it using help function
    help(least_difference)
    
    # functions can have optional arguments with a default in quotes
    def greeting(who="Ivan"):
        print("Hello", who)
    
    greeting() # use the default if no parameter is given
    greeting("TestName")
    
    

    # ========================================================================
    # Booleans and Conditionals
    # ========================================================================
    print("\nBooleans and Conditionals ===============================")
    
    have_umbrella = True
    rain_level = 6
    have_hood = False
    is_workday = True
    # can split a conditional statement over multiple lines
    prepared_for_weather = (
        have_umbrella
        or ((rain_level < 5) and have_hood)
        or (not (rain_level > 0 and is_workday))
    )
    print("Are you prepared for the weather?",prepared_for_weather)
    
    # single line conditional statements (equivalent to ternary operator
    # in other languages)
    def quiz_message(grade):
        outcome = "failed" if grade < 50 else "passed"
        print("You", outcome, "with grade", grade)
    quiz_message(51)
    print("\n")
    
    # boolean conversion
    print("1987 =", bool(1987)) # all numbers are treated as True except 0
    print("0 =", bool(0))
    print("'asdfg' =", bool("asdfg")) # all strings are treated as True except ""
    print("'' =", bool(""))
    
    # since 1 = True and 0 = False, can make a logical expression work like
    # a math problem
    # e.g. if only one of the input parameters can be true:
    def exactly_one(ketchup, mustard, relish):
        return (int(ketchup) + int(mustard) + int(relish)) == 1
    

    # ========================================================================
    # Lists
    # ========================================================================
    print("\nLists ===============================")
    
    # a list can contain a mix of types of variables
    my_favs = [32, "this string", 'c', 3.14]
    print("My faves:", my_favs)
    
    # elements at the end of the list can be accessed with negatives startings with -1
    nums = [1, 2, 3, 4, 5, 6]
    print("Original nums list:", nums)
    last_el = nums[-1] # is value 6
    second_to_last = nums[-2] # is value 5
    print("Last element in the list:", last_el)
    
    # can slice a list (not inclusive of the end index)
    nums_slice = nums[0:3] # is values for indices 0, 1, 2, but NOT 3
    print("Slice of nums[0:3]: ", nums_slice)
    # if either the beginning index or ending index is omitted, then python assumes it
    first_half = nums[:3]
    last_half = nums[3:]
    print("First half of nums[:3]:", first_half)
    print("Second half of nums[3:]:", last_half)
    
    # can do value reassignment using slices as well
    nums[0:3] = [10, 9, 8]
    print("Value reassignment on nums:", nums)
    
    # some functions
    nums_length = len(nums)
    sorted_nums = sorted(nums) # sorts the list (default in alphabetical or numerical order)
    sum_nums = sum(nums)
    print("Length of nums list:", nums_length)
    print("Sorted nums list:", sorted_nums)
    print("Sum of nums list:", sum_nums)
    sorted_nums.append(11)
    print("Nums after appending 11:", sorted_nums)
    last_el = sorted_nums.pop()
    print("Last element from nums:", last_el)
    
    # can ask whether an element is in a list
    print("Is 790 in nums?:", 790 in sorted_nums)
    
    # a tuple is like a list except not mutable. It must be complete 
    # when first declared/assigned. They are commonly used for functions
    # that have multiple return values
    atuple = (1, 2, 3, 4)
    
    # a swap in python is easier than in other languages. No temp variable 
    # is needed!
    a = 1
    b = 99
    a, b = b, a  # do the swap
    print("a:", a)
    print("b:", b)
    
    
    # ========================================================================
    # Loops and List Comprehensions
    # ========================================================================
    print("\nLoops and List Comprehensions ===============================")
    
    # use of "in" for iteration over any collection of things
    nums_list = [1, 2, 3, 4, 5, 6]
    nums_tuple = (1, 2, 3, 4, 5, 6)
    nums_str = "123456"
    for num in nums_list:
        print(num, end=' ')
    print("\n")
    for num in nums_tuple:
        print(num, end=' ')
    print("\n")
    for num in nums_str:
        print(num, end=' ')
    print("\n")
    
    # also have the range function for iterating over numbers
    for i in range(6):
        print(i, end=' ')
    print("\n")
    
    for i in range(1,6): # range can have a start and stop parameter
        print(i, end=' ')
    print("\n")
    
    # list comprehensions are a one-line method for creating lists
    squares = [n**2 for n in range(10)]
    print(squares)
    
    # can also apply a transformation in a list comprehension
    planets = ["Mercury", "Venus", "Earth"]
    cap_planets = [planet.upper() + "!" for planet in planets]
    print(cap_planets)
    
    # append two or more lists using the plus operator
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    print("Consolidated list:", list1 + list2)
    
    
    # ========================================================================
    # Strings and Dictionaries
    # ========================================================================
    print("\nStrings and Dictionaries ===============================")
    
    # can split a string into a list using .split()
    claim = "Pluto is a planet"
    words = claim.split() # by default, splits on whitespace
    print(words)
    adate = "2020-03-26"
    numbers = adate.split('-') # canalso split on a specific character
    print(numbers)
    
    # can lower case or upper case a string
    claim_lower = claim.lower()
    print(claim_lower)
    claim_upper = claim.upper()
    print(claim_upper)
    
    # can strip out punctuation using .strip(), or replace it using .replace()
    mystring = "This is a typical sentence, with some punctiation."
    newstring = mystring.strip(".") # only removes things at begining or end of the string
    newstring = newstring.replace(",", "")
    print(newstring)
    
    # can go from list to string using .join()
    str_list = ["Pluto", "is", "a", "planet"]
    new_str = ' '.join(str_list)
    print(new_str)
    
    # can index into a string, but cannot change the value (strings are immutable)
    print(claim[0])
    # claim[0] = "B" # this would cause an error

    # can concatenate a string using .format and {} as a placeholder
    planet = "Pluto"
    position = 9
    claim2 = "{}, you'll always be the {}th planet to me.".format(planet, position)    
    print(claim2)
    
    
    # Python has dictionary comprehensions that work similarly to list compr
    planet_to_initial = {planet: planet[0] for planet in planets}
    print(planet_to_initial)
    
    # can check wether a certain key exists in the dictionary
    if "Earth" in planet_to_initial:
        print(planet_to_initial["Earth"])
    
    # can access all of the keys using .keys() and all the values using .values()
    print(planet_to_initial.keys())
    print(planet_to_initial.values())
    
    # can iterate over key, value pairs using .items()
    for planet, initial in planet_to_initial.items():
        print("{} begins with {}".format(planet, initial))
    
    
    
    # ========================================================================
    # Working with External Libraries
    # ========================================================================
    print("\nWorking with External Libraries ===============================")
    
    """
    import math
    
    # can see all of the functions and values in a particular module using dir()
    print(dir(math))

    # help also works for imported modules and their functions
    help(math)
    help(math.log)
    
    # can import a module using an alias name
    import math as mt
    mt.log(32,2)
    
    # or can import the entire contents of a module with * if don't want to 
    # use dot notation (but this is bad practice as conflicts with other 
    # modules can occur)
    from math import *
    log(32, 2)
    
    # some modules have submodules in them. To access them, you have to use
    # dot notation twice
    rolls = np.random.randint(low=1, high=6, size=10)
    
    # Important functions for when using a new module
    type() # what is this thing?
    dir() # what functions and values are associated with it?
    help() # what is the documentation on this thing?
    
    """
    
    
    