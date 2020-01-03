
def encrypt(word, key):
    encrypted_word = ''
    
    if key > 26:
        return 'Enter a integer from 1 - 26'

    for char in word:

        #isalpha() returns boolean if character is a letter
        if not char.isalpha() and char is not ' ':
            return 'Enter letters of the Alphabet'
        
        if char.isalpha():

            #ord() returns an integer representing the Unicode code point of the character
            unicode_num = ord(char)
            unicode_num += key
            if char.isupper():
                if unicode_num > ord('Z'):
                    unicode_num -= 26
                elif unicode_num < ord('A'):
                    unicode_num += 26
            elif char.islower():
                if unicode_num > ord('z'):
                    unicode_num -= 26
                elif unicode_num < ord('a'):
                    unicode_num += 26

            #chr() returns a character from a string 
            encrypted_word += chr(unicode_num)
        else:
            encrypted_word += char

    return encrypted_word

def decrypt(encoded, key):
    return encrypt(encoded, -key)


if __name__ == "__main__":
    word_to_encrypt = encrypt('aaaaaazZ Testing one two', 3)
    word_to_decode = decrypt('ddddddcC Whvwlqj rqh wzr', 3)
    print(word_to_encrypt)
    print(word_to_decode)

