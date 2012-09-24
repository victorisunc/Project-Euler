#SICP Chapter #02 Examples in Python
import math

# Functions defined in previous chapters
def gcd(a, b):
   if (b == 0):
      return a
   else:
      return gcd(b, a % b)

def fib(n):
   if (n == 0):
      return 0
   elif (n == 1):
      return 1
   else:
      return fib(n - 1) + fib(n - 2)

def identity(x): return x

# 2 Building Abstractions with Data
def linear_combination(a, b, x, y):
   return a*x + b*y

def mul(a, b): return a * b
def linear_combination(a, b, x, y):
   return mul(a, x) + mul(b, y)

# 2.1.1 Introduction to Data Abstraction - Example: Arithmetic Operations for Rational Numbers

# Literal Translation #
def make_rat(n, d): return (n, d)
def numer(x): return x[0]
def denom(x): return x[1]

def add_rat(x, y):
   return make_rat(numer(x)*denom(y) + numer(y)*denom(x), denom(x)*denom(y))

def sub_rat(x, y):
   return make_rat(numer(x)*denom(y) - numer(y)*denom(x), denom(x)*denom(y))

def mul_rat(x, y):
   return make_rat(numer(x)*numer(y), denom(x)*denom(y))

def div_rat(x, y):
   return make_rat(numer(x)*denom(y), denom(x)*numer(y))

def equal_rat(x, y):
   return (numer(x)*denom(y) == numer(y)*denom(x))

def cons(x, y): return (x, y)
def car(xs): return xs[0]
def cdr(xs): return xs[1]

x = cons(1, 2)
print (car(x))
print (cdr(x))

x = cons(1, 2)
y = cons(3, 4)
z = cons(x, y)
print (car(car(z)))
print (car(cdr(z)))
print (z)

# footnote -- alternative definitions
make_rat = cons
numer = car
denom = cdr

x = (1, 2)
y = (3, 4)
print (numer(x))
print (denom(x))

def compose(f, g): return lambda x: f(g(x))

def print_rat(x):
   print (str(numer(x)) + "/" + str(denom(x)))

one_half = make_rat(1, 2)
print_rat(one_half)

one_third = make_rat(1, 3)
print_rat(add_rat(one_half, one_third))
print_rat(mul_rat(one_half, one_third))
print_rat(add_rat(one_third, one_third))

# reducing to lowest terms in constructor
def make_rat(n, d):
   g = gcd(n, d)
   return (n / g, d / g)

def add_rat(x, y):
   return make_rat(numer(x)*denom(y) + numer(y)*denom(x), denom(x)*denom(y))

print_rat(add_rat(one_third, one_third))
# end Literal Translation #

# Object Translation #
class Rational:
   def __init__(self, n, d):
      self.numer = n
      self.denom = d
   def add_rat(self, y):
      return Rational(self.numer*y.denom + y.numer*self.denom, self.denom*y.denom)
   def sub_rat(self, y):
      return Rational(self.numer*y.denom - y.numer*self.denom, self.denom*y.denom)
   def mul_rat(self, y):
      return Rational(self.numer*y.numer, self.denom*y.denom)
   def div_rat(self, y):
      return Rational(self.numer*y.denom, self.denom*y.numer)
   def equal_rat(self, y):
      return self.numer*y.denom == y.numer * self.denom
   def print_rat(self):
      print (str(self.numer) + "/" + str(self.denom))

one_half = Rational(1, 2)
one_half.print_rat()

one_third = Rational(1, 3)
one_half.add_rat(one_third).print_rat()
one_half.mul_rat(one_third).print_rat()
one_third.add_rat(one_third).print_rat()

class Rational:
   def __init__(self, n, d):
      g = gcd(n, d)
      self.numer = n / g
      self.denom = d / g
   def add_rat(self, y):
      return Rational(self.numer*y.denom + y.numer*self.denom, self.denom*y.denom)
   def sub_rat(self, y):
      return Rational(self.numer*y.denom - y.numer*self.denom, self.denom*y.denom)
   def mul_rat(self, y):
      return Rational(self.numer*y.numer, self.denom*y.denom)
   def div_rat(self, y):
      return Rational(self.numer*y.denom, self.denom*y.numer)
   def equal_rat(self, y):
      return self.numer*y.denom == y.numer * self.denom
   def print_rat(self):
      print (str(self.numer) + "/" + str(self.denom))

one_third = Rational(1, 3)
one_third.print_rat()
one_third.add_rat(one_third).print_rat()
# end Object Translation #

# Exercise 2.1
def make_rat(n, d):
   if (d < 0 and n < 0) or n < 0:
      return (d * -1, n * -1)
   else:
      return (d, n)

# 2.1.2 Introduction to Data Abstraction - Abstraction barriers

# Literal Translation #
# reducing to lowest terms in selectors
def make_rat(n, d): return (n, d)

def numer(x):
   g = gcd(x[0], x[1])
   return x[0] / g

def denom(x):
   g = gcd(x[0], x[1])
   return x[1] / g
# end Literal Translation #

# Object Translation #
class Rational:
   def __init__(self, n, d):
      self.n = n
      self.d = d
   def numer(self):
      g = gcd(self.n, self.d)
      return self.n / g
   def denom(self):
      g = gcd(self.n, self.d)
      return self.d / g
   def add_rat(self, y):
      return Rational(self.numer()*y.denom() + y.numer()*self.denom(), self.denom()*y.denom())
   def sub_rat(self, y):
      return Rational(self.numer()*y.denom() - y.numer()*self.denom(), self.denom()*y.denom())
   def mul_rat(self, y):
      return Rational(self.numer()*y.numer(), self.denom()*y.denom())
   def div_rat(self, y):
      return Rational(self.numer()*y.denom(), self.denom()*y.numer())
   def equal_rat(self, y):
      return self.numer()*y.denom() == y.numer() * self.denom()
   def print_rat(self):
      print (str(self.numer()) + "/" + str(self.denom()))
# end Object Translation #

# Exercise 2.2
def make_point(x, y): return (x, y)
def x_point(point): return point[0]
def y_point(point): return point[1]
def make_segment(start_segment, end_segment):
   return (start_segment, end_segment)
def start_segment(segment): return segment[0]
def end_segment(segment): return segment[1]
def midpoint_segment(segment):
   s = start_segment(segment)
   e = end_segment(segment)
   return make_point((x_point(s) + x_point(e)) / 2, (y_point(s) + y_point(e)) / 2)
def print_point(p):
   print ("(" + str(x_point(p)) + "," + str(y_point(p)) + ")")

# Exercise 2.3
def square(x): return x * x
def length_segment(segment):
   s = start_segment(segment)
   e = end_segment(segment)
   return math.sqrt(square(x_point(e) - x_point(s)) + square(y_point(e) - y_point(s)))

# Constructors create type tagged using tuple
def make_rectangle_axy(anchor, xlen, ylen):
   return ("axy", anchor, xlen, ylen)
def make_rectangle_seg(start_segment, end_segment):
   return ("seg", start_segment, end_segment)

# 'length_rectangle' and 'width_rectangle' act as an abstraction barrier for higher-level
# procedures because 'rectangle' implementation details are buried here, and should the
# implementation change, only these procedures will need to be altered to support the change
def length_rectangle(rect):
   if rect[0] == "axy":
      return 0                                     # Compute length ...
   elif rect[0] == "seg":
      return 0                                     # Compute length ...

def width_rectangle(rect):
   # As per 'length_rectangle' except that rectangle width is returned ...
   return 0

# High-level procedures are quarantined from representation / implementation details
def area_rectangle(rect):
   return length_rectangle(rect) * width_rectangle(rect)
def perimeter_rectangle(rect):
   return length_rectangle(rect) * 2 + width_rectangle(rect) * 2

# 2.1.3 Introduction to Data Abstraction - What is meant by data?
def cons(x, y):
   def dispatch(m):
      if (m == 0):
         return x
      elif (m == 1):
         return y
      else:
         raise Exception("Argument not 0 or 1 -- CONS " + str(m))
   return dispatch

def car(z): return z(0)
def cdr(z): return z(1)

# Exercise 2.4
def cons(x, y):
   return (lambda m: m(x, y))
def car(z):
   return z(lambda p, q: p)
def cdr(z):
   return z(lambda p, q: q)

# Exercise 2.5
def cons(x, y):
   return 2 ^ (x * (3 ^ y))
def car(z):
   if z % 2 == 0:
      return car((z / 2) + 1)
   else:
      return 0
def cdr(z):
   if z % 3 == 0:
      return cdr((z / 3) + 1)
   else:
      return 0

# Exercise 2.6
zero = lambda f: lambda x: x
def add1(n): return lambda f: lambda x: (f((n(f))(x)))

# 2.1.4 Introduction to Data Abstraction - Extended Exercise: Interval Arithmetic

# Literal Translation #
def make_interval(a, b): return (a, b)

def lower_bound(p): return p[0]
def upper_bound(p): return p[1]

def add_interval(x, y):
   return make_interval(lower_bound(x) + lower_bound(y), upper_bound(x) + upper_bound(y))

def mul_interval(x, y):
   p1 = lower_bound(x) * lower_bound(y)
   p2 = lower_bound(x) * upper_bound(y)
   p3 = upper_bound(x) * lower_bound(y)
   p4 = upper_bound(x) * upper_bound(y)
   return make_interval(
      min(min(p1, p2), min(p3, p4)),
      max(max(p1, p2), max(p3, p4)))

def div_interval(x, y):
   z = make_interval(1.0 / upper_bound(y), 1.0 / lower_bound(y))
   return mul_interval(x, z)

def make_center_width(c, w):
   return make_interval(c-w, c+w)

def center(i):
   return (lower_bound(i) + upper_bound(i)) / 2.0

def width(i):
   return (upper_bound(i) - lower_bound(i)) / 2.0

# parallel resistors
def par1(r1, r2):
   return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
   one = make_interval(1.0, 1.0)
   return div_interval(one,
            add_interval(div_interval(one, r1),
                         div_interval(one, r2)))
# end Literal Translation #

# Object Translation #
class Interval:
   def __init__(self, a, b):
      self.upper_bound = a
      self.lower_bound = b
   def add_interval(self, y):
      return Interval(self.lower_bound + y.lower_bound, self.upper_bound + y.upper_bound)
   def mul_interval(self, y):
      p1 = self.lower_bound * y.lower_bound
      p2 = self.lower_bound * y.upper_bound
      p3 = self.upper_bound * y.lower_bound
      p4 = self.upper_bound * y.upper_bound
      return Interval(
         math.min(math.min(p1, p2), math.min(p3, p4)),
         math.max(math.max(p1, p2), math.max(p3, p4)))
   def div_interval(self, y):
      z = Interval(1 / y.upper_bound, 1 / y.lower_bound)
      return self.mul_interval(x, z)
   def make_center_width(self, c, w):
      return Interval(c-w, c+w)
   def center(self):
      return (self.lower_bound + self.upper_bound) / 2
   def width(self):
      return (self.upper_bound - self.lower_bound) / 2

interval = Interval(10, 20)

# parallel resistors
def par1(r1, r2):
   return r1.mul_interval(r2).div_interval(r1.add_interval(r2))

def par2(r1, r2):
   one = Interval(1, 1)
   return one.div_interval(one.div_interval(r1).add_interval(one.div_interval(r2)))
# end Object Translation #

# Exercise 2.8
def sub_interval(x, y):
   return make_interval(lower_bound(x) - lower_bound(y), upper_bound(x) - upper_bound(y))

# Exercise 2.9
i = make_interval(5, 10)
j = make_interval(15, 25)

# width of the sum (or difference) of two intervals *is* a function only of the widths of
# the intervals being added (or subtracted)
print (width(add_interval(i, j)), width(i) + width(j))
print (width(sub_interval(i, j)), width(i) + width(j))

# width of the product (or quotient) of two intervals *is not* a function only of the widths
# of the intervals being multiplied (or divided)
print (width(mul_interval(i, j)), width(i) + width(j))
print (width(div_interval(i, j)), width(i) + width(j))

# Exercise 2.10
def is_zero_interval(i):
   return lower_bound(i) == 0 or upper_bound(i) == 0
def div_interval_zero_check(x, y):
   if is_zero_interval(y):
      raise exception("Zero interval divisor")
   else:
      return div_interval(x, y)

# Exercise 2.12
def make_center_percent(c, p):
   return make_center_width(c, p * c / 100)
def percent(i):
   return width(i) / center(i) * 100

# 2.2.1 Hierarchical Data and the Closure Property - Representing Sequences
one_through_four = [1, 2, 3, 4]

print (one_through_four)
print (one_through_four[0])
print (one_through_four[1:])
print (one_through_four[1])
one_through_four.insert(0, 10)      # note: Python insert modifies state
print (one_through_four)

def list_ref(items, n):
   return items[n]

squares = [1, 4, 9, 16, 25]
print (list_ref(squares, 3))

def length(items):
   return len(items)

odds = [1, 3, 5, 7]
print (len(odds))

def append(xs, ys):
   rt = xs[0:]
   for i in ys:
      rt.append(i)
   return rt

print (append(squares, odds))
print (append(odds, squares))

# Mapping over lists
def scale_list(factor, items):
   rt = []
   for val in items:
      rt.append(val * factor)
   return rt

print (scale_list(10, [1, 2, 3, 4, 5]))

# uncurried version of map
def map(proc, items):
   rt = []
   for val in items:
      rt.append(proc(val))
   return rt
print (map(abs, [-10, 2.5, -11.6, 17]))
print (map(lambda x: x * x, [1, 2, 3, 4]))

def scale_list(factor, items):
   return map(lambda x: x * factor, items)

# curried version map
def map(proc):
   def map_lambda(items):
      rt = []
      for val in items:
         rt.append(proc(val))
      return rt
   return map_lambda
print (map (abs) ([-10, 2.5, -11.6, 17]))
print (map (lambda x: x * x) ([1, 2, 3, 4]))

def scale_list(factor, items):
   return map (lambda x: x * factor) (items)

# Exercise 2.17
def last_pair(items):
   return items[-1:]
print (last_pair([23, 72, 149, 34]))

# Exercise 2.18
def reverse(items):
   rt = []
   for val in items:
      rt.insert(0, val)
   return rt
print (reverse([1, 4, 9, 16, 25]))

# Exercise 2.19
def no_more(coin_values):
   return len(coin_values) == 0
def except_first_denomination(coin_values):
   return coin_values[1:]
def first_denomination(coin_values):
   return coin_values[0]
def cc(amount, coin_values):
   if amount == 0:
      return 1
   elif amount < 0 or no_more(coin_values):
      return 0
   else:
      return (cc(amount, except_first_denomination(coin_values)) +
              cc(amount - first_denomination(coin_values), coin_values))
us_coins = [50, 25, 10, 5, 1]
uk_coins = [100, 50, 20, 10, 5, 2, 1, 0.5]
print (cc(100, us_coins))
# works but takes a long time based on inefficiency above (tail[1:])
# print (cc(100, uk_coins))

# Exercise 2.20
def filter(predicate, items):
   rt = []
   for value in items:
      if predicate(value):
         rt.append(value)
   return rt
def is_odd(n): return n % 2 == 1
def is_even(n): return not(is_odd(n))
def same_parity(items):
   head = items[0]
   tail = items[1:]
   predicate = is_odd if is_odd(head) else is_even
   return filter(predicate, tail)
print (same_parity([1, 2, 3, 4, 5, 6, 7]))
print (same_parity([2, 3, 4, 5, 6, 7]))

# Exercise 2.21
def square_list(items):
   rt = []
   for value in items:
      rt.append(value * value)
   return rt
print (square_list([1, 2, 3, 4]))
def square_list(items):
   return map (lambda x: x * x) (items)
print (square_list([1, 2, 3, 4]))

# Exercise 2.23
def for_each(f, items):
   for value in items:
      f(value)

# 2.2.2 Hierarchical Data and the Closure Property - Hierarchical Structures
def count_leaves(items):
   n = 0
   for value in items:
      if isinstance(value, list):
         n = n + count_leaves(value)
      else:
         n = n + 1
   return n

x = [[1, 2], [3, 4]]
print (len(x))
print (count_leaves(x))

print ([x, x])
print (len([x, x]))
print (count_leaves([x, x]))

# Mapping over trees
def scale_tree(factor, items):
   rt = []
   for value in items:
      if isinstance(value, list):
         rt.append(scale_tree(factor, value))
      else:
         rt.append(factor * value)
   return rt

print (scale_tree(10, [1, [2, [3, 4], 5], [6, 7]]))

def scale_tree(factor, items):
   def map_lambda(sub_tree):
      if isinstance(sub_tree, list):
         return scale_tree(factor, sub_tree)
      else:
         return sub_tree * factor
   return map (map_lambda) (items)

print (scale_tree(10, [1, [2, [3, 4], 5], [6, 7]]))

# Exercise 2.24
print ([1, [2, [3, 4]]])

# Exercise 2.25
print ([1, 3, [5, 7], 9])
print ([[7]])
print ([1, [2, [3, [4, [5, [6, 7]]]]]])

# Exercise 2.26
x = [1, 2, 3]
y = [4, 5, 6]
print (append(x, y))
print ([x, y])

# Exercise 2.27
def deep_reverse(items):
   rt = []
   for value in items:
      if isinstance(value, list):
         rt.insert(0, deep_reverse(value))
      else:
         rt.insert(0, value)
   return rt
x = [[1, 2], [3, 4]]
print (x)
print (reverse(x))
print (deep_reverse(x))

# Exercise 2.28
def fringe(items):
   rt = []
   for value in items:
      if isinstance(value, list):
         for value2 in fringe(value):
            rt.append(value2)
      else:
         rt.append(value)
   return rt
x = [[1, 2], [3, 4]]
print (fringe(x))
print (fringe([x, x]))

# Exercise 2.29
# List-based representation
# a.
def make_mobile(left, right): return (left, right)
def make_branch(length, struc): return (length, struc)
def left_branch(mobile): return mobile[0]
def right_branch(mobile): return mobile[1]
def branch_length(branch): return branch[0]
def branch_structure(branch): return branch[1]

# Helpers for b. and c.
def branch_weight(branch):
   if len(branch) == 0:
      return 0
   elif isinstance(branch, list):
      return branch_weight(branch_structure(branch))
   else:
      return branch_structure(branch)
def total_branch_length(branch):
   if len(branch) == 0:
      return 0
   elif isinstance(branch, list):
      return branch_length(branch) + total_branch_length(branch_structure(branch))
   else:
      return branch_length(branch)

# b.
def total_weight(mobile):
   return branch_weight(left_branch(mobile)) + branch_weight(right_branch(mobile))

# c. [Not as per specification]
def is_mobile_balanced(mobile):
   lmwl = total_branch_length(left_branch(mobile)) * branch_weight(left_branch(mobile))
   rmwl = total_branch_length(right_branch(mobile)) * branch_weight(right_branch(mobile))
   return lmwl == rmwl

# Exercise 2.30
def square_tree(items):
   rt = []
   for value in items:
      if isinstance(value, list):
         rt.append(square_tree(value))
      else:
         rt.append(value*value)
   return rt
print (square_tree([1, [2, [3, 4], 5], [6, 7]]))

# Exercise 2.31
def tree_map(items, proc):
   rt = []
   for value in items:
      if isinstance(value, list):
         rt.append(tree_map(value, proc))
      else:
         rt.append(proc(value))
   return rt
def square_tree(items):
   return tree_map(items, lambda x: x * x)
print (square_tree([1, [2, [3, 4], 5], [6, 7]]))

# Exercise 2.32
def subsets(items):
   if (len(items) == 0):
      return [[]]
   else:
      head = items[0]
      tail = items[1:]
      rest = subsets(tail)
      return append(rest, map (lambda x: append([head], x)) (rest))
print (subsets([1, 2, 3]))

# 2.2.3 Hierarchical Data and the Closure Property - Sequences as Conventional Interfaces
def is_odd(n): return n % 2 == 1
def is_even(n): return not(is_odd(n))
def square(x): return x * x

def sum_odd_squares(items):
   sum = 0
   for value in items:
      if isinstance(value, list):
         sum = sum + sum_odd_squares(value)
      elif is_odd(value):
         sum = sum + square(value)
   return sum

def even_fibs(n):
   rt = []
   for i in range(1, n+1):
      f = fib(i)
      if is_even(f):
         rt.append(f)
   return rt

print (even_fibs(10))

# Sequence operations
print (map (square) ([1,2,3,4,5]))

# non-curried version of filter
def filter(predicate, items):
   rt = []
   for value in items:
      if predicate(value):
         rt.append(value)
   return rt

print (filter(is_odd, [1,2,3,4,5]))

# curried version of filter
def filter(predicate):
   def filter_lambda(items):
      rt = []
      for value in items:
         if predicate(value):
            rt.append(value)
      return rt
   return filter_lambda

print (filter (is_odd) ([1,2,3,4,5]))

# non-curried version of accumulate (aka foldl)
def accumulate(oper, initial, items):
   rt = initial
   for value in items:
      rt = oper(value, rt)
   return rt

def construct(x, items):
   rt = items[0:]
   rt.append(x)
   return rt

print (accumulate(lambda x,y: x+y, 0, [1,2,3,4,5]))
print (accumulate(lambda x,y: x*y, 1, [1,2,3,4,5]))
print (accumulate(construct, [], [1,2,3,4,5]))

# curried version of accumulate (aka foldl)
def accumulate(oper):
   def initial_lambda(initial):
      def sequence_lambda(items):
         rt = initial
         for value in items:
            rt = oper(value, rt)
         return rt
      return sequence_lambda
   return initial_lambda

print (accumulate (lambda x,y: x+y) (0) ([1,2,3,4,5]))
print (accumulate (lambda x,y: x*y) (1) ([1,2,3,4,5]))
print (accumulate (construct) ([]) ([1,2,3,4,5]))

def enumerate_interval(low, high):
   rt = []
   for i in range(low, high+1):
      rt.append(i)
   return rt

print (enumerate_interval(2,7))

def enumerate_tree(items):
   rt = []
   for value in items:
      if isinstance(value, list):
         for value2 in enumerate_tree(value):
            rt.append(value2)
      else:
         rt.append(value)
   return rt

print (enumerate_tree([1, [2, [3, 4], 5]]))

def sum_odd_squares(tree):
   return (
      accumulate (
         lambda x,y: x+y) (0) (map (square) (filter (is_odd) (enumerate_tree(tree)))))

def even_fibs(n):
   return accumulate (construct) ([]) (filter (is_even) (map (fib) (enumerate_interval(0, n))))

def list_fib_squares(n):
   return accumulate (construct) ([]) (map (square) (map (fib) (enumerate_interval(0, n))))

print (list_fib_squares(10))

def product_of_squares_of_odd_elements(sequence):
   return accumulate (lambda x,y: x*y) (1) (map (square) (filter (is_odd) (sequence)))

print (product_of_squares_of_odd_elements([1,2,3,4,5]))

class Employee:
   def __init__(self, empname, jobtitle, salary):
      self.empname = empname
      self.jobtitle = jobtitle
      self.salary = salary
   def isProgrammer(self):
      return (self.jobtitle == "Programmer")
   def getSalary(self):
      return self.salary

def salary_of_highest_paid_programmer(records):
   return accumulate (max) (0) (map (Employee.getSalary) (filter (Employee.isProgrammer) (records)))

recs = [Employee(empname="Fred", jobtitle="Programmer", salary=180),
        Employee(empname="Hank", jobtitle="Programmer", salary=150)]

print (salary_of_highest_paid_programmer(recs))

# Nested mappings
n = 5                   # book doesn't define n
print (accumulate (append) ([]) (
         map
            (lambda i: map
               (lambda j: [i, j])
               (enumerate_interval(1, i-1)))
            (enumerate_interval(1, n))))

def flatmap(proc):
   def flatmap_lambda(seq):
      return accumulate (append) ([]) (map (proc) (seq))
   return flatmap_lambda

def has_no_divisors(n, c):
   if c == 1:
      return True
   elif n % c == 0:
      return False
   else:
      return has_no_divisors(n, c-1)

def isPrime(n):
   return has_no_divisors(n, n-1)

def prime_sum(pair):
   return isPrime(pair[0] + pair[1])

def make_pair_sum(pair):
   return (pair[0], pair[1], pair[0] + pair[1])

def prime_sum_pairs(n):
   return map(make_pair_sum)(
            filter
               (prime_sum)
               (flatmap
                  (lambda i: map(lambda j: [i,j])(enumerate_interval(1, i-1)))
                  (enumerate_interval(1, n))))

print (prime_sum_pairs(5))

def remove(item, sequence):
   return filter (lambda x: x != item) (sequence)

def permutations(s):
   if (len(s) == 0):
      return [[]]
   else:
      return (
         flatmap
            (lambda x:
               map
                  (lambda p: construct(x, p))
                  (permutations(remove(x, s))))
            (s))

print (permutations([1,2,3]))

# Exercise 2.34
# exercise left to reader to define appropriate functions
# def horner_eval(x, coefficient_sequence):
#    return accumulate (lambda this_coeff, higher_terms: ??FILL_THIS_IN??) (0) (coefficient_sequence)
# horner_eval(2, [1,3,0,5,0,1])

# Exercise 2.36
# exercise left to reader to define appropriate functions
# def accumulate_n(oper):
#    def initial_lambda(initial):
#       def sequence_lambda(sequence):
#          if len(sequence) == 0:
#             return initial
#          else:
#             return construct(accumulate (oper) (init) (??FILL_THIS_IN??),
#                              accumulate_n (oper) (init) (??FILL_THIS_IN??))
#       return sequence_lambda
#    return initial_lambda
# accumulate_n (lambda x,y: x + y) (0) (s)

# Exercise 2.38
fold_right = accumulate
def fold_left(oper):
   def initial_lambda(initial):
      def sequence_lambda(items):
         rt = initial
         for value in reverse(items):
            rt = oper(rt, value)
         return rt
      return sequence_lambda
   return initial_lambda
print (fold_right (lambda x,y: x/y) (1.0) ([1,2,3]))
print (fold_left (lambda x,y: x/y) (1.0) ([1,2,3]))
print (fold_right (construct) ([]) ([1,2,3]))
print (fold_left (lambda x,y: construct(y,x)) ([]) ([1,2,3]))

# Exercise 2.42
# exercise left to reader to define appropriate functions
# def queens(board_size):
#    def queen_cols(k):
#       if (k == 0):
#          return [empty_board]
#       else:
#          return (
#             filter
#                (lambda positions: isSafe(k, positions))
#                (flatmap
#                   (lambda rest_of_queens:
#                      map
#                         (lambda new_row: adjoin_position(new_row, k, rest_of_queens))
#                         (enumerate_interval(1, board_size)))
#                   (queen_cols(k-1))))
#    return queen_cols(board_size)

# Exercise 2.43
# exercise left to reader to define appropriate functions
# def queens(board_size):
#    def queen_cols(k):
#       if (k == 0):
#          return [empty_board]
#       else:
#          return (
#             filter
#                (lambda positions: isSafe(k, positions))
#                (flatmap
#                   (lambda new_row:
#                      map
#                         (lambda rest_of_queens: adjoin_position(new_row, k, rest_of_queens))
#                         (queen_cols(k-1)))
#                   (enumerate_interval(1, board_size))))
#    return queen_cols(board_size)

# 2.2.4 Hierarchical Data and the Closure Property - Example: a picture language

# these two routines are to be written
def draw_line(x, y): nop
def wave(xframe): return xframe

class Vect:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def getX(self):
      return self.x
   def getY(self):
      return self.y

def make_vect(x, y): return Vect(x, y)
def xcor_vect(v): return v.getX()
def ycor_vect(v): return v.getY()
def add_vect(v1, v2):
   return make_vect(xcor_vect(v1) + xcor_vect(v2), ycor_vect(v1) + ycor_vect(v2))
def sub_vect(v1, v2):
   return make_vect(xcor_vect(v1) - xcor_vect(v2), ycor_vect(v1) - ycor_vect(v2))
def scale_vect(s, v):
   return make_vect(s * xcor_vect(v), s * ycor_vect(v))

class Frame:
   def __init__(self, orig, edge1, edge2):
      self.orig = orig
      self.edge1 = edge1
      self.edge2 = edge2
   def getOrig(self):
      return self.orig
   def getEdge1(self):
      return self.edge1
   def getEdge2(self):
      return self.edge2

def make_frame(origin, edge1, edge2):
   return Frame(origin, edge1, edge2)
def origin_frame(f): return f.getOrig()
def edge1_frame(f): return f.getEdge1()
def edge2_frame(f): return f.getEdge2()
a_frame = make_frame(make_vect(0.0, 0.0), make_vect(1.0, 0.0), make_vect(0.0, 1.0))

class Segment:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def getX(self):
      return self.x
   def getY(self):
      return self.y

def start_segment(seg): return seg.getX()
def end_segment(seg): return seg.getY()

# Frames
def frame_coord_map(xframe, v):
   return add_vect(
      origin_frame(xframe),
      add_vect(scale_vect(xcor_vect(v), edge1_frame(xframe)),
               scale_vect(ycor_vect(v), edge2_frame(xframe))))

frame_coord_map(a_frame, make_vect(0.0, 0.0))
origin_frame(a_frame)

# Painters
def foreach(f):
   def foreach_lambda(items):
      for value in items:
         f(value)
   return foreach_lambda

def segments_painter(segment_list, xframe):
   (foreach
      (lambda segment:
         draw_line
            (frame_coord_map(xframe)(start_segment, segment)),
            (frame_coord_map(xframe)(end_segment, segment)))
      (segment_list))

def transform_painter(painter, origin, corner1, corner2):
   def transform_painter_lambda(xframe):
      m = frame_coord_map(xframe)
      new_origin = m(origin)
      return painter(
         make_frame(
            new_origin,
            sub_vect(m(corner1), new_origin),
            sub_vect(m(corner2), new_origin)))
   return transform_painter_lambda

def flip_vert(painter):
   return transform_painter(
      painter,
      make_vect(0.0, 1.0),
      make_vect(1.0, 1.0),
      make_vect(0.0, 0.0))

def flip_horiz(painter):
   return transform_painter(
      painter,
      make_vect(1.0, 0.0),
      make_vect(0.0, 0.0),
      make_vect(1.0, 1.0))

def shrink_to_upper_right(painter):
   return transform_painter(
      painter,
      make_vect(0.5, 0.5),
      make_vect(1.0, 0.5),
      make_vect(0.5, 1.0))

def rotate90(painter):
   return transform_painter(
      painter,
      make_vect(1.0, 0.0),
      make_vect(1.0, 1.0),
      make_vect(0.0, 0.0))

def rotate180(painter):
   return transform_painter(
      painter,
      make_vect(1.0, 1.0),
      make_vect(0.0, 1.0),
      make_vect(1.0, 0.0))

def squash_inwards(painter):
   return transform_painter(
      painter,
      make_vect(0.0, 0.0),
      make_vect(0.65, 0.35),
      make_vect(0.35, 0.65))

def beside(painter1, painter2):
   def beside_lambda(xframe):
      split_point = make_vect(0.5, 0.0)
      paint_left = (
         transform_painter(
            painter1,
            make_vect(0.0, 0.0),
            split_point,
            make_vect(0.0, 1.0)))
      paint_right = (
         transform_painter(
            painter2,
            split_point,
            make_vect(1.0, 0.0),
            make_vect(0.5, 1.0)))
      paint_left(xframe)
      paint_right(xframe)
   return beside_lambda

def below(painter1, painter2):
   def below_lambda(xframe):
      split_point = make_vect(0.0, 0.5)
      paint_below = (
         transform_painter(
            painter1,
            make_vect(0.0, 0.0),
            make_vect(1.0, 0.0),
            split_point))
      paint_above = (
         transform_painter(
            painter2,
            split_point,
            make_vect(1.0, 0.5),
            make_vect(0.0, 1.0)))
      paint_below(xframe)
      paint_above(xframe)
   return below_lambda

def up_split(painter, n):
   if (n == 0):
      return painter
   else:
      smaller = up_split(painter, n-1)
      return below(painter, beside(smaller, smaller))

wave2 = beside(wave, flip_vert(wave))

wave4 = below(wave2, wave)

def flipped_pairs(painter):
   painter2 = beside(painter, flip_vert(painter))
   return below(painter2, painter2)

wave4 = flipped_pairs(wave)

def right_split(painter, n):
   if (n == 0):
      return painter
   else:
      smaller = right_split(painter, n-1)
      return beside(painter, below(smaller, smaller))

def corner_split(painter, n):
   if (n == 0):
      return painter
   else:
      up = up_split(painter, n-1)
      right = right_split(painter, n-1)
      top_left = beside(up, up)
      bottom_right = below(right, right)
      corner = corner_split(painter, n-1)
      return beside(below(painter, top_left),  below(bottom_right, corner))

def square_limit(painter, n):
   quarter = corner_split(painter, n)
   half = beside(flip_horiz(quarter), quarter)
   return below(flip_vert(half), half)

# Higher_order operations
def square_of_four(tleft, tright, bleft, bright):
   def square_of_four_lambda(painter):
      top = beside(tleft(painter), tright(painter))
      bottom = beside(bright(painter), bright(painter))
      return below(bottom, top)
   return square_of_four_lambda

def flipped_pairs(painter):
   combine4 = square_of_four(identity, flip_vert, identity, flip_vert)
   return combine4(painter)

# footnote
flipped_pairs = square_of_four(identity, flip_vert, identity, flip_vert)

def square_limit(painter, n):
   combine4 = square_of_four(flip_horiz, identity, rotate180, flip_vert)
   return combine4(corner_split(painter, n))

# Exercise 2.45
# exercise left to reader to define appropriate functions
# right_split = split(beside, below)
# up_split = split(below, beside)

# Exercise 2.47
def make_frame(origin, edge1, edge2):
   return [origin, edge1, edge2]
def make_frame(origin, edge1, edge2):
   return [origin, [edge1, edge2]]

# 2.3.1 Symbolic Data - Quotation

# To Be Done.

# 2.3.2 Symbolic Data - Example: Symbolic Differentiation
class Sum:
   def __init__(self, add_end, aug_end):
      self.add_end = add_end
      self.aug_end = aug_end
   def __str__(self):
      return "Sum(" + str(self.add_end) + ", " + str(self.aug_end) + ")"

class Product:
   def __init__(self, multiplier, multiplicand):
      self.multiplier = multiplier
      self.multiplicand = multiplicand
   def __str__(self):
      return "Product(" + str(self.multiplier) + ", " + str(self.multiplicand) + ")"

def is_number(x):
   return isinstance(x, int) or isinstance(x, float)

def is_same_number(x, y):
   return is_number(x) and is_number(y) and (x == y)

def is_variable(x):
   return isinstance(x, str)

def is_same_variable(x, y):
   return is_variable(x) and is_variable(y) and x == y

def is_sum(items):
   return isinstance(items, Sum)

def is_product(items):
   return isinstance(items, Product)

def make_sum(x, y):
   if is_number(x) and is_number(y):
      return x + y
   else:
      return Sum(x, y)

def make_product(x, y):
   if is_number(x) and is_number(y):
      return x * y
   else:
      return Product(x, y)

def add_end(items):
   if is_sum(items):
      return items.add_end
   else:
      raise Exception("Invalid pattern match " + str(items))

def aug_end(items):
   if is_sum(items):
      return items.aug_end
   else:
      raise Exception("Invalid pattern match " + str(items))

def multiplier(items):
   if is_product(items):
      return items.multiplier
   else:
      raise Exception("Invalid pattern match " + str(items))

def multiplicand(items):
   if is_product(items):
      return items.multiplicand
   else:
      raise Exception("Invalid pattern match " + str(items))

def deriv(exp, var):
   if is_number(exp):
      return 0
   elif is_variable(exp):
      if is_same_variable(exp, var):
         return 1
      else:
         return 0
   elif is_sum(exp):
      return make_sum(deriv(add_end(exp), var),
                      deriv(aug_end(exp), var))
   elif is_product(exp):
      return make_sum(make_product(multiplier(exp), deriv(multiplicand(exp), var)),
                      make_product(deriv(multiplier(exp), var), multiplicand(exp)))
   else:
      raise Exception("Invalid expression " + str(exp))

# dx(x + 3) = 1
print (deriv(Sum('x', 3), 'x'))

# # dx(x*y) = y
print(deriv(Product('x', 'y'), 'x'))

# dx(x*y + x + 3) = y + 1
print(deriv(Sum(Sum(Product('x', 'y'), 'x'), 3), 'x'))

# With simplification
def make_sum(x, y):
   if is_number(x) and x == 0:
      return y
   elif is_number(y) and y == 0:
      return x
   elif is_number(x) and is_number(y):
      return x + y
   else:
      return Sum(x, y)

def make_product(x, y):
   if is_number(x)and x == 0:
      return 0
   elif is_number(y) and y == 0:
      return 0
   elif is_number(x) and x == 1:
      return y
   elif is_number(y) and y == 1:
      return x
   elif is_number(x) and is_number(y):
      return x * y
   else:
      return Product(x, y)

def deriv(exp, var):
   if is_number(exp):
      return 0
   elif is_variable(exp):
      if is_same_variable(exp, var):
         return 1
      else:
         return 0
   elif is_sum(exp):
      return make_sum(deriv(add_end(exp), var),
                      deriv(aug_end(exp), var))
   elif is_product(exp):
      return make_sum(make_product(multiplier(exp), deriv(multiplicand(exp), var)),
                      make_product(deriv(multiplier(exp), var), multiplicand(exp)))
   else:
      raise Exception("Invalid expression " + str(exp))

# dx(x + 3) = 1
print (deriv(Sum('x', 3), 'x'))

# # dx(x*y) = y
print(deriv(Product('x', 'y'), 'x'))

# dx(x*y + x + 3) = y + 1
print(deriv(Sum(Sum(Product('x', 'y'), 'x'), 3), 'x'))

# 2.3.3 Symbolic Data - Example: Representing Sets

# unordered
def is_element_of_set(x, items):
   for value in items:
      if x == value:
         return True
   return False

def adjoin_set(x, items):
   if is_element_of_set(x, items):
      return items
   else:
      return items.insert(0, x)

def intersection_set(xs, ys):
   rt = []
   for value in xs:
      if is_element_of_set(value, ys):
         rt.append(value)
   return rt

# ordered
def is_element_of_set(x, items):
   for value in items:
      if x == value:
         return True
      elif x < value:
         return False
   return False

def intersection_set(xs, ys):
   rt = []
   i = 0
   j = 0
   while i < len(xs) and j <= len(ys):
      if xs[i] == ys[j]:
         rt.append(xs[i])
         i = i + 1
         j = j + 1
      elif xs[i] < ys[j]:
         i = i + 1
      else:
         j = j + 1
   return rt

class Node:
   def __init__(self, value, left, right):
      self.value = value
      self.left = left
      self.right = right
   def __str__(self):
      return "Node(" + str(self.value) + ", " + str(self.left) + ", " + str(self.right) + ")"

def is_element_of_set(x, node):
   if node == ():
      return False
   else:
      if x == node.value:
         return True
      elif x < node.value:
         return is_element_of_set(x, node.left)
      else:
         return is_element_of_set(x, node.right)

print (is_element_of_set(3, Node(2, Node(1, (), ()), Node(3, (), ()))))

def adjoin_set(x, node):
   if node == ():
      return Node(x, (), ())
   else:
      if x == node.value:
         return node
      elif x < node.value:
         return Node(node.value, adjoin_set(x, node.left), node.right)
      else:
         return Node(node.value, node.left, adjoin_set(x, node.right))

print (adjoin_set(3, Node(4, Node(2, (), ()), Node(6, (), ()))))

# Exercise 2.63
def tree_to_list(node):
   if node == ():
      return []
   else:
      return append(tree_to_list(node.left),
                    append(
                       [node.value],
                       tree_to_list(node.right)))

print (tree_to_list(Node(4, Node(2, (), ()), Node(6, (), ()))))

def tree_to_list(node):
   def copy_to_list(node, xs):
      if node == ():
         return xs
      else:
         return copy_to_list(node.left, append([node.value], copy_to_list(node.right, xs)))
   return copy_to_list(node, [])

print (tree_to_list(Node(4, Node(2, (), ()), Node(6, (), ()))))

# Exercise 2.64
def partial_tree(elts, n):
   if n == 0:
      return {"foo":(), "bar":elts}
   else:
      left_size = math.floor((n-1) / 2.0)
      right_size = n - (left_size + 1)
      left_result = partial_tree(elts, left_size)
      left_tree = left_result["foo"]
      non_left_elts = left_result["bar"]
      this_entry = non_left_elts[0]
      right_result = partial_tree(non_left_elts[1:], right_size)
      right_tree = right_result["foo"]
      remaining_elts = right_result["bar"]
      return {"foo":Node(this_entry, left_tree, right_tree), "bar":remaining_elts}

def list_to_tree(elements):
   result = partial_tree(elements, len(elements))
   return result["foo"]

print (list_to_tree([2, 4, 6]))

# information retrieval
def lookup(given_key, items):
   if given_key in items:
      return items[given_key]
   return ()
print (lookup(2, {1:'a', 2:'b', 3:'c'}))

# 2.3.4 Symbolic Data - Example: Huffman Encoding Trees
class Leaf:
   def __init__(self, symbol, weight):
      self.symbol = symbol
      self.weight = weight
   def __str__(self):
      return "Leaf(" + str(self.symbol) + ", " + str(self.weight) + ")"

class Tree:
   def __init__(self, subsymbols, weight, left, right):
      self.subsymbols = subsymbols
      self.weight = weight
      self.left = left
      self.right = right
   def __str__(self):
      return "Tree(" + str(self.symbol) + ", " + str(self.weight) + ", " + str(self.left) + ", " + str(self.right) + ")"

def make_leaf(symbol, weight):
   return Leaf(symbol, weight)

def is_leaf(node):
   return isinstance(node, Leaf)

def symbol_leaf(node):
   if is_leaf(node):
      return node.symbol
   else:
      raise Exception("Invalid pattern match " + str(node))

def weight_leaf(node):
   if is_leaf(node):
      return node.weight
   else:
      raise Exception("Invalid pattern match " + str(node))

def symbols(node):
   if is_leaf(node):
      return [node.symbol]
   else:
      return node.subsymbols

def weight(node):
   return node.weight

def make_code_tree(left, right):
   return Tree(append(symbols(left), symbols(right)), weight(left) + weight(right), left, right)

def left_node(node):
   if not(is_leaf(node)):
      return node.left
   else:
      raise Exception("Invalid pattern match " + str(node))

def right_node(node):
   if not(is_leaf(node)):
      return node.right
   else:
      raise Exception("Invalid pattern match " + str(node))

def choose_node(n, node):
   if n == 0:
      return left_node(node)
   elif n == 1:
      return right_node(node)
   else:
      raise Exception("Invalid pattern match " + str(n))

# decoding
def decode(bits, tree):
   def decode_1(bits, current_node):
      if len(bits) == 0:
         return []
      else:
         head = bits[0]
         tail = bits[1:]
         next_node = choose_node(head, current_node)
         if is_leaf(next_node):
            return append([symbol_leaf(next_node)], decode_1(tail, tree))
         else:
            return decode_1(tail, next_node)
   return decode_1(bits, tree)

# sets
def adjoin_set(x, items):
   if node == ():
      return [x]
   else:
      head = items[0]
      if weight(x) < weight(head):
         return append([x], items)
      else:
         tail = items[1:]
         return append(head, adjoin_set(x, tail))

def make_leaf_set(node):
   head = node[0]
   tail = node[1:]
   if is_leaf(head):
      return adjoin_set(make_leaf(symbol_leaf(head), symbol_weight(head)), make_leaf_set(tail))
   else:
      raise Exception("Invalid pattern match " + str(node))

# Exercise 2.67
sample_tree = make_code_tree(
      make_leaf('A', 4),
      make_code_tree(
         make_leaf('B', 2),
         make_code_tree(
            make_leaf('D', 1),
            make_leaf('C', 1))))

sample_message = [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]

print (decode(sample_message, sample_tree))

# Exercise 2.68
# exercise left to reader to define appropriate functions
# def encode(message, tree):
#    if len(message) == 0:
#       return []
#    else
#       head = message[0]
#       tail = message[1:]
#       return append(encode_symbol(head, tree), encode(tail, tree))

# 2.4.1 Multiple Representations for Abstract Data - Representations for Complex Numbers

# Same as above
def square(x): return x * x

class Rectangular:
   def __init__(self, real, imag):
      self.real = real
      self.imag = imag
   def __str__(self):
      return "Rectangular(" + str(self.real) + ", " + str(self.imag) + ")"

class Polar:
   def __init__(self, magnitude, angle):
      self.magnitude = magnitude
      self.angle = angle
   def __str__(self):
      return "Polar(" + str(self.magnitude) + ", " + str(self.angle) + ")"

# Rectangular
def real_part_r(z): return z.real
def imag_part_r(z): return z.imag

def magnitude_r(z):
   return math.sqrt(square(real_part_r(z)) + square(imag_part_r(z)))

def angle_r(z):
  return math.atan2(imag_part_r(z), real_part_r(z))

def make_from_real_imag_r(x, y): return Rectangular(x, y)
def make_from_mag_ang_r(r, a):
   return Rectangular(r*math.cos(a), r*math.sin(a))

# polar
def magnitude_p(z): return z.magnitude
def angle_p(z): return z.angle

def real_part_p(z):
   return magnitude_p(z) * math.cos(angle_p(z))

def imag_part_p(z):
   return magnitude_p(z) * math.sin(angle_p(z))

def make_from_real_imag_p(x, y):
   return Polar(math.sqrt(square(x) + square(y)), math.atan2(y, x))

def make_from_mag_ang_p(r, a):
   return Polar(r, a)

# using the abstract type
magnitude = magnitude_r
angle = angle_r
real_part = real_part_r
imag_part = imag_part_r
make_from_real_imag = make_from_real_imag_r
make_from_mag_ang = make_from_mag_ang_r

z = Rectangular(1, 2)
print (make_from_real_imag(real_part(z), imag_part(z)))
print (make_from_mag_ang(magnitude(z), angle(z)))

def add_complex(z1, z2):
   return make_from_real_imag(
      real_part(z1) + real_part(z2),
      imag_part(z1) + imag_part(z2))

def sub_complex(z1, z2):
   return make_from_real_imag(
      real_part(z1) - real_part(z2),
      imag_part(z1) - imag_part(z2))

def mul_complex(z1, z2):
   return make_from_mag_ang(
      magnitude(z1) * magnitude(z2),
      angle(z1) + angle(z2))

def div_complex(z1, z2):
   return make_from_mag_ang(
      magnitude(z1) / magnitude(z2),
      angle(z1) - angle(z2))

# 2.4.2 Multiple Representations for Abstract Data - Tagged Data

def type_tag(a):
   if isinstance(a, Rectangular):
      return 'rectangular'
   elif isinstance(a, Polar):
      return 'polar'
   else:
      raise Exception("Invalid pattern match " + str(a))

def contents(a):
   return a

def is_rectangular(a):
   return isinstance(a, Rectangular)

def is_polar(a):
   return isinstance(a, Polar)

# Rectangular
def make_from_real_imag_rectangular(x, y):
   return Rectangular(x, y)
def make_from_mag_ang_rectangular(r, a):
   return Rectangular(r*math.cos(a), r*math.sin(a))

def real_part_rectangular(z):
   return z.real
def imag_part_rectangular(z):
   return z.imag

def magnitude_rectangular(z):
   return math.sqrt(square(real_part_rectangular(z)) + square(imag_part_rectangular(z)))
def angle_rectangular(z):
   math.atan2(imag_part_rectangular(z), real_part_rectangular(z))

# Polar
def make_from_real_imag_polar(x, y):
   return Polar(math.sqrt(square(x) + square(y)), math.atan2(y, x))
def make_from_mag_ang_polar(r, a):
   return Polar(r, a)

def magnitude_polar(z):
   return z.magnitude
def angle_polar(z):
   return z.angle

def real_part_polar(z):
   return magnitude_polar(z) * math.cos(angle_polar(z))
def imag_part_polar(z):
   return magnitude_polar(z) * math.sin(angle_polar(z))

# Generic selectors
def real_part_g(a):
   if is_rectangular(a):
      return real_part_rectangular(a)
   elif is_polar(a):
      return real_part_polar(a)
   else:
      raise Exception("Invalid pattern match " + str(a))
def imag_part_g(a):
   if is_rectangular(a):
      return imag_part_rectangular(contents(a))
   elif is_polar(a):
      return imag_part_polar(contents(a))
   else:
      raise Exception("Invalid pattern match " + str(a))

def magnitude_g(a):
   if is_rectangular(a):
      return magnitude_rectangular(contents(a))
   elif is_polar(a):
      return magnitude_polar(contents(a))
   else:
      raise Exception("Invalid pattern match " + str(a))
def angle_g(a):
   if is_rectangular(a):
      return angle_rectangular(contents(a))
   elif is_polar(a):
      return angle_polar(contents(a))
   else:
      raise Exception("Invalid pattern match " + str(a))

# Constructors for complex numbers
def make_from_real_imag_g(x, y):
   return make_from_real_imag_rectangular(x, y)
def make_from_mag_ang_g(r, a):
   return make_from_mag_ang_polar(r, a)

# same as before
def add_complex_g(z1, z2):
   return make_from_real_imag_g(
      real_part_g(z1) + real_part_g(z2),
      imag_part_g(z1) + imag_part_g(z2))

def sub_complex_g(z1, z2):
   return make_from_real_imag_g(
      real_part_g(z1) - real_part_g(z2),
      imag_part_g(z1) - imag_part_g(z2))

def mul_complex_g(z1, z2):
   return make_from_mag_ang_g(
      magnitude_g(z1) * magnitude_g(z2),
      angle_g(z1) + angle_g(z2))

def div_complex_g(z1, z2):
   return make_from_mag_ang_g(
      magnitude_g(z1) / magnitude_g(z2),
      angle_g(z1) - angle_g(z2))

print (add_complex_g(make_from_real_imag_g(3, 4), make_from_real_imag_g(3, 4)))

# 2.4.3 Multiple Representations for Abstract Data - Data-Directed Programming and Additivity

# To Be Done.

# 2.5.1 Systems with Generic Operations - Generic Arithmetic Operations

# To Be Done.
