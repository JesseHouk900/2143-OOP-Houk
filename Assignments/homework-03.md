```
Jesse Houk
1) []
['blue', 'red', 'green', 'red']
blue
1
1
[]
['blue', 'red', 'green', 'red']
2
2
2)  Doesn't work   
    def take_skittle(self, color):
        if color in self.skittles:
        	self.skittles.pop(self.skittles.index(color))
3)  Neither work
    def take_all(self):
        for skit in self.skittles:
            self.skittles.pop()

	def take_all(self):
		L = []
		while self.skittles:
			L.append(self.skittles.pop())
		return L
```
