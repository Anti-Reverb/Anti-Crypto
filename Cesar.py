# Ceaser Cipher
plain_text = input("Enter text which is to be encrypted:")
def encrypt_ceaser(plain_text): 
    c_text = []
    if plain_text.isupper():
        for i in plain_text:
            x = chr(((ord(i) + 3) - 65) % 26 +65)
            c_text.append(x)
    if plain_text.islower():
        for i in plain_text:
            x = chr(((ord(i) + 3) - 97) % 26 +97)
            c_text.append(x)
    return ''.join(c_text)
def decrypt_ceaser(cipher_text): 
    p_text = []
    if cipher_text.isupper(): 
        for i in cipher_text:
            x = chr(((ord(i) - 3) - 65) % 26 + 65)
            p_text.append(x)
    if cipher_text.islower(): 
        for i in cipher_text:
            x = chr(((ord(i) - 3) - 97) % 26 + 97)
            p_text.append(x)
    return ''.join(p_text)
print(f"Cipher Text: {encrypt_ceaser(plain_text)}")
print('--------------------------------------')
cipher_text = input('Enter text which is to be decrypted:')
print(f"Plain Text : {decrypt_ceaser(cipher_text)}")