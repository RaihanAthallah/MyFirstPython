# Boolean and

# Define a function named triple_and that
# takes three parameters and returns True 
# only if they are all True and False otherwise.

#EXERCISE 18 BOOLEAN AND

def triple_and(bool1,bool2,bool3):
    if bool1 and bool2 and bool3:
        return True
    else: return False
    
print(triple_and(True,False,True))
    