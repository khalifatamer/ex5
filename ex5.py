ALPHABET_LETTERS

def isUppercase(letter):
  if ord(letter) < ord('A') or ord(letter) > ord('Z'):
    return False
  return True

def isLowercase(letter):
  if ord(letter) < ord('a') or ord(letter) > ord('z'):
    return False
  return True

class CaesarCipher:
	def __init__(self,int key):
		self.key = key
		self.alteredList = []
		self.alteredString = ""
		self.lowerCase = list(string.ascii_lowercase)
		self.upperCase = list(string.ascii_uppercase)

	
	def encrypt(self, string):

		for letter in string:
			if isUppercase(letter):
				index = self.lowerCase.index(letter)
				self.alteredList.append((ALPHABET_LETTERS + (self.uppercase[(index + self.key) % ALPHABET_LETTERS])) % ALPHABET_LETTERS)
			else if isLowercase(letter):
				index = self.uppercase.index(letter)
				self.alteredList.append((ALPHABET_LETTERS + (self.lowercase[(index + self.key) % ALPHABET_LETTERS])) % ALPHABET_LETTERS)
			else
				self.alteredList.append(letter)

		for elem in self.alteredList:
			alteredString += elem

		return self.alteredString

	def decrypt(self, string):
				for letter in string:
			if isUppercase(letter):
				index = self.lowerCase.index(letter)
				self.alteredList.append((ALPHABET_LETTERS + (self.lowercase[(index - self.key) % ALPHABET_LETTERS])) % ALPHABET_LETTERS)
			else if isLowercase(letter):
				index = self.uppercase.index(letter)
				self.alteredList.append((ALPHABET_LETTERS + (self.lowercase[(index  self.key) % ALPHABET_LETTERS])) % ALPHABET_LETTERS)
			else
				self.alteredList.append(letter)

		for elem in self.alteredList:
			alteredString += elem

		return self.alteredString


class VigenereCypher (CaesarCipher):
	def __init__(self, key):
		self.key = key
		self.alteredList = []
		self.alteredString = ""
		self.lowerCase = list(string.ascii_lowercase)
		self.upperCase = list(string.ascii_uppercase)
	
