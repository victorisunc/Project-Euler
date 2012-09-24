#SICP Chapter #03 Examples in Python
import math

# Functions defined in previous chapters
def gcd(a, b):
   if (b == 0):
      return a
   else:
      return gcd(b, a % b)

def square(x): return x * x
def average(x, y):
   return (x + y) / 2.0
def has_no_divisors(n, c):
   if c == 1:
      return True
   elif n % c == 0:
      return False
   else:
      return has_no_divisors(n, c-1)
def isPrime(n):
   return has_no_divisors(n, n-1)
def enumerate_interval(low, high):
   rt = []
   for i in range(low, high+1):
      rt.append(i)
   return rt
def is_odd(n): return n % 2 == 1
def is_even(n): return not(is_odd(n))

# 3.1.1 - Assignment and State - State Variables
balance = 100

def withdraw(amount):
   global balance
   if balance >= amount:
      balance = balance - amount
      return balance
   else:
      print('InsufficientFunds: ' + str(balance))
      return ()

print (withdraw(25))
print (withdraw(25))
print (withdraw(60))
print (withdraw(15))

def new_withdraw():
   balance = [100]                                    # use list to overcome scoping intricacies in Python
   def withdraw(amount):
      if balance[0] >= amount:
         balance[0] = balance[0] - amount
         return balance[0]
      else:
         print('InsufficientFunds: ' + str(balance[0]))
         return ()
   return withdraw

def make_withdraw(init_balance):
   balance = [init_balance]
   def withdraw(amount):
      if balance[0] >= amount:
         balance[0] = balance[0] - amount
         return balance[0]
      else:
         print('InsufficientFunds: ' + str(balance[0]))
         return ()
   return withdraw

w1 = make_withdraw(100)
w2 = make_withdraw(100)

print (w1(50))
print (w2(70))
print (w2(40))
print (w1(40))

class Account:
   def __init__(self, init_balance):
      self.balance = init_balance
   def withdraw(self, amount):
      if self.balance >= amount:
         self.balance = self.balance - amount
         return self.balance
      else:
         print('InsufficientFunds: ' + str(self.balance))
         return ()
   def deposit(self, amount):
      self.balance = self.balance + amount
      return self.balance
   def getbalance(self):
      return self.balance

acc = Account(100)
acc.withdraw(50)
acc.withdraw(60)
acc.deposit(40)
acc.withdraw(60)
print (acc.getbalance())

Account(100)

# Exercise 3.1
# exercise left to reader to define appropriate functions
# a = make_accumulator(5)
# a.f(10)
# a.f(10)

# Exercise 3.2
# exercise left to reader to define appropriate functions
# s = make_monitored(math.sqrt)
# s.f(100)
# s.how_many_calls()

# Exercise 3.3
# exercise left to reader to define appropriate functions
# acc = Account(100, "secret-password")
# acc.withdraw(40, "secret-password")
# acc.withdraw(50, "some-other-password")

# 3.1.2 - Assignment and State - The Benefits of Introducing Assignment
random_init = 7

def rand_update(x):
   a = 27
   b = 26
   m = 127
   return (a*x + b) % m

def rand():
   global random_init
   x = random_init
   random_init = rand_update(random_init)
   return x

def cesaro_test():
   return gcd(rand(), rand()) == 1

def monte_carlo(trials, experiment):
   def iter (trials_remaining, trials_passed):
      if trials_remaining == 0:
         return trials_passed / trials
      elif experiment():
         return iter(trials_remaining - 1, trials_passed + 1)
      else:
         return iter(trials_remaining - 1, trials_passed)
   return iter(trials, 0)

def estimate_pi(trials):
   return math.sqrt(6.0 / monte_carlo(trials, cesaro_test))

print (estimate_pi(10))

# second version (no assignment)
def random_gcd_test(trials, initial_x):
   def iter(trials_remaining, trials_passed, x):
      x1 = rand_update(x)
      x2 = rand_update(x1)
      if trials_remaining == 0:
         return trials_passed / trials
      elif gcd(x1, x2) == 1:
         return iter(trials_remaining - 1, trials_passed + 1, x2)
      else:
         return iter(trials_remaining - 1, trials_passed, x2)
   return iter(trials, 0, initial_x)

def estimate_pi(trials):
   return math.sqrt(6.0 / random_gcd_test(trials, random_init))

random_init = 7
print (estimate_pi(10))

# Exercise 3.6
# exercise left to reader to define appropriate functions
# def random_in_range(low, high):
#    range = high - low
#    return low + random(range)

# 3.1.3 - Assignment and State - The Cost of Introducing Assignment
def make_simplified_withdraw(init_balance):
   balance = [init_balance]
   def withdraw(amount):
      balance[0] = balance[0] - amount
      return balance[0]
   return withdraw

w = make_simplified_withdraw(25)
print (w(20))
print (w(10))

def make_decrementer(balance):
   return lambda amount: balance - amount

d = make_decrementer(25)
print (d(20))
print (d(10))

make_decrementer(25)(20)
(lambda amount: 25 - amount)(20)
25 - 20

make_simplified_withdraw(25)(20)

# Sameness and change
d1 = make_decrementer(25)
d2 = make_decrementer(25)

w1 = make_simplified_withdraw(25)
w2 = make_simplified_withdraw(25)
print (w1(20))
print (w1(20))
print (w2(20))

peter_acc = Account(100)
paul_acc = Account(100)

peter_acc = Account(100)
paul_acc = peter_acc

# Pitfalls of imperative programming
def factorial(n):
   def iter(product, counter):
      if counter > n:
         return product
      else:
         return iter(counter * product, counter + 1)
   return iter(1, 1)

def factorial(n):
   product = 1
   counter = 1
   def iter():
      if counter > n:
         return product
      else:
         product = counter * product;
         counter = counter + 1;
         return iter()
   return iter()

# Exercise 3.7
# exercise left to reader to define appropriate functions
# paul_acc = make_joint(peter_acc, "open_sesame", "rosebud")

# 3.2.1 - The Environment Model of Evaluation - The Rules for Evaluation
def square(x): return x * x

square = lambda x: x * x

# 3.2.2 - The Environment Model of Evaluation - Applying Simple Procedures
def square(x): x * x

def sum_of_squares(x, y):
   return square(x) + square(y)

def f(a):
   return sum_of_squares(a + 1, a * 2)

# Exercise 3.9
def factorial(n):
   if n == 1:
      return 1
   else:
      return n * factorial(n - 1)

def fact_iter(product, counter, max_count):
   if counter > max_count:
      return product
   else:
      return fact_iter(counter * product, counter + 1, max_count)

def factorial(n):
   return fact_iter(1, 1, n)

# 3.2.3 - The Environment Model of Evaluation - Frames as Repository of State
def make_withdraw(init_balance):
   balance = [init_balance]
   def withdraw(amount):
      if balance[0] >= amount:
         balance[0] = balance[0] - amount
         return balance[0]
      else:
         print('InsufficientFunds: ' + str(balance[0]))
         return ()
   return withdraw

w1 = make_withdraw(100)
print (w1(50))
w2 = make_withdraw(100)

# Exercise 3.10
def make_withdraw(initial_amount):
   balance = [initial_amount]
   def withdraw(amount):
      if balance[0] >= amount:
         balance[0] = balance[0] - amount
         return balance[0]
      else:
         print('InsufficientFunds: ' + str(balance[0]))
         return nil
   return withdraw
w1 = make_withdraw(100)
print (w1(50))
w2 = make_withdraw(100)

# 3.2.4 - The Environment Model of Evaluation - Internal Definitions

# same as in section 1.1.8
def sqrt(x):
   def good_enough(guess):
      return abs(square(guess) - x) < 0.001
   def improve(guess):
      return average(guess, x / guess)
   def sqrt_iter(guess):
      if good_enough(guess):
         return guess
      else:
         return sqrt_iter(improve(guess))
   return sqrt_iter(1.0)

# Exercise 3.11
class Account:
   def __init__(self, init_balance):
      self.balance = init_balance
   def withdraw(self, amount):
      if self.balance >= amount:
         self.balance = self.balance - amount
         return self.balance
      else:
         print('InsufficientFunds: ' + str(self.balance))
         return ()
   def deposit(self, amount):
      self.balance = self.balance + amount
      return self.balance
   def getbalance(self):
      return self.balance

acc = Account(50)
acc.deposit(40)
acc.withdraw(60)
print (acc.getbalance())
acc2 = Account(100)