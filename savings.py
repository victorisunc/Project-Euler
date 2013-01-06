#!/usr/bin/env python

import timeit

# CALCULATE SAVINGS

def savings(initial, period, salary, salary_rate_increase, exchange, monthly_rate):
    """
    This function takes an initial amount, period which the total amount will
    be kept accumulating, and a fixed salary which will be deposited into
    the savings account monthly. The monthly salary increases by a set percentage.
    """
    salary = int(salary)
    salary_rate_increase = float(salary_rate_increase)
    monthly_rate = float(monthly_rate)
    initial = int(initial)
    result = initial
    exchange = float(exchange)
    interest = 0
    print "\nInitial: {:,.2f} - Period in Months: {!s} - Salary: {:,.2f} - Yearly Salary Increase: {:.2%} - Dollar-Real Exchange: {!s} - Monthly Rate: {:.2%}\n".\
    format(initial, period, salary, salary_rate_increase, exchange, monthly_rate)
    for i in range(1, int(period)+1):

        # increase salary every year by a percentage set in input parameter
        if (i > 1 and (i % 12) == 1):
            salary = salary * (1 + salary_rate_increase)

        print "{:,.2f} \t- next interest: {:,.2f} \t- amount added: {:,.2f} \t- month: {!s} \t- year: {!s}".format(result, (monthly_rate*result), salary, i, ((i-1)/12)+1)
        result += salary + ((monthly_rate) * result)
        interest += monthly_rate*result
    print "\nFinal Total: {:,.2f}".format(result)
    print "Interest Only: {:,.2f}".format(interest)
    print "USD: {:,.2f}".format(result/exchange)
    return
if (__name__ == "__main__"):
    """
    Main
    """
    try:
        t = timeit.Timer(setup='from __main__ import savings', stmt='savings(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])')
        print "\n" + str(t.timeit(1)) + " seconds"
    except:
        print """
            Usage: python file_name.py
            <initial amount>
            <period in months>
            <monthly amount added>
            <percent increase of monthly amount added every year>
            <dollar-real exchange rate>
            <savings monthly-rate>
            """
