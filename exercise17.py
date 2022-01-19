# All equal

# Define a function named all_equal that 
# takes a list and checks whether all elements
# in the list are the same.

# For example
# calling all_equal([1, 1, 1]) should return True.

#  EXERCISE 17 ALL EQUAL
def all_equal(list):
    if len(set(list)) == 1 or len(list) == 0:
        return  True
    else: return False
        
    
print(all_equal([1, 1, 1]))
    