# Flatten a list

# Write a function that takes a list of lists
# and flattens it into a one-dimensional list.

# Name your function flatten. It should take 
# a single parameter and return a list.

# For example, calling:

# flatten([[1, 2], [3, 4]])
# Should return the list: [1, 2, 3, 4]


#  EXERCISE 10 FLATTEN A LIST
def flatten(list):
    flatten_list = []
    for i in list:
        flatten_list += i
    return flatten_list
        
        
print(flatten([[1, 2], [3, 4]]))