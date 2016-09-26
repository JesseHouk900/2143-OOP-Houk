
def gcd(x, y):
		while y:	  
			x, y = y, x % y
		return x



class fraction(object):
	def __init__(self,n=None,d=None):
		self.numerator = n
		self.denominator = d
		self._reduce()

	def __str__(self):
		if isinstance((self.numerator / self.denominator), int):
			return "%d" % ((self.numerator / self.denominator))
		return "%d / %d" % (self.numerator , self.denominator)

	def numerator(self,n):
		self.numerator = n 

	def denominator(self,d):
			self.denominator = d
		
	def __div__(self, rhs):
		y = self.denominator * rhs.numerator
		x = self.numerator * rhs.denominator
		return fraction(x, y)

	def __mul__(self,rhs):
		x = self.numerator * rhs.numerator
		y = self.denominator * rhs.denominator
		return fraction(x,y)
	
	def __add__(self, rhs):
		gcdNum = gcd(self.denominator, rhs.denominator)
		if rhs.denominator / gcdNum == self.denominator:
			y = self.denominator * gcdNum
			x = (self.numerator * gcdNum) + rhs.numerator
		if self.denominator / gcdNum == rhs.denominator:
			y = self.denominator
			x = self.numerator + (rhs.numerator * gcdNum)
		
		if self.denominator == rhs.denominator:
			y = self.denominator
			x = self.numerator + rhs.numerator
		if self.denominator < gcdNum and rhs.denominator < gcdNum:
			y = self.denominator * gcdNum
			x = (self.numerator * gcdNum) + (rhs.numerator * gcdNum)
		
		if x / y > 1:
			z = x // y
			x = x - (y * z)
			a = fraction(x, y)
			return "%s %s / %s" % (z, a.numerator, a.denominator)
		else:
			return fraction(x, y)
	
	
	def _reduce(self):
		gcdNum = gcd(self.numerator, self.denominator)
		self.numerator = self.numerator / gcdNum
		self.denominator = self.denominator / gcdNum   

a = fraction(7,2)
b = fraction(0,4)
c = a + b
print(c)
input("Press ENTER to continue...")