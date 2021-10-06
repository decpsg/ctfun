'''
Write a program which will generate a list of numbers from 1 to n inclusive. 
When the number is a multiple of 3 or contains 3, show the symbol '@', else show the actual number. 
For example, when n = 20, numbers = [1, 2, '@', 4, 5, '@', 7, 8, '@', 10, 11, '@', '@', 14, '@', 16, 17, '@', 19, 20]
Show using comments, where computational thinking ideas (abstraction, decomposition, pattern recognition, algorithm design)
can be applied.
'''

# input/initialisation - initialise variable(s) and data structure(s)
numbers = []
n = 100
# process - loop from 1 to n inclusive
for i in range(1, n+1):
  # if multiple of 3 and contains 3 (pattern recognition)
  if i % 3 == 0 or '3' in str(i):
    # add symbol
    numbers.append('@')
  else:
    # add number
    numbers.append(i)
# output - display results    
print(numbers)

# comments show decomposition (input/initialisation, process, output) and algorithm design
# no abstraction in this context as there is no noise in the task specification
