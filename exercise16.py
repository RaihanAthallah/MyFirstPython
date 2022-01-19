# Consecutive zeros

# The goal of this challenge is to analyze
# a binary string consisting of only zeros 
# and ones. Your code should find the biggest 
# number of consecutive zeros in the string. 
# For example, given the string:

# "1001101000110"
# The biggest number of consecutive zeros is 3.

# Define a function named consecutive_zeros
# that takes a single parameter, which is the 
# string of zeros and ones. Your function should 
# return the number described above.



#  EXERCISE 16 CONSECUTIVE ZERO 
def consecutive_zeros(word):
    count = 0
    biggest = 0
    for i in word:
        if i == '0':
            count += 1
            biggest = max(biggest, count)
            
        else:
            count = 0
    return biggest

        
print(consecutive_zeros('100110100011000010000111'))