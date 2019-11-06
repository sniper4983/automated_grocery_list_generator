from math import gcd
from numpy import lcm
import pdb

#use regular expression to devekop the use of strings
class Fraction():
    def __init__(self, num=0, den=1):
        self.numerator = num
        self.denominator = den
        #no need to implement yet no negative teaspoons
        self.sign = '' 

    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    def simplify(self):
        commonDenom = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / commonDenom
        self.denominator = self.denominator / commonDenom
        return self
            
    def __add__(self, rhs):
        if self.denominator != rhs.denominator:
            left = rhs.denominator * self.numerator
            right = self.denominator * rhs.numerator
            self.denominator = lcm(self.denominator, rhs.denominator)
            self.numerator = left + right
            print('hi')
            print(str(left) + ' + ' + str(right) + ' / ' + str(self.denominator) )
            print(self.__str__())
        else:
            #add same denominator way
            self.numerator = self.numerator + rhs.numerator
        print (str(self.numerator))
        
        if self.numerator / self.denominator > 0: #whole number
            self.whole = int(self.numerator / self.denominator)
            self.numerator = self.numerator % self.denominator
                
        self.simplify()
        return self

    #should never be used. will lead to negative numbers not possible in ingredients
    def __sub__(self, rhs):
        if self.denominator != rhs.denominator:
            left = rhs.denominator * self.numerator
            right = self.denominator * rhs.numerator
            self.denominator = lcm(self.denominator, rhs.denominator)
            self.numerator = left - right
            simplify()
        else:
            self.numerator - rhs.numerator

        if self.numerator / self.denominator > 0: #whole number
            self.whole = int(self.numerator / self.denominator)
            self.numerator = self.numerator % self.denominator
        else:
            self.simplify()
            
        return self
    
    def __mul__(self, rhs):
        self.numerator = int(self.numerator * rhs.numerator)
        self.denominator = self.denominator * rhs.denominator
        '''
        if self.numerator / self.denominator > 0: #whole number
            self.whole = self.numerator / self.denominator
            self.numerator = self.numerator % self.denominator
        '''
        #self.simplify()
            
        return self

    def __truediv(self, rhs):
        self.numerator = self.numerator * rhs.denominator
        self.denominator = self.denominator * rhs.numerator

        if self.numerator / self.denominator > 0: #whole number
            self.whole = int(self.numerator / self.denominator)
            self.numerator = self.numerator % self.denominator
        else:
            print('here')
            self.simplify()

        return self


#have to rewrite all functions to incorporate whole number
class Mixed(Fraction):

    def __init__(self, num=1, den=1, whole=0):
        super().__init__(num, den)
        self.whole = whole
        self.numerator = num
        self.denominator = den

    def toFraction(whole, num, den):
        if whole == 0:
            return Mixed(num, den)
        else: #still negative
            return Mixed(den * whole + num, den)

    def __str__(self):
        if self.whole != 0:
            
            return str(self.whole) + " " + super().__str__()
        else:
            return super().__str__()
