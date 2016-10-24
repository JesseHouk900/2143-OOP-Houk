1)
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print('...')
        
class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives = lives
		
	def talk(self):
		"""A cat says meow! when asked to talk."""
		print('meow!')
		
	def lose_life(self):
		"""A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
		self.lives --
		if (self.lives <= 0):
			self.is_alive = False
2)
4
3
AttributeError: 'Foo' object has no attribute 'baz'
3
9
16