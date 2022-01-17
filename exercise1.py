 # Capital indexes
 
    # Write a function named capital_indexes. 
    # The function takes a single parameter, 
    # which is a string. Your function should 
    # return a list of all the indexes in the 
    # string that have capital letters.

    # For example, calling 
    # capital_indexes("HeLlO") should return the list [0, 2, 4].


# EXERCISE 1 INDEX OF CAPITAL LETTER
def capital_index(word):
    list = []
    index = 0
    for i in word:
        if i.isupper():
            list.append(index)
        index += 1
    print(list)
            
words = input('>')
capital_index(words)