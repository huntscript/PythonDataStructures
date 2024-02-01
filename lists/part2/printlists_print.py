'''
Ways to print lists in python part 1
using print() function
use case: print the entire list
'''
# You can print lists by passing them directly into  the print
# function. But it is better to store them into variables.
# print(['monday', 'tuesday', 'wednesday', 'thursday'])
# print([1, 2, 3, 4, 5])

# Create lists 'days' and 'numbers'
# store the lists into variables
days = ['monday', 'tuesday', 'wednesday', 'thursday']
numbers = [1, 2, 3, 4, 5]

# using print() function
print(days)
print(numbers)

# print the lists on same line 
# add a comma to separate them by a space automatically
print(days, numbers)
# print the lists on same line, separate them by a comma
print(days, ', ', numbers)
# print the lists on same line, separate them by an hyphen
print(days, '-', numbers)
