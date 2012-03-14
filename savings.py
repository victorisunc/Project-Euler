#!/usr/bin/env python

import timeit

# CALCULATE SAVINGS

def savings(initial, period, salary, exchange, monthly_rate):
    """
    This function takes an initial amount, period which the total amount will
    be kept accumulating, and a fixed salary which will be deposited into
    the savings account monthly.
    """
    salary = int(salary)
    monthly_rate = float(monthly_rate)
    initial = int(initial)
    result = initial
    exchange = float(exchange)
    print "\nInitial: R$%.2f - Period in Months: %s - Salary: R$%.2f - Dollar-Real Exchange: %s - Monthly Rate: %s percent\n"\
 % (initial, period, salary, exchange,(monthly_rate*100))
    for i in range(1, int(period)+1):
        print "R$%.2f \t- next interest: R$%.2f" % (result,(monthly_rate*result))
        result += salary + ((monthly_rate) * result)
    print "\nFinal Total: R$%.2f" % result
    print "Interest Only: R$%.2f" % (result - (initial + salary * int(period)))
    print "In Dollar: $%.2f" % (result/exchange)
    return
if (__name__ == "__main__"):
    """
    Main
    """
    try:
        t = timeit.Timer(setup='from __main__ import savings', stmt='savings(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])')
        print "\n" + str(t.timeit(1)) + " seconds"
    except:
        print """
            Usage: python file_name.py
            <initial amount>
            <period in months>
            <monthly amount added>
            <dollar-real exchange rate>
            <savings monthly-rate>
            """
