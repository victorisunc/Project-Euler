#!/usr/bin/env python

import timeit

# CALCULATE SAVINGS 

def savings(initial, period, salary):
    """
This function takes an initial amount, period which the total amount will
be kept accumulating, and a fixed salary which will be deposited into
the savings account monthly.
    """
    salary = int(salary)
    monthly_rate = 0.005
    initial = int(initial)
    result = initial 
    print "Initial: R$%.2f - Period in Months: %s - Salary: R$%.2f - Monthly Rate: %s percent"\
 % (initial, period, salary, (monthly_rate*100))
    for i in range(1, int(period)+1):
        print "R$%.2f - next interest: R$%.2f" % (result,(monthly_rate*result))
        result += salary + ((monthly_rate) * result)
    print "\nFinal Total: R$%.2f" % result
    print "Interest Only: R$%.2f" % (result - (initial + salary * int(period)))
    print "In Dolar: $%.2f" % (result/1.7)
    return
if (__name__ == "__main__"):
    """
    Main
    """
    try: 
        t = timeit.Timer(setup='from __main__ import savings', stmt='savings(sys.argv[1], sys.argv[2], sys.argv[3])') 
        print "\n" + str(t.timeit(1)) + " seconds"
    except:
        print 'Usage: python file_name.py <n>'
