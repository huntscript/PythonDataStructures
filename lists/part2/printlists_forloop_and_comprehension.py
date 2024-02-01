'''
Ways to print lists in python part 2
using for loop
using list comprehension
use case: print each element of the list individually
'''

# Create lists 'days' and 'numbers'
days = ['monday', 'tuesday', 'wednesday', 'thursday']
numbers = [1, 2, 3, 4, 5]

# using for loop
# for day in days:
#     print(day)

# print()

# for number in numbers:
#     print(number)

# using list comprehension
[print(day) for day in days]
print()
[print(number) for number in numbers]
