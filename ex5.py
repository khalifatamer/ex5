ALPHABET_LETTERS = 26


class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.alteredList = []
        self.alteredString = ""
        self.lowerCase = list(string.ascii_lowercase)
        self.upperCase = list(string.ascii_uppercase)


    def encrypt(self, string):
        for letter in string:
            if isuppercase(letter):
                index = self.lowerCase.index(letter)
                self.alteredList.append(
                    (self.uppercase[((index + self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            elif islowercase(letter):
                index = self.uppercase.index(letter)
                self.alteredList.append(
                    (self.lowercase[((index + self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            else:
                self.alteredList.append(letter)


        for elem in self.alteredList:
            alteredString += elem

        return self.alteredString


    def decrypt(self, string):
        for letter in string:
            if isuppercase(letter):
                index = self.lowerCase.index(letter)
                self.alteredList.append((self.uppercase[((index - self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            elif islowercase(letter):
                index = self.uppercase.index(letter)
                self.alteredList.append((self.lowercase[((index - self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            else:
                self.alteredList.append(letter)

            for elem in self.alteredList:
                alteredString += elem

        return self.alteredString


class VigenereCypher(CaesarCipher):
    def __init__(self, key):
        self.key = key
        self.alteredList = []
        self.alteredString = ""
        self.lowerCase = list(string.ascii_lowercase)
        self.upperCase = list(string.ascii_uppercase)

    def encryptLetter(self, letter, oneTimeKey):
        caesar_cypher_letter = CaesarCipher(oneTimeKey)
        alteredLetter = CaesarCipher.encrypt(letter)
        return alteredLetter

    def encryptLetter(self, letter, oneTimeKey):
        caesar_cypher_letter = CaesarCipher(oneTimeKey)
        alteredLetter = CaesarCipher.decrypt(letter)
        return alteredLetter

    def encrypt(self, string):
        c = 0
        for letter in string:
            index = self.key[0]
            self.alteredList.append(self.encryptLetter(letter, index))
            c += 1
        for elem in self.alteredList:
            self.alteredString += elem

        return self.alteredString

    def decrypt(self, string):
        c = 0

        for letter in string:
            index = self.key[0]
            self.alteredList.append(self.decryptLetter(letter, index))
            c += 1
        for elem in self.alteredList:
            self.alteredString += elem

        return self.alteredString




