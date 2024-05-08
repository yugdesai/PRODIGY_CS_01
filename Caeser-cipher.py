letters='abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if not letter ==" ":
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= len(letters):
                    new_index -= len(letters)
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if not letter ==" ":
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += len(letters)
                plaintext += letters[new_index]
    return plaintext

print()
print("ENCRYPTION AND DECRYPTION USING CAESAR CIPHER")
print()

print("DO YOU WANT TO ECRYPT OR DECRYPT: ")
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
        print('ENCRYPTION SELECTED')
        key = int(input("ENTER THE KEY (1 --> 26) : "))
        plaintext = input("Enter text to encrypt: ")
        ciphertext = encrypt(plaintext,key)
        print(f"ENCRYPTED TEXT: {ciphertext} ")

if user_input == 'd':
        print('DECRYPTION SELECTED')
        key = int(input("ENTER THE KEY (1 --> 26) : "))
        ciphertext = input("Enter text to decrypt: ")
        plaintext = decrypt(ciphertext,key)
        print(f"DECRYPTED TEXT: {plaintext} ")