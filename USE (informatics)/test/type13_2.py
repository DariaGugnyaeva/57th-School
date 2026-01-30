from itertools import *

ip = [bin(int(i))[2:] for i in '172.16.168.0'.split('.')]
print(ip.count(1)) # ip 8
x = [bin(int(i))[2:] for i in '255.255.248.0'.split('.')]
print(x.count(0))  #  маске 11 изменяемых знаков


c = 0
for i in product([0,1], repeat=11):
    if (8 + sum(i))% 5 != 0:
        c += 1
print(c)
