
def answer(str):
    result = []
    operators_stack = []
    operators = {'+':1, '*':2}
    for c in str:
        # number
        if c.isdigit():
            result.append(c)
            print "result: " + ''.join(result)
        # operator
        else:
            print ''.join(operators_stack)
            # first operator
            if not operators_stack:
               operators_stack.append(c)
            else:
               # push to result when lower operators comes
                while (operators_stack and (operators[c] < operators[operators_stack[-1]])):
                    result.append(operators_stack.pop())
                operators_stack.append(c)
    # left operators append
    while operators_stack:
        result.append(operators_stack.pop())
    return ''.join(result)

if __name__ == "__main__":
    my_ans = answer("2+3*2")
    # my_ans = answer("2*4*3+9*3+5")
    print my_ans




