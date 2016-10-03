alphaNumeric = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher
"""
class ShiftCipher(object):
	
	"""
	@ Name: __init__
	@ Description: 
	@ Params:
	     None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None
		self.cleanText = None
		self.shift = 3
	"""
	Nice string representation of your class to help debug.
	"""
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
	
	"""
	@ Name: promptUserMessage
	@ Description: Prompts user for message from standard in
	@ Params:
	     None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:
	     message {string}: String message
	     encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		else:
			self.cipherText = message
			self.__decrypt()
	"""
	@ Name: getCipherText
	@ Description: returns the cipherText stored in the object memory.
	@ Params:
	     None
	"""
	def getCipherText(self):
		return self.cipherText
	"""
	@ Name: getPlainText
	@ Description: returns the plainText stored in the object memory.
	@ Params:
	     None
	"""
	def getPlainText(self):
		return self.plainText
	"""
	@ Name: setShift
	@ Description: sets the shift value of the object.
	@ Params:
	     shift {int}: the amount each letter will be changed by.
	"""
	def setShift(self,shift):
		self.shift = shift
	"""
	@ Name: getShift
	@ Description: returns the shift stored in the object memory.
	@ Params:
	     None
	"""
	def getShift(self):
		return self.shift
	"""
	@ Name: cleanData
	@ Description: sets the cleanText value to the values of plainText
			but in uppercase and without any white space.
	@ Params:
	     None
	"""
	def cleanData(self):
		self.cleanText = ''
		for letter in self.plainText:
			if ord(letter) == 32:
				continue
			if ord(letter) < 65 and ord(letter) > 57:
				continue
			if ord(letter) < 48:
				continue
			if ord(letter) > 90 and ord(letter) < 97:
				continue
			if ord(letter) > 122:
				continue
			if ord(letter) > 96:
				self.cleanText += chr(ord(letter)-32)
			else:
				self.cleanText += letter

	"""
    @ Name: __encrypt
    @ Definition: Encrypts plaintext not ciphertext
    @ Params:
        None
	"""
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
			self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
		    
	"""
	if isinstance(chr(ord(letter) - self.shift), int):
				self.plainText += (chr(ord(letter) - self.shift)
				continue
    @ Name: __decrypt
    @ Definition: Decrypts ciphertext not plaintext
    @ Params:
        None
	"""
	def __decrypt(self):
		self.plainText = ''
		for letter in self.cipherText:
			
			if ((((ord(letter) - 65) - self.shift) % 26) < 0):
				self.plainText += (chr((((ord(letter) - 65) - self.shift) % 26) + 65 + 26))
			else:
				self.plainText += (chr((((ord(letter) - 65) - self.shift) % 26) + 65))

"""
Only run this if we call this file directly:
"""
alice = ShiftCipher()
alice.promptUserMessage()
print(alice)


bob = ShiftCipher()
bob.setMessage(alice.getCipherText(),True)
print(bob)