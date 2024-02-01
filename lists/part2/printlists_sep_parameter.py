''' 
Ways to print lists in python part 3
using sep parameter
use case: print each element of the list individually
          add separator between the elements of the list
'''
# Create lists 'days' and 'numbers'
days = ['monday', 'tuesday', 'wednesday', 'thursday']
numbers = [1, 2, 3, 4, 5]

# using sep parameter

# add empty string
print("add empty string")
print(*days, sep= '')
print(*numbers, sep= '')

# add space
print("add space")
print(*days, sep= ' ')
print(*numbers, sep= ' ')

# add hyphen
print("add hyphen")
print(*days, sep= '-')
print(*numbers, sep= '-')

# add space + hyphen + space
print("add space + hyphen + space")
print(*days, sep= ' - ')
print(*numbers, sep= ' - ')

# add new line character
print("add new line character")
print(*days, sep= '\n')
print(*numbers, sep= '\n')
