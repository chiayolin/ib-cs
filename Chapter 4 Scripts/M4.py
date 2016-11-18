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

# check if c is a special char
def is_special_char(c):
    # acsii special char range:
    #   32 --> 47, 58 --> 64, 91 --> 96, 123 --> 126
    return ord(c) in ([*range(32, 48)] + [*range(58, 65)] + \
                      [*range(91, 97)] + [*range(123, 127)])

# check if c is a char
def is_char(c):
    return ord(c) in ([*range(65, 91)] + [*range(97, 123)])

# check if n is a number
def is_number(n):
    return ord(n) in range(48, 58)

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a','m'), ('b','h'), ('c','t'), ('d','f'), ('e','g'),
  ('f','k'), ('g','b'), ('h','p'), ('i','j'), ('j','w'), ('k','e'),('l','r'),
  ('m','q'), ('n','s'), ('o','l'), ('p','n'), ('q','i'), ('r','u'), ('s','o'),
  ('t','x'), ('u','z'), ('v','y'), ('w','v'), ('x','d'), ('y','c'), ('z','a'))

# program greeting
print('This program will encrypt and decrypt user passwords\n')

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
             [*filter(is_char, password_in)]         and \
             [*filter(is_number, password_in)]       and \
             len(password_in) >= 8
    
    if not secure: 
        print("INVALID -",
              "Must be at least 8 chars, with at least a digit and a symbol.") 

# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1 
    to_index = 0

for ch in password_in:
    letter_found = False
    
    for t in encryption_key:
        if ('a' <= ch and ch <= 'z') and ch == t[from_index]:  
            password_out = password_out + t[to_index]
            letter_found = True
        elif ('A' <= ch and ch <= 'Z') and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True
            
    if not letter_found:
         password_out = password_out + ch
            
# output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)

