""" The Chinese remainder theorem is a theorem which gives a unique solution to simultaneous
linear congruences with coprime moduli. In its basic form, the Chinese remainder theorem
will determine a number
that, when divided by some given divisors, leaves given
remainders. """

#Chinese Remainder Theorem
a = []
m = [] 
M=1 
result = [] 
Mi = [] 
M_a = [] 
x_temp = 0
input_val = int(input("Enter the number of calculations you want to do:"))
for i in range(input_val):
    j = int(input('Enter the value of a:')) 
    a.append(j)
print('----------------------------------------')
for i in range(input_val):
    j = int(input('Enter the value of m:')) 
    m.append(j)
#M = m1 * m2 * m3
for i in m:
    M=M*i
print(f'Value of M:{M}')

for i in m: 
    j=M/i
    M_a.append(int(j))
print('Values of Mi:',M_a)
#M inverse
for j in m:
    for i in M_a:
        k = pow(int(i),int(j)-2,int(j)) 
        result.append(k)
for i in result:
    if i != 0:
        Mi.append(int(i))
print('Values of Mi Inverse:',Mi)
mul_list = []
for i1,i2,i3 in zip(a,M_a,Mi): mul_list.append(i1*i2*i3)
for i in mul_list:
    x_temp += i
x = x_temp % M
print(f'Value of X : {x}')