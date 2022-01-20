
#UNIFINISHED


def validate(code):
    check = 7
    spaces =0
    for i in code:
        if i == ' ':
            spaces += 1
    if 'def' not in code:
        check -= 1
        return 'missing def'
    elif ':' not in code:
        check -= 1
        return 'missing :'
    elif '(' and ')' not in code:
        check -= 1
        return 'missing paren'
    elif '()' in code:
        check -= 1
        return 'missing param'
    elif 'validate'not in code:
        check -= 1
        return 'wrong name'
    elif 'return' not in code:
        check -= 1
        return 'missing return'
    elif spaces != 4:
        check -= 1
        return 'missing indent'
    
    if check == 7:
        return True
    else:
        print(check)
        return False
    
    
print(validate("validate('def foo(x):\nprint(123)')"))
     
    