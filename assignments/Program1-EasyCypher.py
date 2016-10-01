"""
Name: Zac Conley
Email: acdczlc@gmail.com
Assignment: Program 1 - Easy Cypher
Due: 3 Oct @ 1:00 p.m.
"""

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
		temp = input('Message: ') #gets input message,works on repl.it,
		self.setMessage(temp)# but not visual studio code

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:
	     message {string}: String message
	     encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message #sets plain text =keyboard message
			self.cleanData() #runs cleandata
			self.__encrypt() #encrypts message
		else:
			self.cipherText = message #if encrypted, message becomes ciphertext
			self.__decrypt() #decrypts the message
	"""
	@ Name: getCipherText
	@ Description: returns self.cipherText
	@ Params: self
	"""
	def getCipherText(self):
		return self.cipherText

	"""
	@ Name: getPlainText
	@ Description: returns self.plainText
	@ Params: self
	"""
	def getPlainText(self):
		return self.plainText

	"""
	@ Name: setShift
	@ Description: sets self.shift as shift
	@ Params: self,shift
	"""
	def setShift(self,shift):
		self.shift = shift
	
	"""
	@ Name: getShift
	@ Description: returns self.shift
	@ Params: self
	"""
	def getShift(self):
		return self.shift
		
	"""
	@ Name: cleanData
	@ Description: removes spaces and capitalizes letters, then
	@ removes everything that is not a letter or number
	@ Params: self
	"""
	def cleanData(self):
		self.cleanText = '' #initializes to empty string for accumulating later
		for letter in self.plainText:
			if ord(letter) == 32: #skips spaces
				continue
			if ord(letter) > 96: #capitalizes letters
				self.cleanText += chr(ord(letter)-32)
			else: #stores already capital letters
				self.cleanText += letter
		self.temporary='' #makes temporary location, so cleanText is 
		for letter in self.cleanText:#not overwritten while the loop runs
			if ord(letter)in range(65,90): #stores capital letters in temporary
				self.temporary+=letter
			elif ord(letter)in range(48,58): #stores numbers in temporary
				self.temporary+=letter #This excludes all non-letters and non-numbers
			self.cleanText=self.temporary #overwrites clean text with temporary
			
	"""
	@ Name: _encrypt
	@ Description: shifts message by shift value
	@ Params: self
	"""
	def __encrypt(self):
		self.cipherText = ''#used for accumulating
		if(not self.cleanText):
			return
		for letter in self.cleanText:
			if(ord(letter)in range(48,58)):	#if values is number, shifts by 3
				self.cipherText+=chr(ord(letter)+self.shift)
			else: #if value is letter, shifts by 3 with wraparound
				self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
		    
		
	
	"""
	@ Name: _decrypt
	@ Description: unshifts message by shift value
	@ Params: self
	"""
	def __decrypt(self):
		self.output=''#for accumulating
		for letter in self.cipherText:
			if(ord(letter)in range(51,61)): #checks if value is a number that had 
				self.output+=chr(ord(letter)-self.shift)#it's ascii increased by shift
			else:										#and decrypts it
				self.output += chr((((ord(letter)-65) - self.shift) % 26)+65)#subtracts shift with
		self.cleanText=self.output											#wraparound
			

"""
Only run this if we call this file directly:
"""

if __name__=='__main__': #remove on repl.it and unshift everything below

    alice = ShiftCipher()
    alice.promptUserMessage()
    print(alice)


    bob = ShiftCipher()
    bob.setMessage(alice.getCipherText(),True)
    print(bob)