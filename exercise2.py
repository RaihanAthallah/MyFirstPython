# Middle letter

    # Write a function named mid that 
    # takes a string as its parameter. 
    # Your function should extract and 
    # return the middle letter. If there 
    # is no middle letter, your function 
    # should return the empty string.

    # For example, 
    # mid("abc") should return "b" and mid("aaaa") should return "".
    

# EXERCISE 2 MIDDLE LETTER
def mid(words):
    length = len(words)
    if length%2 == 1:
        return words[int(length/2)]
    else:
        return ''

print(mid('aaaa'))