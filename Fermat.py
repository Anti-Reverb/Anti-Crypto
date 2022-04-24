#Fermat Theorem
a = int(input('Enter a prime number:')); p = int(input('Enter p:'))
n = pow(a,p-1) % p
if(n == 1): print('Fermat Little Theorem is true')
else: print('Fermat little theorem is false')