# M4.py - Password Encryption/Decryption Program
#
# Modify the Password Encryption/Decryption program in the chapter so that the
# program rejects any en- tered password for encryption that is not considered 
# “secure” enough. A password is considered secure if it contains at least ei-
# ght characters, with at least one digit and one special character.
#
# date:    11/04/2016
# author:  n/a
# license: n/a

from random import randint

# helper functions
def is_number(n):
    return ord(n) in range(48, 58)

def is_char(c):
    return ord(c) in ([*range(65, 91)] + [*range(97, 123)])

def is_special_char(c):
    # acsii special char range:
    #   32 --> 47, 58 --> 64, 91 --> 96, 123 --> 126
    return ord(c) in ([*range(32, 48)] + [*range(58, 65)] + \
                      [*range(91, 97)] + [*range(123, 127)])

# encryption:
#   this simple cryptographic algorithm is a fusion of the caesar cipher 
#   and a single rotor Enigma, and is able to emulate the "behaviour" of 
#   a muti-rotor Enigma if is put in series (unlike the real Enigma, the 
#   input will sometimes repeat itslef in this algorithm, which makes it 
#   more secure). The ciphertext produced by this algorithm can deciphe-
#   red using just brute force in probably a second with a digital comp-
#   uter. Therefore, this algorithm is not secure at all. However, this 
#   is still much better than the one the textbook provides. 
#
#   source code credit: Chiayo Lin 2015
#   (just in case of academic dishonesty)
#
def encrypt(plaintext, initial_vector):
    ciphertext = str() 
    for char in plaintext:
        ciphertext += chr((((ord(char) - 32) + initial_vector) % 95) + 32)
        initial_vector += 3
    
    return (ciphertext, initial_vector)

# decryption:
#   the inverse of the encryption function.
def decrypt(ciphertext, final_vector):
    plaintext = str()
    final_vector -= 3 # minus 3 because the intial vector is off by 3
    for char in reversed(ciphertext):
        plaintext += chr((((ord(char) - 32) - final_vector) % 95) + 32)
        final_vector -= 3
    
    return reversed(plaintext)

# program greeting
print('This program will encrypt and decrypt user passwords.')

# get selection (encrypt/decrypt)
which = input('Enter (e) to encrypt a password, and (d) to decrypt: ')

while which != 'e' and which != 'd':
    which = input("\nINVALID - Enter 'e' to encrypt, 'd' to decrypt: ")
 
# assigns True or False
encrypting = (which == 'e')

# get password and perform security check
secure = False
while not secure:
    password_in = input('Enter password: ')
    secure = [*filter(is_special_char, password_in)] and \
             [*filter(is_number, password_in)]       and \
             [*filter(is_char, password_in)]         and \
             len(password_in) >= 8
    
    if not encrypting:
        secure = True 
    elif not secure: 
        print("INVALID -",
              "Must be at least 8 chars, with at least a digit and a symbol.")
    
# perform encryption / decryption and output the result
if encrypting:
    initial_vector = randint(100000, 999999)
    result = encrypt(password_in, initial_vector)
    print("\nDecryption key is:", result[1])
    print("Encrypted password is:", result[0])
else:
    final_vector = int(input("Enter your decryption key: "))
    print("\nDecrypted password: ", 
          *decrypt(password_in, final_vector), sep = '')

