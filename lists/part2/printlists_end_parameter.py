''' 
Ways to print lists in python part 4
using end parameter
use case: print each element of the list individually
          add separator between the elements of the list
'''

# Create a list of integers
integers = [1, 2, 3, 4]

# add empty string 
print("add empty string")
for integer in integers:
    print(integer, end= '')

print() # new line    

# add space 
print("add space")
for integer in integers:
    print(integer, end= ' ')

print() # new line  

# add hyphen 
print("add hyphen")
for integer in integers:
    print(integer, end= '-')

print() # new line  

# add space + hyphen + space
print("add space + hyphen + space")
for integer in integers:
    print(integer, end= ' - ')

print() # new line     

# add new line character
print("add new line character")
for integer in integers:
    print(integer, end= '\n')
