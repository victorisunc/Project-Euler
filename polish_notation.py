#!/usr/bin/python

def polish(argv):
    import operator
    symbols = argv.split(' ')
    stack = []
    def get_operator(op):
        return {
          '*': operator.mul,
          '/': operator.div,
          '+': operator.add,
          '-': operator.sub,
          '%': operator.mod
        }[op]
    for symbol in reversed(symbols):
        if symbol.isdigit():
            stack.append(symbol)
        else:
            operand1 = float(stack.pop())
            operand2 = float(stack.pop())
            calc_result = get_operator(symbol)(operand1, operand2)
            stack.append(calc_result)
    return stack.pop()

if __name__ == '__main__':
    import sys
    print polish(sys.argv[1])
    # print polish(['*', '5', '*', '2', '2']) == 20.0
    # print polish('- * / 15 - 7 + 1 1 3 + 2 + 1 1'.split()) == 5
