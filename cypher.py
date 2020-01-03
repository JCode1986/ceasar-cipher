
def encrypt(message, key):
    encrypted_message = ''
    
    if key > 26:
        return 'Enter a number from 1 - 26'

    for char in message:
        
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
            encrypted_message += chr(unicode_num)
        else:
            encrypted_message += char

    return encrypted_message

def decrypt(encoded, key):
    return encrypt(encoded, -key)

def encrypt_input():
    while True:
        e_message = input('\nEnter message to encrypt: ')
        e_key = int(input('\nEnter key number from 1 - 26: '))
        if e_key < 26:
            return f'\nYour encrypted message is =====> {encrypt(e_message, e_key)}'
        else:
            e_key = int(input('\nEnter key number from 1 - 26: '))
            return f'\nYour encrypted message is =====> {encrypt(e_message, e_key)}'


def decrypt_input():
    while True:
        d_message = input('\nEnter message to decrypt: ')
        d_key = int(input('\nEnter key number from 1 - 26: '))
        if d_key < 26:
            return f'\nYour decrypted message is =====> {decrypt(d_message, d_key)}'
        else:
            d_key = int(input('\nEnter key number from 1 - 26: '))        
            return f'\nYour decrypted message is =====> {decrypt(d_message, d_key)}'

def start():
    question = input('\nEncrpyt (e) or Decrypt (d) a message? ')
    if question == 'e':
        return encrypt_input()
    if question == 'd':
        return decrypt_input()   
    start()

if __name__ == "__main__":
    while True:
        print(start())
