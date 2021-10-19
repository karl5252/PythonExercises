"""
Classic FizzBuzz exercise.
For range from 1 to 100
if number is divisible by 3 print "fizz", if divisible by 5 print "buzz"
and if divisible by both 3 and 5 print "FizzBuzz"
"""

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

