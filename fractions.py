from math import gcd
from numpy import lcm

class Fraction():
  def __init__(self, num=0, den=1):
    self.numerator = num
    self.denominator = den
    #no need to implement yet no negative teaspoons
    self.sign = '' 

  def __str__(self):
    return "%d/%d" % (self.numerator, self.denominator)
