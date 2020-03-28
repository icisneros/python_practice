# FizzBuzz program

# fizzes = 0
# buzzes = 0
# fizzbuzzes = 0
# neither = 0

# for i in range(1,101):
#     s = str(i)
#     if i % 3 == 0 or i % 5 == 0:
#         s = ''
#         if i % 3 == 0:
#             s = 'Fizz'
#             fizzes = fizzes + 1
#         elif i % 5 == 0:
#             s = 'Buzz'
#             buzzes = buzzes + 1
#         if i % 3 == 0 and i % 5 == 0:
#             s = 'FizzBuzz'
#             fizzbuzzes = fizzbuzzes + 1
#         else:
#             neither = neither + 1
#     print s

# print 'The final count:'
# print 'There were ' + str(fizzes) + ' Fizzes'
# print 'There were ' + str(buzzes) + ' Buzzes'
# print 'There were ' + str(fizzbuzzes) + ' FizzBuzzes'
# print 'And there were ' + str(neither) + ' regular numbers'
# print 'There were ' + str(fizzes+buzzes+fizzbuzzes+neither) + ' total numbers'

fizzes = 0
buzzes = 0
both = 0
other = 0

for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        s = 'Fizz'
        fizzes = fizzes + 1
    elif i % 3 != 0 and i % 5 == 0:
        s = 'Buzz'
        buzzes = buzzes + 1
    elif i % 3 == 0 and i % 5 == 0:
        s = 'FizzBuzz'
        both = both + 1
    else:
        s = str(i)
        other = other + 1

    print s

print '\nThe final count:\n'
print 'Total Fizzes: ' + str(fizzes) + '\n'
print 'Total Buzzes: ' + str(buzzes) + '\n'
print 'Total FizzBuzzes: ' + str(both) + '\n'
print 'Total regular numbers: ' + str(other) + '\n'
print 'Total numbers: ' + str(fizzes + buzzes + both + other) + '\n'

