# Counting syllables

# Define a function named count that 
# takes a single parameter. The parameter is a string.
# The string will contain a single word divided into 
# syllables by hyphens, such as these:

# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"

# Your function should count the number of syllables and return it.

# For example, the call count("ho-tel") should return 2.

#  EXERCISE 8 COUNTING SYLLABLES
def count(word):
    count = 1
    for i in word:
        if i == '-':
            count += 1
    return count
    
print(count('ho-tel'))
print(count('cat'))
print(count('met-a-phor'))
print(count('ter-min-a-tor'))