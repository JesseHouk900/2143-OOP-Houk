
def gcd(x, y):
		while y:	  
			x, y = y, x % y
		return x



class Fraction(object):
	def __init__(self,n=None,d=None):
		self.numerator = n
		self.denominator = d
		self._reduce()

	def __str__(self):
		if (self.numerator / self.denominator) >= 1:
			if (self.numerator % self.denominator) == 0:
				return "%d" % (self.numerator / self.denominator)
			else:
				return "%d %d / %d" % ((self.numerator / self.denominator), (self.numerator % self.denominator), self.denominator)
		return "%d / %d" % (self.numerator , self.denominator)

	def numerator(self,n):
		self.numerator = n 

	def denominator(self,d):
			self.denominator = d
		
	def __div__(self, rhs):
		y = self.denominator * rhs.numerator
		x = self.numerator * rhs.denominator
		return Fraction(x, y)

	def __mul__(self,rhs):
		x = self.numerator * rhs.numerator
		y = self.denominator * rhs.denominator
		return Fraction(x,y)
	
	def __add__(self, rhs):
		y = self.denominator * rhs.denominator
		x = (self.numerator * rhs.denominator) + (self.denominator * rhs.numerator)
		if x / y == 1:
			return 1
		else:
			return Fraction(x, y)
	
	def _reduce(self):
		gcdNum = gcd(self.numerator, self.denominator)
		self.numerator = self.numerator / gcdNum
		self.denominator = self.denominator / gcdNum   

a = Fraction(7,2)
b = Fraction(24,4)
c = a + b
print(c)
input("Press ENTER to continue...")