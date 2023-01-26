import os
import json

ALPHABET_LETTERS = 26

def isUppercase(letter):
    if ord(letter) < ord('A') or ord(letter) > ord('Z'):
        return False
    return True

def isLowercase(letter):
    if ord(letter) < ord('a') or ord(letter) > ord('z'):
        return False
    return True

class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.alteredList = []
        self.alteredString = ""
        self.lowercase = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.uppercase = [chr(i) for i in range(ord('A'), ord('Z')+1)]



    def encrypt(self, string):
        for letter in string:
            if isUppercase(letter):
                index = self.lowercase.index(letter)
                self.alteredList.append(
                    (self.uppercase[((index + self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            elif isLowercase(letter):
                index = self.uppercase.index(letter)
                self.alteredList.append(
                    (self.lowercase[((index + self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            else:
                self.alteredList.append(letter)


        for elem in self.alteredList:
            self.alteredString += elem

        return self.alteredString

    def decrypt(self, string):
        for letter in string:
            if isUppercase(letter):
                index = self.lowercase.index(letter)
                self.alteredList.append((self.uppercase[((index - self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            elif isLowercase(letter):
                index = self.uppercase.index(letter)
                self.alteredList.append((self.lowercase[((index - self.key) % ALPHABET_LETTERS) + ALPHABET_LETTERS]) % ALPHABET_LETTERS)
            else:
                self.alteredList.append(letter)

            for elem in self.alteredList:
                self.alteredString += elem

        return self.alteredString

    def changeKey(self, newKey):
        self.key = newKey


class VigenereCypher(CaesarCipher):
    def __init__(self, key):
    #     self.key = key
        # self.alteredList = []
        # self.alteredString = ""
        # self.lowerCase = [chr(i) for i in range(ord('a'), ord('z')+1)]
        # self.upperCase = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        self.keySize = key.size()
    cypher = CaesarCipher(0)

    def encryptLetter(self, letter, oneTimeKey):
        self.cypher.changeKey(oneTimeKey)
        alteredLetter = self.cypher.encrypt(letter)
        return alteredLetter

    def decryptLetter(self, letter, oneTimeKey):
        self.cypher.changeKey(oneTimeKey)
        alteredLetter = self.cypher.decrypt(letter)
        return alteredLetter

    def encrypt(self, string):
        c = 0
        for letter in string:
            index = self.key[c % self.keySize]
            self.alteredList.append(self.encryptLetter(letter, index))
            c += 1
        for elem in self.alteredList:
            self.alteredString += elem

        return self.alteredString

    def decrypt(self, string):
        c = 0

        for letter in string:
            index = self.key[c % self.keySize]
            self.alteredList.append(self.decryptLetter(letter, index))
            c += 1
        for elem in self.alteredList:
            self.alteredString += elem

        return self.alteredString

def getVigenereFromStr(keyString):
    lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    uppercase = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    alphabet = []
    for elem in lowercase:
        alphabet.append(elem)
    for elem in uppercase:
        alphabet.append(elem)

    keyList = []
    for letter in keyString:
        keyList.append(alphabet.index(letter))

    vigenere = VigenereCypher(keyList)
    return vigenere

def processDirectory(dir_path):
    file_path = os.path.join(dir_path, "config.json")
    with open(file_path, "r") as file:
        loaded_dict = json.load(file)

    if loaded_dict['type'] == "Caesar":
        caesar_cipher = CaesarCipher(loaded_dict['key'])
    elif loaded_dict['type'] == "Vigenere":
        vigenere_cipher = VigenereCypher(loaded_dict['key'])
    if loaded_dict['mode'] == "encrypt":
        for filename in os.listdir(dir_path):
                    if filename.endswith(".txt"):
                        with open(file_path, "r") as f:
                            data = f.read()
                            if loaded_dict['type'] == "Caesar":
                                data = caesar_cipher.encrypt(data)
                            elif loaded_dict['type'] == "Vigenere":
                                data = vigenere_cipher.encrypt(data)
                            filename -= ".txt"
                            with open(filename + ".enc", "w") as w:
                                w.write(data)

    if loaded_dict['mode'] == "decrypt":
        for filename in os.listdir(dir_path):
                    if filename.endswith(".enc"):
                        with open(file_path, "r") as f:
                            data = f.read()
                            if loaded_dict['type'] == "Caesar":
                                data = caesar_cipher.decrypt(data)
                            elif loaded_dict['type'] == "Vigenere":
                                data = vigenere_cipher.decrypt(data)
                            filename -= ".enc"
                            with open(filename + ".txt", "w") as w:
                                w.write(data)