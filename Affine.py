# affine cipher
# E(x) : (ax + b) mod m
#D(x) = c(x-b) mod m where c is modular multipilcative inverse of a #gcd of c and m should be 1
a_input = input('Enter the plain text:')
a = int(input('Enter the first key:'))
b = int(input('Enter the second key:'))
def encrypt_affine(a_input,a,b): 
    f = []
    if a_input.isupper():
        for i in a_input:
            e = (((a*ord(i)) + b)-65) % 26 +65
            f.append(chr(e))
    else:
        for i in a_input:
            e = ((a*ord(i) + b)-97) % 26 +97
            f.append(chr(e))
    return ''.join(f)
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
def decrypt_affine(cipher_text,a,b): 
    c= modInverse(a,26)
    f = []
    if cipher_text.isupper():
        for i in cipher_text:
            d = ( (c*(ord(i)-b)) - 65) % 26 +65
            f.append(chr(d))
    else:
        for i in cipher_text:
            d = ( (c*(ord(i)-b)) - 97) % 26 +97
            f.append(chr(d))
    return ''.join(f)
print(f"Encrypted value of {a_input} is {encrypt_affine(a_input,a,b)}")
cipher_text = input('Enter cipher text:') 
print(f'Decrypted value of cipher text {cipher_text} is {decrypt_affine(cipher_text,a,b)}')