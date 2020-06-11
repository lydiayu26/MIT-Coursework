#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


#c = Coordinate(3,4)
#origin = Coordinate(0,0)
#print(c.x, origin.x)
#print(c.distance(origin))
#print(Coordinate.distance(c, origin))
#print(origin.distance(c))
##print(c)


#################
## EXAMPLE: simple class to represent fractions
#################
class SimpleFraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def times(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.num
        bottom = self.denom*other.denom
        return top/bottom
    def divide(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom
        bottom = self.denom*other.num
        return top/bottom
    def plus(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return top/bottom
    def minus(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bottom = self.denom*other.denom
        return top/bottom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return self.denom/self.num

f1 = SimpleFraction(3, 4)
f2 = SimpleFraction(1, 4)
#print(f1.num)
#print(f1.denom)
#print(f2.num)
#print(f2.denom)
#print(f1.times(f2))
#
#print(f1.divide(f2))
#print(f1.plus(f2))
#print(f1.minus(f2))
#print(f1.inverse())
#
#print(f1)
#print(f1.times(f2))

#################
## EXAMPLE: simple class to represent fractions
## Added functionality by implementing +, -, *, / operators
#################
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __mul__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.num
        bottom = self.denom*other.denom
        return Fraction(top, bottom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return Fraction(top, bottom)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bottom = self.denom*other.denom
        return Fraction(top, bottom)
    def __truediv__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom
        bottom = self.denom*other.num
        return Fraction(top, bottom)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def reduce(self):
        """ Returns a new fraction the reduced version of self 
            using the greatest common divisor """
        def gcd(n, d):
            while d != 0:
                (d, n) = (n%d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1:
            return self.num
        else:
            greatest_common_divisor = gcd(self.num,self.denom)
            top = int(self.num/greatest_common_divisor)
            bottom = int(self.denom/greatest_common_divisor)
            return Fraction(top, bottom)
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

        
a = Fraction(1,4)
b = Fraction(3,4)
#print(a)
c = a * b # c is a Fraction object
#print(c)
#########
# These three are equivalent
#print(float(c))              ##1 (shorthand) same as #2, #3
#print(c.__float__())         ##2 (method call) same as #1, #3
#print(Fraction.__float__(c)) ##3 (explicit class call) same as #1, #2
#
#print(float(b.inverse()))
##########
#print(a**b) # error, did not define it on two Fraction objects
## Test yourself! Write a function call to reduce a fraction and print


